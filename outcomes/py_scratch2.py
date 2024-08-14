import sys
sys.path.append('/home/slye/mat-106-bank/outcomes/')
import slye_math as sm
import random
from fractions import Fraction
from decimal import Decimal, localcontext, ROUND_DOWN

orig_frac_dec_str = '0.4821'

quantize_places = 4
transposeds = []
for i in range(2, quantize_places + 1):
    swap_list = list(orig_frac_dec_str)
    swap_list[i], swap_list[i + 1] = swap_list[i + 1], swap_list[i]
    transposed = ''.join(swap_list)
    transposeds.append(transposed)

print(transposeds)