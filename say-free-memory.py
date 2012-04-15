#coding:utf8
import android,commands,re

droid = android.Android()
result = commands.getoutput("cat /proc/meminfo")
patern = re.compile("[0-9]+ kB")
result = result.split("\n")

print result


for line in result:
    if line.find("MemTotal") != -1:
        total = int(line.split(" ")[-2])
    elif line.find("MemFree") != -1:
        free = int(line.split(" ")[-2])
    elif line.find("Inactive") != -1:
        inactive = int(line.split(" ")[-2])
        
print "total = %d" % total
print "free = %d" % free
print "inactive = %d" % inactive


print "memory of free = %dMB" % ((free+inactive)/1000)
#print "free %f" % ((free+inactive)/total/100.0)

droid.makeToast("free memory %dMB" % ((free+inactive)/1000))
droid.ttsSpeak("%d mega byte are free" %((free+inactive)/1000))

