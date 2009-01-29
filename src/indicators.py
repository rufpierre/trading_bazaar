

# Here's our "unit".
def IsOdd(n):
    return n % 2 == 1


def sma(quotes,period):
	#return sum(quotes)/len(quotes)
	print range(len(quotes))
	return [sum(quotes[0:period]) for i in range(len(quotes))]
	
def ema(quotes):
	return []