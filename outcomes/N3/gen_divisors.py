import pprint

# Use this to generate divisor lists of your choosing, then paste it into the generator.

primes_too_big = [17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

divisors_dict = {}

for i in range(2, 101):
    divisors = []
    for j in range(1,i//2 + 1):
        if i % j == 0:
            divisors.append(str(j))
    divisors.append(str(i))
    divisors_dict[f'{i}'] = {'divisors_list': divisors}
    divisors_dict[f'{i}']['len'] = len(divisors)
    divisors_dict[f'{i}']['available_multiples'] = []
    divisors_dict[f'{i}']['relative_primes'] = []
    divisors_dict[f'{i}']['shares_prime_only'] = []
    divisors_dict[f'{i}']['shares_smaller_composite'] = []
    # While I get rid of this later, you could choose to keep if you decide to include primes in your own list
    divisors_dict[f'{i}']['prime'] = False if len(divisors) >2 else True

filtered_divisors_dict = {k: v for k, v in divisors_dict.items() 
                          if v['prime'] is False 
                          and v['len'] <= 8
                          and set(v['divisors_list']).intersection(primes_too_big) == set()}


# List out what multiples of a number still exist in the filtered dictionary
for test_num in filtered_divisors_dict.keys():
    multiples = [k for k in filtered_divisors_dict.keys() 
                 if int(k) > int(test_num)
                 and int(k) % int(test_num) == 0]
    if len(multiples) == 0:
        multiples = None
    filtered_divisors_dict[test_num]['available_multiples'] = multiples

    # Pop off prime while we're in this loop anyway
    filtered_divisors_dict[test_num].pop('prime')

for test_num, test_num_dict in filtered_divisors_dict.items():
    relatively_prime = []
    shares_prime_with = []
    shares_composite_with = []

    for other_num, other_num_dict in filtered_divisors_dict.items():
        if len(set(test_num_dict['divisors_list']).intersection(other_num_dict['divisors_list'])) == 1:
            relatively_prime.append(other_num)
        if test_num != other_num:
            if len(set(test_num_dict['divisors_list']).intersection(other_num_dict['divisors_list'])) == 2:
                shares_prime_with.append(other_num)
            if (len(set(test_num_dict['divisors_list']).intersection(other_num_dict['divisors_list'])) > 2
                and int(test_num) % int(other_num) != 0
                and int(other_num) % int(test_num) != 0):
                shares_composite_with.append(other_num)

    if relatively_prime == []:
        relatively_prime = None
    if shares_prime_with == []:
        shares_prime_with = None
    if shares_composite_with == []:
        shares_composite_with = None

    filtered_divisors_dict[test_num]['relative_primes'] = relatively_prime
    filtered_divisors_dict[test_num]['shares_prime_only'] = shares_prime_with
    filtered_divisors_dict[test_num]['shares_smaller_composite'] = shares_composite_with
    # print(f'{test_num}: {filtered_divisors_dict[test_num]["shares_smaller_composite"]}')

pprint.pprint(filtered_divisors_dict, compact=True, sort_dicts=False, width=108)