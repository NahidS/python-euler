fiboseq = [1, 2]
index = 0
sum = 2
while fiboseq[index] <= 4000000:
	index = len(fiboseq)
	fiboseq.append(fiboseq[index - 2] + fiboseq[index - 1])
	if (fiboseq[index] % 2) == 0:
		sum += fiboseq[index]
print(sum)