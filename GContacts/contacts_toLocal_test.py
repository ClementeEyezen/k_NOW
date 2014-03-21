import sys
import getopt
import getpass
import atom
import gdata.contacts.data
import gdata.contacts.client

from data.Contact import Contact
Contact.Contact = Contact

###############################################################
####################################
# Test application for Contacts API.
# Usage:
#   $ python get_contacts_tester.py
####################################

class ContactsLocal():
    def __init__(self, email, password):
        self.gd_client = gdata.contacts.client.ContactsClient(source='[k]NOW')
        self.gd_client.ClientLogin(email, password, self.gd_client.source)
        cont = []
        try:
            query = gdata.contacts.client.ContactsQuery()
            #query.max_results = 1
            feed = self.gd_client.GetContacts(q=query) #the feed can be treated like the cal list
            cont = [None]*len(feed.entry)
            for i, entry in enumerate(feed.entry):
                try:
                    print '\n%s %s' % (i+1, entry.name.full_name.text)+" - "
                except:
                    pass
                # Display the email addresses for the contact.
                email_list = []
                for email in entry.email:
                    print '    %s' % str(email.address)
                    email_list.append(email.address)
                # Contact ID
                print 'ID - '+str(entry.id.text)
                #start local creation and printing
                if (entry.name != None):
                    try:
                        first_name_ = entry.name.family_name.text
                    except AttributeError, ae:
                        first_name_ = "__none__" 
                if (entry.name != None):
                    try:
                        last_name_ = entry.name.family_name.text
                    except AttributeError, ae:
                        last_name_ = "__none__" 
                lol = Contact(id_=entry.id.text, 
                              first_name=first_name_, 
                              last_name=last_name_, 
                              email_address=email_list,
                              home_phone = None,
                              mobile_phone = None,
                              work_phone=None)
                cont[i] = lol
                del lol
                del first_name_
                del last_name_
                del email_list
                try:
                    print 'lolol '+str(cont[len(cont)-2])+' llloo '+str(cont[len(cont)-1])
                except:
                    pass
                #end local creation and printing
            print 'cont (length'+str(len(cont))+')'
            print cont
            print 'local contact test'
            party = 0
            for person in cont:
                print str(party+1)+' '+str(person.toString())
                party = party + 1
            print 'end local contact test'
        except gdata.client.BadAuthentication:
            print 'Invalid user credentials given.'

###############################################################

if __name__ == '__main__':
    f = open('/home/pythoncoder/Github/k_NOW/GContacts/nothing_here.smiley','r')
    usr = f.readline()
    pas = f.readline()
    cl = ContactsLocal(usr,pas)