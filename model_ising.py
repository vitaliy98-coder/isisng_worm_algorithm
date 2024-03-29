# -*- coding: utf-8 -*-
"""Untitled28.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EjHrjcXfPuLRlx4auwAc4v46JRnOJjSu
"""



import random
import math
import csv
# 
# 
T = 1.25
L = 10
nsteps = 1000000
N = L**2
# 
nbr = {q: ((q // L) * L + (q + 1) % L, (q + L) % N,
        (q // L) * L + (q - 1) % L, (q - L) % N) for q in range(N)}
# 
bonds = {}
# 
for i in range(N):
     for m in nbr[i]:
         if tuple(sorted([i, m])) not in bonds.keys():
             bonds[tuple(sorted([i, m]))] = 0
# 
# 
def worm_alg(bonds,  T,  nsteps):
#     
     K = 1.0 / T
     inv_K = 1.0 / K
     Z = 0.0
     Nb = 0
     E_tot = 0.0
     I = 0
     M = 0
     N_b2=0
     N_b=0
#     
#         
     for step in range(nsteps):
         if I == M:
             I = random.randrange(N)
             M = I
             Z += 1.0
 
             N_b2+=(Nb*Nb-Nb)
             N_b+=Nb
             
             E_tot += - T * Nb
#     
         new_M = random.choice(nbr[M])
         bond = tuple(sorted([M, new_M]))
         nb = bonds[bond]
         if random.uniform(0.0, 1.0) < 0.5:
             delta_nb = 1
             #P_acc = math.tanh(K)
             P_acc = K / (nb + 1.0)
#         
         else:
             delta_nb = -1
         
             #P_acc = math.atanh(K)
             P_acc = nb * inv_K
         if random.uniform(0.0, 1.0) < P_acc:
             bonds[bond] += delta_nb
             Nb += delta_nb
# 
             M = new_M
     #print(E_tot / Z / float(N))   
     return (((N_b2/Z)-(N_b/Z)**2)/float(N)) , (E_tot / Z / float(N))
# 
# temp=[]
# 
with open('data.csv', 'w') as file:
     writer = csv.writer(file)
# 
     for n in range(40):
       for f in range(2):
         a,b=worm_alg(bonds,  T+n*0.051,  nsteps)
         l=[list(bonds.values())]
         print(T+n*0.051,b)
#         
         writer.writerows(l)
#   
         bonds = {}
         for p in range(N):
           for j in nbr[p]:
             if tuple(sorted([p, j])) not in bonds.keys():
               bonds[tuple(sorted([p, j]))] = 0
# 
# #with open('data.csv', 'w') as file:
#     #writer = csv.writer(file)
#     #writer.writerows(temp)
# #print(temp)
#