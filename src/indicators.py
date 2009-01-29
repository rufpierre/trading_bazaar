

# Here's our "unit".
def IsOdd(n):
    return n % 2 == 1


def sma(quotes,period):
	#return sum(quotes)/len(quotes)
	#print range(len(quotes))
	return [sum(quotes[0+i:period+i])/period for i in range(len(quotes)-period+1)]
	
def ema(quotes):
	return []