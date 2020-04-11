import random

saikoro = ["⚀","⚁","⚂","⚃","⚄","⚅"]
han = ' '.join([random.choice(saikoro) for i in range(5)])
print("Dice shuffle 5 times ... " + han)