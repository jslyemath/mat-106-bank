import sys
sys.path.append('/home/slye/mat-106-bank/outcomes/')
import slye_math as sm
import random

# For local testing purposes

def main():
    base_ten_num1 = ''
    base_ten_num2 = ''
    base_b_num1 = ''
    base_b_num2 = ''
    base_ten_alg = 'Standard'
    base_b_alg = 'Standard'
    add_algs = ('Column Addition', 'Partial Sums', 'Lattice')
    sub_algs = ('Equal Additions', 'Trades First', 'Subtract from the Base')
    base_b_base = random.choice((4, 5, 6, 7, 8, 9))
    base_names = ['null', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    base_b_ss = base_names[base_b_base]
    base_ten_op = random.choice(('+', '-'))
    base_b_op = ''
    xmore_likely = 4
    sub_match_counter = 0
    bt_n1_wts = {'wt_0':0.0, 'wt_1':0.0, 'wt_2':0.0, 'wt_3':0.0, 'wt_4':0.0, 
                    'wt_5':0.0, 'wt_6':0.0, 'wt_7':0.0, 'wt_8':0.0, 'wt_9':0.0}
    bt_n2_wts = {'wt_0':0.0, 'wt_1':0.0, 'wt_2':0.0, 'wt_3':0.0, 'wt_4':0.0, 
                    'wt_5':0.0, 'wt_6':0.0, 'wt_7':0.0, 'wt_8':0.0, 'wt_9':0.0}
    bb_n1_wts = {'wt_0':0.0, 'wt_1':0.0, 'wt_2':0.0, 'wt_3':0.0, 'wt_4':0.0, 
                    'wt_5':0.0, 'wt_6':0.0, 'wt_7':0.0, 'wt_8':0.0, 'wt_9':0.0}
    bb_n2_wts = {'wt_0':0.0, 'wt_1':0.0, 'wt_2':0.0, 'wt_3':0.0, 'wt_4':0.0, 
                    'wt_5':0.0, 'wt_6':0.0, 'wt_7':0.0, 'wt_8':0.0, 'wt_9':0.0}

    if base_ten_op == '+':
        base_b_op = '-'

        for i, wt in enumerate(bt_n1_wts):
            if i < 5:
                bt_n1_wts[wt] = 1 / (10 * (xmore_likely+1))
            if 5 <= i < 10:
                bt_n1_wts[wt] = xmore_likely / (10 * (xmore_likely+1))

        for i, wt in enumerate(bt_n2_wts):
            if i < 5:
                bt_n2_wts[wt] = 1 / (10 * (xmore_likely+1))
            if 5 <= i < 10:
                bt_n2_wts[wt] = xmore_likely / (10 * (xmore_likely+1))

        base_ten_num1 = sm.int_string(place_values=4, **bt_n1_wts)
        base_ten_num2 = sm.int_string(place_values=4, **bt_n2_wts)
        base_ten_alg = random.choice(add_algs)

        for i, wt in enumerate(bb_n1_wts):
            if i < base_b_base/2:
                bb_n1_wts[wt] = xmore_likely / (base_b_base * (xmore_likely+1))
            if base_b_base/2 <= i < base_b_base:
                bb_n1_wts[wt] = 1 / (base_b_base * (xmore_likely+1))

        for i, wt in enumerate(bb_n2_wts):
            if i < base_b_base/2:
                bb_n2_wts[wt] = 1 / (base_b_base * (xmore_likely+1))
            if base_b_base/2 <= i < base_b_base:
                bb_n2_wts[wt] = xmore_likely / (base_b_base * (xmore_likely+1))
                
        base_b_num1 = sm.int_string(place_values=4, **bb_n1_wts)

        for place, numeral in enumerate(base_b_num1):
            if sub_match_counter == place:
                excl_list = list(range(int(base_b_num1[place]) + 1, 10))
            else:
                excl_list = []

            base_b_num2 += sm.int_string(place_values=1,
                                         excl_first=excl_list,
                                         **bb_n2_wts)
            if int(numeral) == int(base_b_num2[place]):
                sub_match_counter += 1

        base_b_num2 = base_b_num2.lstrip('0')

        # while True:
        #     base_b_num2 = sm.int_string(place_values=4,
        #                                 excl_first=excl_list,
        #                                 **bb_n2_wts)
            
        #     print(base_b_num2)
            
        #     if int(base_b_num1) > int(base_b_num2):
        #         break

        base_b_alg = random.choice(sub_algs)

    else:
        base_b_op = '+'

        for i, wt in enumerate(bt_n1_wts):
            if i < 5:
                bt_n1_wts[wt] = 1 / (10 * (xmore_likely+1))
            if 5 <= i < 10:
                bt_n1_wts[wt] = xmore_likely / (10 * (xmore_likely+1))

        for i, wt in enumerate(bt_n2_wts):
            if i < 5:
                bt_n2_wts[wt] = 1 / (10 * (xmore_likely+1))
            if 5 <= i < 10:
                bt_n2_wts[wt] = xmore_likely / (10 * (xmore_likely+1))

        base_ten_num1 = sm.int_string(place_values=4, **bt_n1_wts)
        
        # excl_list = list(range(int(base_ten_num1[0]) + 1, 9))
        # excl_list.append(0)

        # while True:
        #     base_ten_num2 = sm.int_string(place_values=4,
        #                                 excl_first=excl_list,
        #                                 **bt_n2_wts)
            
        #     print(base_ten_num2)
            
        #     if int(base_ten_num1) > int(base_ten_num2):
        #         break

        for place, numeral in enumerate(base_ten_num1):
            if sub_match_counter == place:
                excl_list = list(range(int(base_ten_num1[place]) + 1, 10))
            else:
                excl_list = []

            base_ten_num2 += sm.int_string(place_values=1,
                                           excl_first=excl_list,
                                           **bt_n2_wts)
            if int(numeral) == int(base_ten_num2[place]):
                sub_match_counter += 1

        base_ten_num2 = base_ten_num2.lstrip('0')
        
        base_ten_alg = random.choice(sub_algs)

        for i, wt in enumerate(bb_n1_wts):
            if i < base_b_base/2:
                bb_n1_wts[wt] = xmore_likely / (base_b_base * (xmore_likely+1))
            if base_b_base/2 <= i < base_b_base:
                bb_n1_wts[wt] = 1 / (base_b_base * (xmore_likely+1))

        for i, wt in enumerate(bb_n2_wts):
            if i < base_b_base/2:
                bb_n2_wts[wt] = 1 / (base_b_base * (xmore_likely+1))
            if base_b_base/2 <= i < base_b_base:
                bb_n2_wts[wt] = xmore_likely / (base_b_base * (xmore_likely+1))
                
        base_b_num1 = sm.int_string(place_values=4, **bb_n1_wts)
        base_b_num2 = sm.int_string(place_values=4, **bb_n2_wts)
        base_b_alg = random.choice(add_algs)

    base_ten_prob = f'{base_ten_num1} {base_ten_op} {base_ten_num2}'
    base_ten_ans = f'{eval(base_ten_num1 + base_ten_op + base_ten_num2)}'

    base_b_prob = f'{base_b_num1}_\\text{{{base_b_ss}}} {base_b_op} {base_b_num2}_\\text{{{base_b_ss}}}'
    base_b_ans = f'{sm.int_base_op(base_b_num1, base_b_num2, base_b_op, base_b_base)}_\\text{{{base_b_ss}}}'

    return {
        'base_ten_prob': base_ten_prob,
        'base_ten_alg': base_ten_alg,
        'base_ten_ans': base_ten_ans,
        'base_b_prob': base_b_prob,
        'base_b_alg': base_b_alg,
        'base_b_ans': base_b_ans
    }

if __name__ == "__main__":
    main()