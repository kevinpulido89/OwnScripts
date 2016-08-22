from datetime import datetime
import statistics
print ((datetime.now()).month)
now = datetime.now()

print ('%s/%s/%s' % (now.month, now.day, now.year))
print ('%s:%s:%s' % (now.hour, now.minute, now.second))