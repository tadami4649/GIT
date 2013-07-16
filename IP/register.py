from IP.models import List
import datetime
def reg(IP):
	count = 249
	last  = 10
	while (last<=count):
		original = IP
		IP = IP + str(count)
		p = List(ip = IP, user=" ", machine=" ", location="", note=" ",date = datetime.datetime.now())
		p.save()
		IP = original
		count -= 1

