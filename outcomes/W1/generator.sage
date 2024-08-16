import sys
sys.path.append('/home/slye/mat-106-bank/outcomes/')
import slye_math as sm
import random


class Generator(BaseGenerator):

    def data(self):
        def bab_modern():
            modern = random.choice(range(3501, 162000))
            bab = sm.to_simple_babylonian(modern)
            return f'\\Large {bab}', modern, 'ancient Babylonian'

        def rom_modern():
            modern = int(sm.int_string(4, (0, 4, 5, 6, 7, 8, 9), wt_0=.03, wt_4=.2, wt_6=.2, wt_9=.2))
            rom = sm.to_roman(modern)
            return f'\\text{{{rom}}}', modern, 'Roman'

        def egy_modern():
            modern = random.choice(range(100000, 4000000))
            egy = sm.to_egyptian(modern)
            return f'\\Huge {egy}', modern, 'ancient Egyptian'

        other_system = random.choice([rom_modern, egy_modern])
        chosen_systems = [bab_modern, other_system]
        shuffle(chosen_systems)
        to_ancient_func, to_modern_func = chosen_systems

        egy_test = False
        if other_system == egy_modern:
            egy_test = True

        to_a_ancient, to_a_modern, to_a_system = to_ancient_func()
        to_m_ancient, to_m_modern, to_m_system = to_modern_func()

        return {
            'to_a_modern': f'{int(to_a_modern):,}',
            'to_a_system': f'{to_a_system}',
            'to_a_ancient': f'{to_a_ancient}',
            'to_m_ancient': f'{to_m_ancient}',
            'to_m_system': f'{to_m_system}',
            'to_m_modern': f'{int(to_m_modern):,}',
            'egy_test': egy_test
        }
