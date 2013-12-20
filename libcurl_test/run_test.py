from libcurl_test import angry_test

def main():
    print "begin test"
    ant = angry_test.Angry_Test()
    print ":::ant.imap_test()"
    ant.imap_test()
    print "complete"

if __name__=="__main__":
    main()