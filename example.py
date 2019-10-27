import numpy as np
import pandas as pd

z = pd.read_csv('jokes.csv')
print(z.illoc[:])


f = open("jokes.txt","r")
x = f.read()

l = x.split(",")
y = np.random.randint(0,len(l))
print(type(l[y]))

f.close()
