import h5py
import numpy as np
import random as rand
f = h5py.File("testFile.h5","w")

group = f.create_group("Sugars")

data = group.create_dataset("glucose",(10,2),dtype='i')
data[0,0] = 1
data[0,1] = 1
for i in range(1,10,1):
  data[i,0] = data[i-1,1]
  data[i,1] = data[i-1,0] + data[i-1,1]
#f['glucose'] = data

data2 = group.create_dataset("lactose",(8,8),dtype='i')
for i in range(8):
  for j in range(8):
    if (i%2 == j%2):
      data2[i,j] = 1

def complement(string):
  if (string=="A"): return "T"
  elif (string=="T"): return "A"
  elif (string=="C"): return "G"
  elif (string=="G"): return "C"

def nucleotide(val):
  if (0<val<0.25): return "A"
  elif (0.25<val<0.5): return "C"
  elif (0.5<val<0.75): return "T"
  elif (val<1): return "G"

group2 = f.create_group("Nucleic_Acids")
d = group2.create_dataset("DNA",(10,2),dtype="S1")
for i in range(10):
  temp = rand.random()
  d[i,0] = nucleotide(temp)
  d[i,1] = complement(d[i,0])

print("Sugars/glucose" in f)
print("Nucleic_Acids/DNA" in f)
