import collections
import pprint

with open("/home/saleemuddin1/PythonSS/ceaser1.txt", 'r') as info:
  counting = collections.Counter(info.read().upper())
  valHold = pprint.pformat(counting)
print(valHold)
