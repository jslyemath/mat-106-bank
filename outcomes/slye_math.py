import random
import sys
from PIL import Image


def main():
    pass


def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False
    

def stich_images():
    # https://stackoverflow.com/questions/30227466/combine-several-images-horizontally-with-python
    images = [Image.open(x) for x in ['Test1.jpg', 'Test2.jpg', 'Test3.jpg']]
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
    new_im.paste(im, (x_offset,0))
    x_offset += im.size[0]

    new_im.save('test.jpg')


def int_creator(place_values=1, excl_first=None, excl_last=None, wt_0=0.0, wt_1=0.0, wt_2=0.0, wt_3=0.0, wt_4=0.0,
                wt_5=0.0, wt_6=0.0, wt_7=0.0, wt_8=0.0, wt_9=0.0):
    the_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    wt_list = [wt_0, wt_1, wt_2, wt_3, wt_4, wt_5, wt_6, wt_7, wt_8, wt_9]
    wt_rem = 1 - sum(wt_list)
    if wt_rem == 1:
        for i in range(len(wt_list)):
            wt_list[i] = 0.1
    else:
        non_wtd = sum(1 for wt in wt_list if wt == 0)
        wt_rem_split = wt_rem / non_wtd

        for i in range(len(wt_list)):
            if wt_list[i] == 0:
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
    middle_digits = random.choices(the_digits, weights=ld_wt_list, k=place_values - 2)
    if place_values == 1:
        last_digit = []
    else:
        last_digit = random.choices(last_digits, weights=wt_list, k=1)
    all_digits = first_digit + middle_digits + last_digit
    all_digits_strings = [str(digit) for digit in all_digits]

    our_int = ''.join(all_digits_strings)

    return our_int


def base_conv_list(original_int, base):
    # https://stackoverflow.com/questions/2267362/how-to-convert-an-integer-to-a-string-in-any-base
    if original_int == 0:
        return [0]
    digits = []
    while original_int:
        digits.append(int(original_int % base))
        original_int //= base
    return digits[::-1]


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

    bab_python_zero = 'zero'

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


if __name__ == "__main__":
    main()
