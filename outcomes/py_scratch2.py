import sys
sys.path.append('/home/slye/mat-106-bank/outcomes/')
import slye_math as sm
import random


def check_and_cast_to_int(value):
    try:
        return int(value), True
    except ValueError:
        return value, False


def flex_mult(a, b):
    a, a_is_int = check_and_cast_to_int(a)
    b, b_is_int = check_and_cast_to_int(b)

    if a_is_int and b_is_int:
        ab = a * b
    elif a_is_int:
        if len(b) > 1:
            b = f'({b})'
        ab = str(a) + b
    elif b_is_int:
        if len(a) > 1:
            a = f'({a})'
        ab = str(b) + a
    else:
        if len(b) > 1:
            b = f'({b})'
        if len(a) > 1:
            a = f'({a})'
        ab = a + b
    return ab
    

def div_statement(a=None, b=None, vocab_mode='e', default_order=True, use_not=False):
    # When a and b are integers, they will be ordered automatically for a true statement
    # Else, they will be ordered as entered
    # Use default_order=False to reverse the order in either case
    # Vocab types: 'e' - dividEs, 'o' - divisOr of, 'f' - Factor of, 'm' - Multiple of
    # use_not converts to not statement
    
    if a is None or b is None:
        a = int(random.randint(2, 12))
        b = a * int(random.randint(2, 12))
    
    else:
        a, a_is_int = check_and_cast_to_int(a)
        b, b_is_int = check_and_cast_to_int(b)
        if a_is_int and b_is_int:
            a, b = sorted([a, b])

    match vocab_mode:
        case 'e':
            connecting_string = 'does not divide' if use_not else 'divides'
        case 'o':
            connecting_string = 'is not a divisor of' if use_not else 'is a divisor of'
        case 'f':
            connecting_string = 'is not a factor of' if use_not else 'is a factor of'
        case 'm':
            connecting_string = 'is not a multiple of' if use_not else 'is a multiple of'
            a, b = b, a
    
    if not default_order:
        a, b = b, a
    
    prob = f'{a} {connecting_string} {b}'
    return prob

print(div_statement())

vars = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'm', 'n',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def mult_statement(ans=True, already_used=[]):
    available_versions_dict = {'larger multiple': 0.4, 'smaller factor': 0.4, 'every-is': 0.2}
    if set(already_used) == set(available_versions_dict.keys()):
        available_versions_list = list(available_versions_dict.keys())
        available_versions_weights = list(available_versions_dict.values())
    if set(already_used) != set(available_versions_dict.keys()):
        available_versions_list = [x for x in available_versions_dict.keys() if x not in already_used]
        available_versions_weights = [v for k, v in available_versions_dict.items() if k in available_versions_list]
    ver = random.choices(available_versions_list, available_versions_weights)[0]

    vocab = random.choice(['e', 'o', 'f', 'm'])
    a = random.choice(vars)
    second_variable = random.choices([False, True], [0.8, 0.2])[0]

    if second_variable: 
        vars.remove(a)
        b = random.choice(vars)
    else:
        b = random.choice([3, 4, 6, 7, 8, 9])

    swap = random.choice([True, False])
    if swap:
        a, b = b, a
    
    multiplier = int(random.randint(2, 9))
    b_mult = flex_mult(b, multiplier)

    match ver:
        case 'larger multiple':
            prob = (f'If {div_statement(a, b, vocab_mode=vocab, default_order=ans)}, '
                    f'then {div_statement(a, b_mult, vocab_mode=vocab, default_order=ans)}.')
        case 'smaller factor':
            prob = (f'If {div_statement(b_mult, a, vocab_mode=vocab, default_order=ans)}, '
                    f'then {div_statement(b, a, vocab_mode=vocab, default_order=ans)}.')
        case 'every-is':
            match vocab:
                case 'o':
                    vocab_statement = 'divisor of'
                case 'e':
                    vocab_statement = random.choice(['divisor of', 'factor of'])
                case 'f':
                    vocab_statement = 'factor of'
                case 'm':
                    vocab_statement = 'multiple of'
                    prob = f'Every {vocab_statement} {b_mult} is a {vocab_statement} {b}.'
            if vocab in ['o', 'e', 'f']:
                prob = f'Every {vocab_statement} {b} is a {vocab_statement} {b_mult}.'
    return prob, ver


def mult_false():
    vocab = random.choice(['e', 'o', 'f', 'm'])
    a = int(random.randint(2, 9))
    a_mult = int(random.randint(2, 6)) * a
    b = random.choice(vars)
    prob = (f'If {div_statement(a, b, vocab_mode=vocab)} '
            f'and {div_statement(a_mult, b, vocab_mode=vocab)}, '
            f'then {div_statement(a * a_mult, b, vocab_mode=vocab)}.')
    return prob

# vocab_statements_answers = random.choices([True, False], [0.5, 0.5], k=4)
# problems = [div_statement(vocab_mode=x, default_order=vocab_statements_answers) for x in ['o', 'e', 'f', 'm']]

# if_then_answers = [False, True] + random.choices([True, False], [0.5, 0.5], k=2)
# remaining_if_then_answers = if_then_answers[:]
# if_then_versions = ['sum', 'mult', 'sum', 'mult']
# random.shuffle(if_then_versions)

# use_an_always_false = random.choices([True, False], [0.6, 0.4])[0]
# already_used_mult = []
# already_used_sum = []
# if use_an_always_false:
#     if if_then_versions[0] == 'sum':
#         problems.append(mult_false())
#     else:
#         problems.append(mult_false())
#     remaining_if_then_answers = if_then_answers[1:]
# for ans in remaining_if_then_answers:
#     prob, ver = mult_statement(ans=ans, already_used=already_used_mult)
#     already_used_mult.append(ver)
#     problems.append(prob)

# answers = vocab_statements_answers + if_then_answers

# print(problems)
# print(answers)

# prob_ans = list(zip(problems, answers))

# random.shuffle(prob_ans)