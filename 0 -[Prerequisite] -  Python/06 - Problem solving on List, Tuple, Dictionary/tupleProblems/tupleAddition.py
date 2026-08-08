t1 = (1, 2, 3)
t2 = (4, 5, 6)
summed_tuple = tuple(t1[i]+t2[i] for i in range(len(t1)))
print(summed_tuple)