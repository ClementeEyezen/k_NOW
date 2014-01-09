from datetime import datetime

import atom.data
import gdata.data
import gdata.contacts.client
import gdata.contacts.data

from data import Token

class Contact():
    def __init__(self,id_,first_name,last_name,email_address,home_phone,mobile_phone,work_phone):
        global fi_name
        fi_name = str(first_name)
        global la_name
        la_name = str(last_name)
        global online_id
        online_id = str(id_)
        global email_list
        email_list = []
        if isinstance(email_address,list):
            for email in email_address:
                email_list.append(str(email))
        else:
            email_list.append(str(email_address))
        global h_phone
        h_phone = str(home_phone)
        global w_phone
        w_phone = str(work_phone)
        global m_phone
        m_phone = str(mobile_phone)
    
    def update(self):
        #update contact info, and update the last-updated contact field
        pass
    
    def toString(self):
        '''full=False
        if(isinstance(full,bool)):
            if(full):
                lines = ''+str(fi_name)+' '+str(la_name)+'\n'
                lines = 'ID:'+lines+str(id)+'\nEMAIL:'
                for email in email_list:
                    lines = lines+str(email)+', '
                lines = lines + '\n'
                if (h_phone is str and h_phone is not None):
                    lines = lines+'PHONE (home):'+str(h_phone)+'\n'
                if (w_phone is str and m_phone is not None):
                    lines = lines+'PHONE (work):'+str(w_phone)+'\n'
                if (m_phone is str and m_phone is not None):
                    lines = lines+'PHONE (cell):'+str(m_phone)+'\n'
                return lines
        '''
        #print 'stringing '+str(online_id[len(online_id)-5:len(online_id)])
        return str(la_name)+' '+str(online_id[len(online_id)-5:len(online_id)])
    
    def addToken_list(self,item_list):
        #adds tokens from a list
        #returns true if item_list is a list and items were considered for adding
        #returns false if item_list is not a list
        #returns false if one or more items were not Tokens
        bool_test = True
        if isinstance(item_list, list):
            for tok in item_list:
                bool_test = bool_test and self.addToken(tok)
            return bool_test
        else:
            return False
        
    def addToken(self,item):
        #adds tokens that are associated with this event
        #returns true if successfully added
        #returns false if the item was not a token
        global token_list
        if item is Token:
            token_list.append(item)
            return True
        else:
            return False
        
    def set_id(self,id_):
        global online_id
        online_id = id_
        
    def addEmail(self,item):
        global email_list
        email_list.append(str(item))
    
    def gen_attendee(self):
        #generate/return an attendee output for calendar events
        global email_list
        try:
            return {
                    'email': email_list.get(0)
                    }
        except:
            print 'Attendee error\nLikely cause: no emails found in the contact\'s email_list'

    
    def gen_googleCompatible(self):
        #generate/return a contact creation output for Google contacts
        new_contact = gdata.contacts.data.ContactEntry()
        # Set the contact's name.
        new_contact.name = gdata.data.Name(
                                           given_name=gdata.data.GivenName(text=fi_name),
                                           family_name=gdata.data.FamilyName(text=la_name),
                                           full_name=gdata.data.FullName(text=fi_name+' '+la_name)
                                           )
        #Set the contact's note
        stri = '__Tokens__+\n'
        for token in token_list:
            stri = stri+token+'\n'
        new_contact.content = atom.data.Content(text=str)
        #Set the contact's email addresses
        for index, email_ in enumerate(email_list):
            primaryYN = (index == 0)
            if primaryYN:
                new_contact.email.append(gdata.data.Email(address=email_,
                                                          primary='true', 
                                                          rel=gdata.data.HOME_REL, 
                                                          display_name=str(fi_name+' '+la_name))
                                         )
            else:
                new_contact.email.append(gdata.data.Email(address=email_,
                                                          primary='false', 
                                                          rel=gdata.data.HOME_REL, 
                                                          display_name=str(fi_name+' '+la_name))
                                         )
        #Set the contact's phone numbers
        # Set the contact's phone numbers.
        global w_phone
        if w_phone is not None:
            new_contact.phone_number.append(gdata.data.PhoneNumber(text=w_phone,
                                                                    rel=gdata.data.WORK_REL))
        global h_phone
        if h_phone is not None:
            new_contact.phone_number.append(gdata.data.PhoneNumber(text=h_phone,
                                                                    rel=gdata.data.HOME_REL, primary='true'))
        global m_phone
        if m_phone is not None:
            new_contact.phone_number.append(gdata.data.PhoneNumber(text=m_phone,
                                                                   rel=gdata.data.HOME_REL))
        return new_contact
    
    def create_online_contact(self,gd_client):
        contact_entry = gd_client.CreateContact(self.gen_googleCompatible())
        print "Contact's ID: %s" % contact_entry.id.text
        self.set_id(contact_entry.id.text)
