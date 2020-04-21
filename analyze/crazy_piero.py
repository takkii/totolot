# -*- coding: utf-8 -*-
import random, os, sys

saikoro = ["⚀","⚁","⚂","⚃","⚄","⚅"]

num = random.randint(0,1)

if(num == 0):
  sin = ' '.join([random.choice(saikoro) for i in range(5)])
  print("Dice shuffle 5 times [心] ... " + sin)
elif(num == 1): 
  gi = ' '.join([random.choice(saikoro) for i in range(5)])
  print("Dice shuffle 5 times [義] ... " + gi)
else:
  print('Error? ... not use.')

