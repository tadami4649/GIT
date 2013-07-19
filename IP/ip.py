from models import List
from threading import Thread
import subprocess
from Queue import Queue


num_threads = 4
queue = Queue()
ips = []
for temp in List.objects.all():
	ips.append(temp.ip)
ips.reverse()

def pinger(i, q):
    while True:
	ip = q.get()
        print "3"
	ret = subprocess.call("ping -c 1 %s" % ip,
			shell=True,
			stdout=open('/dev/null', 'w'),
			stderr=subprocess.STDOUT)
	if ret == 0:
	    print "%s: is alive" % ip
	else:
	    print "%s: did not respond" % ip
	q.task_done()


for i in range(num_threads):
    worker = Thread(target=pinger, args=(i, queue))
    worker.setDaemon(True)
    worker.start()

for ip in ips:
    print "2"
    queue.put(ip)
#queue.join()
