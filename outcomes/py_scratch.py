import sys
sys.path.append('/home/slye/mat-106-bank/outcomes/')
import slye_math as sm
import random
from fractions import Fraction
from decimal import Decimal


def create_repeating_dec():
    period = random.randint(1, 2)
    for i in range(0, 50000):
        repetend_denom = int('9' * period)
        repetend_num = random.choice(sm.rel_primes(repetend_denom))
        repetend_frac = Fraction(repetend_num, repetend_denom)

        place_val_offset = random.randint(0, 2)
        non_repeating_digits = int(sm.int_string(place_values=place_val_offset + 1,
                                                    excl_first=[],
                                                    excl_last=[],
                                                    wt_0=0.13, wt_1=0.13, wt_2=0.13, wt_3=0.13, wt_4=0.13))
        shifter = Fraction(1, 10 ** place_val_offset)

        our_fraction = (non_repeating_digits + repetend_frac) * shifter
        fraction_num, fraction_denom = our_fraction.as_integer_ratio()
        non_repeating_dec_part = sm.dec_string(-1 * place_val_offset,
                                                custom_string=non_repeating_digits,
                                                remove_trails=False)
        if place_val_offset == 0:
            non_repeating_dec_part += '.'

        our_fraction_latex = f'\\dfrac{{{fraction_num}}}{{{fraction_denom}}}'
        our_decimal_latex = non_repeating_dec_part + f'\\overline{{{repetend_num}}}'

        output = (our_fraction_latex, our_decimal_latex)

        if fraction_denom == 9 and fraction_denom > 9:
            return output

        if fraction_denom != repetend_denom and fraction_num < 1000 and fraction_denom < 1000:
            return output

    return output

n, d, l = create_repeating_dec()
print(f'Fraction: {n}/{d}\nDecimal: {l}')