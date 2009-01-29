import unittest
import indicators


# Here's our "unit tests".
class IsOddTests(unittest.TestCase):

    #def testOne(self):
    #    self.failUnless(indicators.IsOdd(1))

    #def testTwo(self):
    #    self.failIf(indicators.IsOdd(2))

	def test_sma(self):
		self.assertEqual(indicators.sma([2,3,5,6]),4)

def main():
    #print indicators.IsOdd(2)
	unittest.main()

if __name__ == '__main__':
    main()