
def atomic_sma(quotes, index, period):
	return sum(quotes[0+index:period+index])/period
	
def sma(quotes,period):
	return [atomic_sma(quotes,i,period) for i in range(len(quotes)-period+1)]
	
def ema(quotes,period):
	result = [atomic_sma(quotes,0,period)]
	N = period
	k = 2/(1+N)
	[ result.append((k*result[i]+(1-k)*quotes[i+period])) for i in range(0,len(quotes)-period)]
	return result