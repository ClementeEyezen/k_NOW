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
    """ContactsSample object demonstrates operations with the Contacts feed."""

    def __init__(self, email, password):
        self.gd_client = gdata.contacts.client.ContactsClient(source='GoogleInc-ContactsPythonSample-1')
        self.gd_client.ClientLogin(email, password, self.gd_client.source)
        try:
            feed = self.gd_client.GetContacts() #the feed can be treated like the cal list
            for i, entry in enumerate(feed.entry):
                print '\n%s %s' % (i+1, entry.name.full_name.text)
            # Display the primary email address for the contact.
            for email in entry.email:
                if email.primary and email.primary == 'true':
                    print '    %s' % (email.address)
        except gdata.client.BadAuthentication:
            print 'Invalid user credentials given.'



###############################################################