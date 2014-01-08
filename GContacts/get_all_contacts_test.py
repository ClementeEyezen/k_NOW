import sys
import getopt
import getpass
import atom
import gdata.contacts.data
import gdata.contacts.client



###############################################################
####################################
# Test application for Contacts API.
# Usage:
#   $ python get_contacts_tester.py
####################################

class ContactsTest(object):
    def __init__(self, email, password):
        self.gd_client = gdata.contacts.client.ContactsClient(source='GoogleInc-ContactsPythonSample-1')
        self.gd_client.ClientLogin(email, password, self.gd_client.source)
        try:
            query = gdata.contacts.client.ContactsQuery()
            query.max_results = 10
            feed = self.gd_client.GetContacts(q=query) #the feed can be treated like the cal list
            for i, entry in enumerate(feed.entry):
                try:
                    print '\n%s %s' % (i+1, entry.name.full_name.text)
                except:
                    pass
                # Display the email addresses for the contact.
                for email in entry.email:
                    print '    %s' % str(email.address)
                # Contact ID
                print 'ID - '+str(entry.name)
                # Display extended properties.
                for extended_property in entry.extended_property:
                    if extended_property.value:
                        value = extended_property.value
                    else:
                        value = extended_property.GetXmlBlob()
                    print '    Extended Property - %s: %s' % (extended_property.name, value)
        except gdata.client.BadAuthentication:
            print 'Invalid user credentials given.'

###############################################################

if __name__ == '__main__':
    f = open('/home/pythoncoder/Github/k_NOW/GContacts/nothing_here.smiley','r')
    usr = f.readline()
#    print 'read '+str(usr)+'\n'
    pas = f.readline()
    cs = ContactsTest(usr,pas)