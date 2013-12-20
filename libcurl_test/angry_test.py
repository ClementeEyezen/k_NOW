import pycurl
import cStringIO

class Angry_Test():
    def __init__(self):
        pass
    
    def catch_output(self):
        buf = cStringIO.StringIO()
        url_string = 'https://news.ycombinator.com'
        pycurl.global_init(pycurl.GLOBAL_ALL)
        
        c = pycurl.Curl()
        c.setopt(c.URL, url_string)
        c.setopt(c.WRITEFUNCTION, buf.write)
        c.perform()
 
        print buf.getvalue()
        buf.close()
        
        
        pycurl.global_cleanup()
    def imap_test(self):
        buf = cStringIO.StringIO()
        url_string = 'imap://username:password@imap.google.com/u/0/#inbox/;UID=1'
        pycurl.global_init(pycurl.GLOBAL_ALL)
        
        c = pycurl.Curl()
        c.setopt(c.URL, url_string)
        c.setopt(c.WRITEFUNCTION, buf.write)
        c.perform()
 
        print buf.getvalue()
        buf.close()
        
        
        pycurl.global_cleanup()