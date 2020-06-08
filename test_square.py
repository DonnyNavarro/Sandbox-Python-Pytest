import math

def test_sqrt():
   """An example of a passing test"""
   num = 25
   assert math.sqrt(num) == 5

def testSquare():
   """An example of a failing test"""
   num = 7
   assert 7*7 == 40

def tesequality():
   """An example of an ignored test"""
   assert 10 == 11
