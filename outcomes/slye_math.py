import random
import math
from fractions import Fraction
from typing import Any, List


def main():
    pass


class Person:
    def __init__(self, name, gender):
        self.name = str(name)
        self.gender = str(gender).lower()

    def info(self):
        return self.name, self.gender
    
    def name_cap(self):
        name = self.name
        return name.capitalize()
    
    def subj_pronoun(self):
        if self.gender == 'm':
            return 'he'
        elif self.gender == 'f':
            return 'she'
        elif self.gender == 'n':
            return 'they'
    
    def obj_pronoun(self):
        if self.gender == 'm':
            return 'him'
        elif self.gender == 'f':
            return 'her'
        elif self.gender == 'n':
            return 'them'
    
    def poss_adjective(self):
        if self.gender == 'm':
            return 'his'
        elif self.gender == 'f':
            return 'her'
        elif self.gender == 'n':
            return 'their'
    
    def poss_pronoun(self):
        if self.gender == 'm':
            return 'his'
        elif self.gender == 'f':
            return 'hers'
        elif self.gender == 'n':
            return 'theirs'
    
    def refl_pronoun(self):
        if self.gender == 'm':
            return 'himself'
        elif self.gender == 'f':
            return 'herself'
        elif self.gender == 'n':
            return 'themselves'

def sign(x):
    if Fraction(x).numerator == 0:
        return 0
    else:
        return int(Fraction(x) / abs(Fraction(x)))
    
def mixed_number(x):
    sign_x = sign(x)
    x = abs(Fraction(x))
    d = x.denominator
    i = x.numerator
    w = i // d
    n = i % d
    return sign_x * w, Fraction(n, d).numerator, Fraction(n, d).denominator 

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
                wt_5=None, wt_6=None, wt_7=None, wt_8=None, wt_9=None, custom_string=None, separator=',', remove_trails=True):
    
    dec_offset = int(dec_offset)

    if separator == None:
        separator = ''

    if custom_string == None:
        our_int_string = int_string(place_values, excl_first, excl_last, wt_0, wt_1, wt_2, wt_3, wt_4, wt_5, wt_6, wt_7, wt_8, wt_9)
    else:
        our_int_string = str(custom_string)
    
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
        if remove_trails:
            new_dec_part = new_dec_part.rstrip('0')
        new_whole_part = f'{int(whole_part[:dec_offset]):,}' if whole_part[:dec_offset] != '' else ''
        our_dec_string = new_whole_part + '.' + new_dec_part
    elif dec_offset >= 0:
        if dec_offset == 0 and remove_trails is False:
            our_dec_string = our_int_string
        elif '.' in our_int_string:
            whole_part, dec_part = our_int_string.split('.', 1)
            if dec_offset >= len(dec_part):
                num_extra_zeros = dec_offset - len(dec_part)
                our_dec_string = f'{int(whole_part + dec_part + "0" * num_extra_zeros):,}'
            else:
                our_dec_string = f'{int(whole_part + dec_part[0:dec_offset]):,}' + '.' + dec_part[dec_offset:]
        else:
            our_dec_string = f'{int(our_int_string + "0" * dec_offset):,}'
    
    if remove_trails:
        our_dec_string = our_dec_string.rstrip('.').replace(',', separator)
    else:
        our_dec_string = our_dec_string.replace(',', separator)

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

def readable_list(seq: List[Any]) -> str:
    # https://stackoverflow.com/a/53981846
    seq = [str(s) for s in seq]
    if len(seq) < 3:
        return ' and '.join(seq)
    return ', '.join(seq[:-1]) + ', and ' + seq[-1]

def rel_primes(n, stop=None):
    n = abs(int(n))
    if stop == None:
        stop = n
    if n == 0:
        return None
    rel_primes_list = []
    if n == 1 and stop == 1:
        return [1]
    for i in range(1, stop + 1):
        if math.gcd(n,i) == 1:
            rel_primes_list.append(i)
    return rel_primes_list

def divisors(n):
    n = abs(int(n))
    if n == 0:
        return None
    divisors_list = []
    if n == 1:
        return [1]
    for i in range(1, n//2 + 1):
        if n % i == 0:
            divisors_list.append(i)
    divisors_list.append(n)
    return divisors_list

def random_person(gender=None, avoid=[]):
    if gender == None:
        gender = random.choice(['m', 'f', 'n'])
    if not is_iterable(avoid):
        avoid = [avoid]
    for x in avoid:
        if isinstance(x, Person):
            x = x.name
        else:
            x = str(x)
    names_and_genders = (('Noah', 'm'), ('Liam', 'm'), ('Jacob', 'm'), ('William', 'm'), ('Mason', 'm'), ('Ethan', 'm'), ('Michael', 'm'), ('Alexander', 'm'), ('James', 'm'), ('Elijah', 'm'), ('Benjamin', 'm'), ('Daniel', 'm'), ('Aiden', 'm'), ('Logan', 'm'), ('Jayden', 'm'), ('Matthew', 'm'), ('Lucas', 'm'), ('David', 'm'), ('Jackson', 'm'), ('Joseph', 'm'), ('Anthony', 'm'), ('Samuel', 'm'), ('Joshua', 'm'), ('Gabriel', 'm'), ('Andrew', 'm'), ('John', 'm'), ('Christopher', 'm'), ('Oliver', 'm'), ('Dylan', 'm'), ('Carter', 'm'), ('Isaac', 'm'), ('Luke', 'm'), ('Henry', 'm'), ('Owen', 'm'), ('Ryan', 'm'), ('Nathan', 'm'), ('Wyatt', 'm'), ('Caleb', 'm'), ('Sebastian', 'm'), ('Jack', 'm'), ('Christian', 'm'), ('Jonathan', 'm'), ('Julian', 'm'), ('Landon', 'm'), ('Levi', 'm'), ('Isaiah', 'm'), ('Hunter', 'm'), ('Aaron', 'm'), ('Thomas', 'm'), ('Charles', 'm'), ('Eli', 'm'), ('Jaxon', 'm'), ('Connor', 'm'), ('Nicholas', 'm'), ('Jeremiah', 'm'), ('Grayson', 'm'), ('Cameron', 'm'), ('Brayden', 'm'), ('Adrian', 'm'), ('Evan', 'm'), ('Jordan', 'm'), ('Josiah', 'm'), ('Angel', 'm'), ('Robert', 'm'), ('Gavin', 'm'), ('Tyler', 'm'), ('Austin', 'm'), ('Colton', 'm'), ('Jose', 'm'), ('Dominic', 'm'), ('Brandon', 'm'), ('Ian', 'm'), ('Lincoln', 'm'), ('Hudson', 'm'), ('Kevin', 'm'), ('Zachary', 'm'), ('Adam', 'm'), ('Mateo', 'm'), ('Jason', 'm'), ('Chase', 'm'), ('Nolan', 'm'), ('Ayden', 'm'), ('Cooper', 'm'), ('Parker', 'm'), ('Xavier', 'm'), ('Asher', 'm'), ('Carson', 'm'), ('Jace', 'm'), ('Easton', 'm'), ('Justin', 'm'), ('Leo', 'm'), ('Bentley', 'm'), ('Jaxson', 'm'), ('Nathaniel', 'm'), ('Blake', 'm'), ('Elias', 'm'), ('Theodore', 'm'), ('Kayden', 'm'), ('Luis', 'm'), ('Tristan', 'm'), ('Ezra', 'm'), ('Bryson', 'm'), ('Juan', 'm'), ('Brody', 'm'), ('Vincent', 'm'), ('Micah', 'm'), ('Miles', 'm'), ('Santiago', 'm'), ('Cole', 'm'), ('Ryder', 'm'), ('Carlos', 'm'), ('Damian', 'm'), ('Leonardo', 'm'), ('Roman', 'm'), ('Max', 'm'), ('Sawyer', 'm'), ('Jesus', 'm'), ('Diego', 'm'), ('Greyson', 'm'), ('Alex', 'm'), ('Maxwell', 'm'), ('Axel', 'm'), ('Eric', 'm'), ('Wesley', 'm'), ('Declan', 'm'), ('Giovanni', 'm'), ('Ezekiel', 'm'), ('Braxton', 'm'), ('Ashton', 'm'), ('Ivan', 'm'), ('Hayden', 'm'), ('Camden', 'm'), ('Silas', 'm'), ('Bryce', 'm'), ('Weston', 'm'), ('Harrison', 'm'), ('Jameson', 'm'), ('George', 'm'), ('Antonio', 'm'), ('Timothy', 'm'), ('Kaiden', 'm'), ('Jonah', 'm'), ('Everett', 'm'), ('Miguel', 'm'), ('Steven', 'm'), ('Richard', 'm'), ('Emmett', 'm'), ('Victor', 'm'), ('Kaleb', 'm'), ('Kai', 'm'), ('Maverick', 'm'), ('Joel', 'm'), ('Bryan', 'm'), ('Maddox', 'm'), ('Kingston', 'm'), ('Aidan', 'm'), ('Patrick', 'm'), ('Edward', 'm'), ('Emmanuel', 'm'), ('Jude', 'm'), ('Preston', 'm'), ('Alejandro', 'm'), ('Luca', 'm'), ('Bennett', 'm'), ('Jesse', 'm'), ('Jaden', 'm'), ('Colin', 'm'), ('Malachi', 'm'), ('Kaden', 'm'), ('Jayce', 'm'), ('Alan', 'm'), ('Marcus', 'm'), ('Kyle', 'm'), ('Brian', 'm'), ('Ryker', 'm'), ('Grant', 'm'), ('Abel', 'm'), ('Jeremy', 'm'), ('Riley', 'n'), ('Calvin', 'm'), ('Brantley', 'm'), ('Caden', 'm'), ('Oscar', 'm'), ('Abraham', 'm'), ('Brady', 'm'), ('Sean', 'm'), ('Jake', 'm'), ('Tucker', 'm'), ('Nicolas', 'm'), ('Mark', 'm'), ('Amir', 'm'), ('Avery', 'n'), ('King', 'm'), ('Gael', 'm'), ('Kenneth', 'm'), ('Bradley', 'm'), ('Cayden', 'm'), ('Xander', 'm'), ('Graham', 'm'), ('Paul', 'm'), ('Emma', 'f'), ('Olivia', 'f'), ('Sophia', 'f'), ('Isabella', 'f'), ('Ava', 'f'), ('Mia', 'f'), ('Abigail', 'f'), ('Emily', 'f'), ('Charlotte', 'f'), ('Madison', 'f'), ('Elizabeth', 'f'), ('Amelia', 'f'), ('Evelyn', 'f'), ('Ella', 'f'), ('Chloe', 'f'), ('Harper', 'f'), ('Sofia', 'f'), ('Grace', 'f'), ('Addison', 'f'), ('Victoria', 'f'), ('Lily', 'f'), ('Natalie', 'f'), ('Aubrey', 'f'), ('Zoey', 'f'), ('Lillian', 'f'), ('Hannah', 'f'), ('Layla', 'f'), ('Brooklyn', 'f'), ('Scarlett', 'f'), ('Zoe', 'f'), ('Camila', 'f'), ('Samantha', 'f'), ('Leah', 'f'), ('Aria', 'f'), ('Savannah', 'f'), ('Audrey', 'f'), ('Anna', 'f'), ('Allison', 'f'), ('Gabriella', 'f'), ('Hailey', 'f'), ('Claire', 'f'), ('Penelope', 'f'), ('Aaliyah', 'f'), ('Sarah', 'f'), ('Nevaeh', 'f'), ('Kaylee', 'f'), ('Stella', 'f'), ('Mila', 'f'), ('Nora', 'f'), ('Ellie', 'f'), ('Bella', 'f'), ('Lucy', 'f'), ('Alexa', 'f'), ('Arianna', 'f'), ('Violet', 'f'), ('Ariana', 'f'), ('Genesis', 'f'), ('Alexis', 'f'), ('Eleanor', 'f'), ('Maya', 'f'), ('Caroline', 'f'), ('Peyton', 'f'), ('Skylar', 'f'), ('Madelyn', 'f'), ('Serenity', 'f'), ('Kennedy', 'f'), ('Taylor', 'f'), ('Alyssa', 'f'), ('Autumn', 'f'), ('Paisley', 'f'), ('Ashley', 'f'), ('Brianna', 'f'), ('Sadie', 'f'), ('Naomi', 'f'), ('Kylie', 'f'), ('Julia', 'f'), ('Sophie', 'f'), ('Mackenzie', 'f'), ('Eva', 'f'), ('Gianna', 'f'), ('Luna', 'f'), ('Katherine', 'f'), ('Hazel', 'f'), ('Khloe', 'f'), ('Ruby', 'f'), ('Piper', 'f'), ('Melanie', 'f'), ('Lydia', 'f'), ('Aubree', 'f'), ('Madeline', 'f'), ('Aurora', 'f'), ('Faith', 'f'), ('Alexandra', 'f'), ('Alice', 'f'), ('Kayla', 'f'), ('Jasmine', 'f'), ('Maria', 'f'), ('Annabelle', 'f'), ('Lauren', 'f'), ('Reagan', 'f'), ('Elena', 'f'), ('Rylee', 'f'), ('Isabelle', 'f'), ('Bailey', 'f'), ('Eliana', 'f'), ('Sydney', 'f'), ('Makayla', 'f'), ('Cora', 'f'), ('Morgan', 'f'), ('Natalia', 'f'), ('Kimberly', 'f'), ('Vivian', 'f'), ('Quinn', 'f'), ('Valentina', 'f'), ('Andrea', 'f'), ('Willow', 'f'), ('Clara', 'f'), ('London', 'f'), ('Jade', 'f'), ('Liliana', 'f'), ('Jocelyn', 'f'), ('Trinity', 'f'), ('Kinsley', 'f'), ('Brielle', 'f'), ('Mary', 'f'), ('Molly', 'f'), ('Hadley', 'f'), ('Delilah', 'f'), ('Emilia', 'f'), ('Josephine', 'f'), ('Brooke', 'f'), ('Lilly', 'f'), ('Ivy', 'f'), ('Adeline', 'f'), ('Payton', 'f'), ('Lyla', 'f'), ('Isla', 'f'), ('Jordyn', 'f'), ('Paige', 'f'), ('Isabel', 'f'), ('Mariah', 'f'), ('Mya', 'f'), ('Nicole', 'f'), ('Valeria', 'f'), ('Destiny', 'f'), ('Rachel', 'f'), ('Ximena', 'f'), ('Emery', 'f'), ('Everly', 'f'), ('Sara', 'f'), ('Angelina', 'f'), ('Adalynn', 'f'), ('Kendall', 'f'), ('Reese', 'f'), ('Aliyah', 'f'), ('Margaret', 'f'), ('Juliana', 'f'), ('Melody', 'f'), ('Amy', 'f'), ('Eden', 'f'), ('Mckenzie', 'f'), ('Laila', 'f'), ('Vanessa', 'f'), ('Ariel', 'f'), ('Gracie', 'f'), ('Valerie', 'f'), ('Adalyn', 'f'), ('Brooklynn', 'f'), ('Gabrielle', 'f'), ('Kaitlyn', 'f'), ('Athena', 'f'), ('Elise', 'f'), ('Jessica', 'f'), ('Adriana', 'f'), ('Leilani', 'f'), ('Ryleigh', 'f'), ('Daisy', 'f'), ('Nova', 'f'), ('Norah', 'f'), ('Eliza', 'f'), ('Rose', 'f'), ('Rebecca', 'f'), ('Michelle', 'f'), ('Alaina', 'f'), ('Catherine', 'f'), ('Londyn', 'f'), ('Summer', 'f'), ('Lila', 'f'), ('Jayla', 'f'), ('Katelyn', 'f'), ('Daniela', 'f'), ('Harmony', 'f'), ('Amaya', 'f'), ('Alana', 'f'), ('Emerson', 'f'), ('Julianna', 'f'), ('Cecilia', 'f'), ('Izabella', 'f'))
    name, gender = random.choice([x for x in names_and_genders if x[1] == gender and x[0] not in avoid])
    person = Person(name, gender)
    return person

if __name__ == "__main__":
    main()
