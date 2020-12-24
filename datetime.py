from _datetime import timedelta, datetime, tzinfo

class UTC(tzinfo):
     def utcoffset(self, dt):
         return timedelta(0)

     def dst(self, dt):
         return timedelta(0)

     def tzname(self,dt):
          return "UTC"

source = datetime(2020, 7, 29, 7, 37, 25, tzinfo=UTC())
repr(source)

source.strftime("%Y-%m-%d %H:%M:%S")
print(source)