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



###############################################################
#gd_client = gdata.contacts.data.ContactsClient(source='k_NOW')
# Authorize the client.

def PrintAllContacts(gd_client):
    feed = gd_client.GetContacts()
    for i, entry in enumerate(feed.entry):
        print '\n%s %s' % (i+1, entry.name.full_name.text)
        if entry.content:
            print '    %s' % (entry.content.text)
        # Display the primary email address for the contact.
        for email in entry.email:
            if email.primary and email.primary == 'true':
                print '    %s' % (email.address)
        # Show the contact groups that this contact is a member of.
        for group in entry.group_membership_info:
            print '    Member of group: %s' % (group.href)
        # Display extended properties.
        for extended_property in entry.extended_property:
            if extended_property.value:
                value = extended_property.value
            else:
                value = extended_property.GetXmlBlob()
            print '    Extended Property - %s: %s' % (extended_property.name, value)

def print_datemin_query_results(gd_client):
    updated_min = '2008-01-01'
    query = gdata.contacts.client.ContactsQuery()
    query.updated_min = updated_min
    feed = gd_client.GetContacts(q = query)
    for contact in feed.entry:
        print contact.name.full_name
        print 'Updated on %s' % contact.updated.text

def retrieve_contact(gd_client):
    contact = gd_client.GetContact('https://www.google.com/m8/feeds/contacts/default/full/contactId')
    # Do something with the contact.
    return contact

if __name__ == '__main__':
    main(sys.argv)