import re,MySQLdb
import shutil
import requests
from urllib2 import urlopen
from lxml.html import fromstring

passed = 0
fail = 0
reserve = 0

for x in range(0,30551):

	payload = {'exam_id':3145, 'exam_year':'2013','exam_month':'DEC','seat_no':x,'submit':'Go'}

        r = requests.post("http://results.mu.ac.in/get_resultb.php", data=payload)
	dom = fromstring(r.text)
	a = dom.cssselect('b')
	for text in a:
		result=text.text_content()
		if result == "FAILED.":
			fail=fail+1
		elif result == "Passed":
			passed=passed+1
		elif result == "HELD IN RESERVE.":
			reserve=reserve+1
		print str(x)+"-"+result



print "passed -"+str(passed)
print "failed -"+str(fail)
print "reserve -"+str(reserve)
