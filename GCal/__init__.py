def test():
    from GCal.CalendarManager import CalendarManager
    import os
    secret_location = os.path.join(os.path.dirname('..'), 'client_secrets.json')
    cm = CalendarManager(client_secrets=secret_location)

if __name__ == "__main__":
    test()
    exit()