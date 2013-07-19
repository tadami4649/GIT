from IP.models import List
import datetime
def reg():
        IP = "192.168.15."
	count = 249
	last  = 10
	while (last<=count):
		check = True
		original = IP
		IP = IP + str(count)
		for temp in List.objects.all():
			if temp.ip == IP:
				check = False
				break;
		if check == True:
			p = List(ip = IP, user=" ", machine=" ", location="", note=" ",date = datetime.datetime.now())
			p.save()
		IP = original
		count -= 1

