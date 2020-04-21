# -*- coding: utf-8 -*-
import random, os, sys

class Dice:
    def __init__(self):
      self.saikoro = ["⚀","⚁","⚂","⚃","⚄","⚅"]
      self.num = random.randint(0,1)

eyes = Dice().saikoro
ice = Dice().num

if(ice == 0):
  sin = ' '.join([random.choice(eyes) for i in range(5)])
  print("Dice shuffle 5 times [心] ... " + sin)
elif(ice == 1): 
  gi = ' '.join([random.choice(eyes) for i in range(5)])
  print("Dice shuffle 5 times [義] ... " + gi)
else:
  print('Error? ... not use.')

