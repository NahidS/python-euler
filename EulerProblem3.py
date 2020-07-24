import math
import numpy

number = 600851475143
primeFactors = []
sqrt = math.sqrt(number)
while number % 2 == 0:
	number = number/2
	primeFactors.append(2)
for i in numpy.arange (3, sqrt, 2):
	while number%i==0:
		primeFactors.append(i)
		number = number/i
print(primeFactors[-1])
#print(list(dict.fromkeys(primeFactors)))