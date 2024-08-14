import sys
sys.path.append('/home/slye/mat-106-bank/outcomes/')
import slye_math as sm
import random
from fractions import Fraction
from decimal import Decimal, localcontext, ROUND_DOWN

double_count = 0
for i in range(1,10000):
    a = sm.random_person()
    b = sm.random_person(avoid=a)
    if a.name == b.name:
        double_count += 1

print(double_count)
