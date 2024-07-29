import pprint

# Use this to generate divisor lists of your choosing, then paste it into the generator.
def dd():
    denoms_dict = {}

    for i in range(1, 26):
        divisors = []
        for j in range(1,i//2 + 1):
            if i % j == 0:
                divisors.append(j)
        divisors.append(i)
        denoms_dict[i] = {'divisors': divisors}
        # denoms_dict[i]['len'] = len(divisors)
        denoms_dict[i]['multiples'] = []
        denoms_dict[i]['relative_primes'] = []
        denoms_dict[i]['shares_divisors'] = []
        # denoms_dict[i]['shares_prime_only'] = []
        # denoms_dict[i]['shares_smaller_composite'] = []
        # While I get rid of this later, you could choose to keep if you decide to include primes in your own list
        # denoms_dict[i]['prime'] = False if len(divisors) >2 else True

    filtered_denoms_dict = denoms_dict # {k: v for k, v in denoms_dict.items() if v['prime'] is False}


    # List out what multiples of a number still exist in the filtered dictionary
    for test_num in filtered_denoms_dict.keys():
        multiples = [k for k in filtered_denoms_dict.keys() 
                    if int(k) > int(test_num)
                    and int(k) % int(test_num) == 0]
        # if len(multiples) == 0:
        #     multiples = None
        filtered_denoms_dict[test_num]['multiples'] = multiples

        # Pop off prime while we're in this loop anyway
        # filtered_denoms_dict[test_num].pop('prime')

    for test_num, test_num_dict in filtered_denoms_dict.items():
        relatively_prime = []
        shares_divisors_with = []

        for other_num, other_num_dict in filtered_denoms_dict.items():
            if len(set(test_num_dict['divisors']).intersection(other_num_dict['divisors'])) == 1:
                relatively_prime.append(other_num)
            if test_num != other_num:
                if (len(set(test_num_dict['divisors']).intersection(other_num_dict['divisors'])) >= 2
                    and int(test_num) % int(other_num) != 0
                    and int(other_num) % int(test_num) != 0):
                    shares_divisors_with.append(other_num)

        # if relatively_prime == []:
        #     relatively_prime = None
        # if shares_divisors_with == []:
        #     shares_divisors_with = None

        filtered_denoms_dict[test_num]['relative_primes'] = relatively_prime
        filtered_denoms_dict[test_num]['shares_divisors'] = shares_divisors_with
        return filtered_denoms_dict

pprint.pprint(dd(), compact=True, sort_dicts=False, width=108)