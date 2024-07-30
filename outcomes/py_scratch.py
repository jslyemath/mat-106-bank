import sys
sys.path.append('/home/slye/mat-106-bank/outcomes/')
import slye_math as sm
import math
import random
from fractions import Fraction

def hard_line_prob():
            # Gives students a problem where the given is not 1
            # Still easy enough that the denominator of the requested fraction can be obtained by subdivision of orig denom

            shape = 'line'
            # Choose from tick locations that have lots of divisors
            orig_loc = random.choice([12, 16, 18, 20, 24, 28, 30])

            # Given numerator must divide tick location, but avoid original tick location itself
            orig_loc_divisors = sm.divisors(orig_loc)
            orig_loc_divisors.remove(orig_loc)
            orig_num = random.choice(orig_loc_divisors)

            # Choose denominator that doesn't force us to simplify the fraction, and that prevents whole numbers
            potential_orig_denoms = sm.rel_primes(orig_num, stop=20)
            potential_orig_denoms.remove(1)
            orig_denom = random.choice(potential_orig_denoms)

            # To be able to subdivide, we need to carefully choose our requested denominator to share a divisor
            # Kick out 1 in certain cases to prevent edge cases
            remaining_divisors = sm.divisors(orig_loc / orig_num)
            if orig_num == 1:
                remaining_divisors.remove(1)
            k = random.choice(remaining_divisors)
            requested_denom = k * orig_denom
            potential_requested_nums = list(range(1, math.ceil(30 * orig_num * k / orig_loc)))
            
            # Prevent requested fraction from equaling given fraction
            if orig_num * requested_denom % orig_denom == 0:
                if orig_num * requested_denom // orig_denom in potential_requested_nums:
                    potential_requested_nums.remove(orig_num * requested_denom // orig_denom)
            requested_num = random.choice(potential_requested_nums)

            # Calculate tick mark of requested fraction
            requested_loc = orig_loc // (orig_num * k) * requested_num

            # Simplifying the fraction for beauty and creating fun cases where requested denom ends up less than given denom
            requested_num, requested_denom = Fraction(requested_num, requested_denom).as_integer_ratio()

            return shape, orig_loc, orig_num, orig_denom, requested_loc, requested_num, requested_denom

highest_tick = 1

for i in range(1,10000):
    shape, orig_loc, orig_num, orig_denom, requested_loc, requested_num, requested_denom = hard_line_prob()
    print(f'Given Tick: {orig_loc},\nGiven: {orig_num}/{orig_denom},\nRequested: {requested_num}/{requested_denom}\nFound At: {requested_loc}\n\n')
    if requested_loc > highest_tick:
        highest_tick = requested_loc

print(highest_tick)