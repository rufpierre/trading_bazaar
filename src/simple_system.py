# fit indicators

from decimal import *
from math import *
from random import *
import shutil
import os
import copy

quotes_path = "/Users/pierre/Data/yahoo_quotes/"

actual_quotes = False

if (actual_quotes):
	shutil.copy(quotes_path+"USDCHF/200901", "temp_rtq.txt")
	os.system('cat temp_rtq.txt|uniq>temp_rtq_uniq.txt')
	os.system('rm temp_rtq.txt')



facts = []
f = file("temp_rtq_uniq.txt", "r")
#f.readlines()
for line in f:
        facts.append(line.rstrip().split(','))
f.close()

if (actual_quotes):
	os.system('rm temp_rtq_uniq.txt')



#facts[0:1] = []


quotes =([float(x[1]) for x in facts])



#quotes = map(lambda x: x + random()/100,quotes)

#quotes.append(0.5)
#quotes.append(0.5)
#quotes.append(0.5)
#quotes.append(0.5)

if (False):
	quotes2 = copy.deepcopy(quotes)
	while (len(quotes2)>0):
		print quotes2.pop(0)

#quotes = quotes[:10]

#print quotes

def offsets(in_list,offset):
	return in_list[:len(in_list)+offset]

#print offsets(quotes,-3)


def sma(in_quotes,period,time=0):
	quotes = offsets(in_quotes,time)
	return sum(quotes[-period:])/period

def sma2(quotes,period,acc=[]):
	if (len(quotes)>period):
		acc.append(sma2(quotes[:-1],period,acc))
	else:
		acc.append(sum(quotes)/period)
	
print quotes

#print (sma (copy.copy(quotes),2))	
print (sma2(copy.copy(quotes),2))	

def ema(in_quotes,period,time=0):
	quotes = offsets(in_quotes,time)
	if (len(quotes)==period):
		result = sma(quotes, period)
		print(result)
		return result
	else:
		k=2.0/(period+1)
		result = k*quotes.pop()+(1-k)*ema(copy.copy(quotes), period)
		print(result)
		return result
	
#print (ema(quotes,2,-1))	
	

#print sma(quotes[:6],2,-1)

if (False):
	k=10
	while(k>0):
		print "ema"
		k = k-1
	
#print ema(quotes,5,-1)







