from datetime import datetime
from datetime import timedelta

start = str(datetime.now())
end = str(datetime.now()+timedelta(0,3600))
print '__non-mod__'
print 'start = '+start
print 'end = '+end
start = start.replace(' ', 'T')
end = end.replace(' ', 'T')
print '__mod__'
print 'start = '+start
print 'end = '+end
