from ipwhois import IPWhois
from pprint import pprint
import time
import socket

target = raw_input("Enter a hostname or an IP: ")

temp = list(target.split("."))

Subnet = 0;

for digit in temp:
	if(digit.isdigit() is True):
		Subnet -= 1; 

if(Subnet is 0):
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

