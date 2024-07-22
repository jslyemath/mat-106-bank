import random
# import sys


def main():
    pass


def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False


def int_string(place_values=1, excl_first=[0], excl_last=[], wt_0=None, wt_1=None, wt_2=None, wt_3=None, wt_4=None,
                wt_5=None, wt_6=None, wt_7=None, wt_8=None, wt_9=None):
    the_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    wt_list = [wt_0, wt_1, wt_2, wt_3, wt_4, wt_5, wt_6, wt_7, wt_8, wt_9]
    non_wtd = sum(1 for wt in wt_list if wt is None)
    if non_wtd == 10:
        for i in range(len(wt_list)):
            wt_list[i] = 0.1
    elif non_wtd > 0:
        wt_rem = 1 - sum(wt for wt in wt_list if wt is not None)
        wt_rem_split = wt_rem / non_wtd

        for i in range(len(wt_list)):
            if wt_list[i] is None:
                wt_list[i] = wt_rem_split

    if excl_first is None:
        excl_first = []

    if excl_last is None:
        excl_last = []

    def exclude_digits(excluded):
        if is_iterable(excluded) is False:
            excluded = [excluded]
        return list(filter(lambda w: w not in excluded, the_digits))

    first_digits = exclude_digits(excl_first)
    fd_wt_list = []
    for digit in first_digits:
        fd_wt_list.append(wt_list[digit])

    last_digits = exclude_digits(excl_last)
    ld_wt_list = []
    for digit in last_digits:
        ld_wt_list.append(wt_list[digit])

    first_digit = random.choices(first_digits, weights=fd_wt_list, k=1)
    middle_digits = random.choices(the_digits, weights=wt_list, k=place_values - 2)
    if place_values == 1:
        last_digit = []
    else:
        last_digit = random.choices(last_digits, weights=ld_wt_list, k=1)
    all_digits = first_digit + middle_digits + last_digit
    all_digits_strings = [str(digit) for digit in all_digits]

    our_int_string = ''.join(all_digits_strings)

    return our_int_string

def dec_string(dec_offset=-1, place_values=1, excl_first=[0], excl_last=[0], wt_0=None, wt_1=None, wt_2=None, wt_3=None, wt_4=None,
                wt_5=None, wt_6=None, wt_7=None, wt_8=None, wt_9=None, custom_string=None, separator=','):
    
    dec_offset = int(dec_offset)

    if separator == None:
        separator = ''

    if custom_string == None:
        our_int_string = int_string(place_values, excl_first, excl_last, wt_0, wt_1, wt_2, wt_3, wt_4, wt_5, wt_6, wt_7, wt_8, wt_9)
    else:
        our_int_string = custom_string
    
    our_int_string = str(our_int_string).replace(',', '')

    # if dec_offset == 0:
    #     our_dec_string = f'{int(our_int_string):,}'
    if dec_offset < 0:
        whole_part = our_int_string
        dec_part = ''
        if '.' in our_int_string:
            whole_part, dec_part = our_int_string.split('.', 1)
        if abs(dec_offset) >= len(whole_part):
            num_extra_zeros = 1 + abs(dec_offset) - len(whole_part)
            whole_part = '0' * num_extra_zeros + whole_part
        new_dec_part = whole_part[dec_offset:] + dec_part
        new_dec_part = new_dec_part.rstrip('0')
        new_whole_part = f'{int(whole_part[:dec_offset]):,}' if whole_part[:dec_offset] != '' else ''
        our_dec_string = new_whole_part + '.' + new_dec_part
    elif dec_offset >= 0:
        if '.' in our_int_string:
            whole_part, dec_part = our_int_string.split('.', 1)
            if dec_offset >= len(dec_part):
                num_extra_zeros = dec_offset - len(dec_part)
                our_dec_string = f'{int(whole_part + dec_part + "0" * num_extra_zeros):,}'
            else:
                our_dec_string = f'{int(whole_part + dec_part[0:dec_offset]):,}' + '.' + dec_part[dec_offset:]
        else:
            our_dec_string = f'{int(our_int_string + "0" * dec_offset):,}'
    
    our_dec_string = our_dec_string.rstrip('.').replace(',', separator)

    return our_dec_string


def base_conv_list(original_int, base):
    # https://stackoverflow.com/questions/2267362/how-to-convert-an-integer-to-a-string-in-any-base
    if original_int == 0:
        return [0]
    digits = []
    while original_int:
        digits.append(int(original_int % base))
        original_int //= base
    return digits[::-1]

def int_base_op(num1, num2, op, base):
    base=int(base)
    num1 = str(num1)
    num2 = str(num2)
    op = str(op)
    val_as_list = base_conv_list(eval(str(int(num1, base=base)) + op + str(int(num2, base=base))), base)
    return int(''.join([str(elem) for elem in val_as_list]))


def to_egyptian(num):
    egy_python = ('\U000133FA', '\U00013386', '\U00013362', '\U000131BC', '\U000130AD', '\U00013190', '\U00013068')

    egyptian = ''

    rev_digits = str(num)[::-1]
    for ten_power, digit in enumerate(rev_digits):
        digit = int(digit)
        for i in range(0, digit):
            egyptian += egy_python[ten_power]

    return egyptian[::-1]


def to_simple_babylonian(num):
    base_60 = base_conv_list(num, 60)

    bab_python_zero = '\U000120F5'

    bab_python = ('\U00012079', '\U0001230B')

    babylonian = ''

    for index, value in enumerate(base_60):
        if index != 0:
            babylonian += '\u2003'
        if value == 0 and index != 0:
            babylonian += bab_python_zero
        else:
            current_numeral = ''
            rev_digits = str(value)[::-1]
            for ten_power, digit in enumerate(rev_digits):
                digit = int(digit)
                for i in range(0, digit):
                    current_numeral += bab_python[ten_power]
            babylonian += current_numeral[::-1]

    return babylonian


def to_roman(num):
    # https://stackoverflow.com/questions/28777219/basic-program-to-convert-integer-to-roman-numerals
    num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
               (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    roman = ''
    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i
    return roman

def samples(population, weights=None, k=1, rng=random):
    # https://maxhalford.github.io/blog/weighted-sampling-without-replacement/
    # https://stackoverflow.com/questions/26785354/normalizing-a-list-of-numbers-in-python
    if weights is None:
        weights = []
        weights += len(population) * [1]
    normed_weights = [float(i)/sum(weights) for i in weights]
    v = [rng.random() ** (1 / w) for w in normed_weights]
    order = sorted(range(len(population)), key=lambda i: v[i])
    return [population[i] for i in order[-k:]]

def constrained_weak_composition(n, k, min_elem, max_elem):
    # https://stackoverflow.com/questions/58915599/generate-restricted-weak-integer-compositions-or-partitions-of-an-integer-n-in
    allowed = range(max_elem, min_elem-1, -1)

    def helper(n, k, t):
        if k == 0:
            if n == 0:
                yield t
        elif k == 1:
            if n in allowed:
                yield t + [n]
        elif min_elem * k <= n <= max_elem * k:
            for v in allowed:
                yield from helper(n - v, k - 1, t + [v])

    full_list = list(helper(n, k, []))

    return random.choice(full_list)

def list_intersect(list_a, list_b):
    # https://stackoverflow.com/a/45313655
    set_intersection = set(list_a).intersection(set(list_b))
    list_intersection = []
    for i in set_intersection:
        num = min(list_a.count(i), list_b.count(i))
        for j in range(num):
            list_intersection.append(i)
    return sorted(list_intersection)

if __name__ == "__main__":
    main()
