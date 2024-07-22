import pprint

# Use this to generate "steps" of your choosing, then paste it into the generator.
# I was lazy and re-used code from the GCD problem, so it is way over-engineered and roundabout here.

divisors_dict = {}

for i in range(2, 14):
    divisors = []
    for j in range(1,i//2 + 1):
        if i % j == 0:
            divisors.append(j)
    divisors.append(i)
    divisors_dict[i] = {'divisors_list': divisors}
    divisors_dict[i]['relative_primes'] = []

for test_num, test_num_dict in divisors_dict.items():
    relatively_prime = []
    for other_num, other_num_dict in divisors_dict.items():
        if len(set(test_num_dict['divisors_list']).intersection(other_num_dict['divisors_list'])) == 1:
            relatively_prime.append(int(other_num))

    if relatively_prime == []:
        relatively_prime = None

    divisors_dict[test_num]['relative_primes'] = relatively_prime

    relative_primes_dict = {k: v['relative_primes'] for k, v in divisors_dict.items()}

pprint.pprint(relative_primes_dict, compact=True, sort_dicts=False, width=108)