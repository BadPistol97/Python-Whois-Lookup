from ipwhois import IPWhois
from pprint import pprint
import time
import socket

target = raw_input("Enter a hostname or an IP: ")

if(len(list(target.split("."))) != 4):
	target = socket.gethostbyname(target)

obj = IPWhois(target)

print "Whois lookup running ",

res = obj.lookup_rdap()

for x in range(0,3):
	time.sleep(0.5)
	print ". ",

time.sleep(0.5)

pprint(res)

#print(res["nets"][0]["country"])

