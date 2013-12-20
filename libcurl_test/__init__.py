#the init script for testing libcurl functionality
import pycurl
import cStringIO

def test_main0():
    print "begin testing"
    pycurl.global_init(pycurl.GLOBAL_ALL)
    ###pycurl test functionality here
    print ":::pycurl.version"
    print pycurl.version
#    print "pycurl.version_info() # tuple"
#    print pycurl.version_info()
    curl_object = pycurl.Curl()
    print ":::curl_object"
    print curl_object
    
    #example code started from the following site
    # ::http://www.angryobjects.com/2011/10/15/http-with-python-pycurl-by-example/
    
    curl_object.setopt(curl_object.URL, 'http://news.ycombinator.com')
    curl_object.perform()
    
    ###end pycurl testing and such
    pycurl.global_cleanup()

def test_main1():
    print "begin testing 1"
    #code from http://www.angryobjects.com/2011/10/15/http-with-python-pycurl-by-example/
    
    buf = cStringIO.StringIO()
    
    pycurl.global_init(pycurl.GLOBAL_ALL)
    c = pycurl.Curl()
    c.setopt(c.URL, 'https://news.ycombinator.com')
    c.setopt(c.WRITEFUNCTION, buf.write)
    c.perform()
    
    print buf.getvalue()
    buf.close()
    pycurl.global_cleanup()

if __name__=="__main__":
    test_main1()
