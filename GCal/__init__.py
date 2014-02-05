def test():
    from GCal.CalendarManager import CalendarManager
    import os
    secret_location = os.path.join(os.path.dirname('..'), 'client_secrets.json')
    cm = CalendarManager(client_secrets=secret_location)

def test1():
    a = [0,1,2,3,4,5,6]
    b = -1
    c = []
    for index , item in enumerate(a):
        b = item
        c.append(b)
        del b
    print 'a '+str(a)
    print 'c '+str(c)

if __name__ == "__main__":
    test1()
    exit()