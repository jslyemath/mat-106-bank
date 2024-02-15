import sys
sys.path.append('/home/slye/mat-106-bank/outcomes/')
import slye_math as sm


class Generator(BaseGenerator):

    def data(self):
        def bab_modern():
            modern = choice(range(3501, 162000))
            bab = sm.to_simple_babylonian(modern)
            return bab, modern, 'ancient Babylonian'

        def rom_modern():
            modern = int(sm.int_creator(4, (0, 4, 5, 6, 7, 8, 9), wt_0=.03, wt_4=.2, wt_6=.2, wt_9=.2))
            rom = sm.to_roman(modern)
            return rom, modern, 'Roman'

        def egy_modern():
            modern = choice(range(100000, 4000000))
            egy = sm.to_egyptian(modern)
            return egy, modern, 'ancient Egyptian'

        other_system = choice([rom_modern, egy_modern])
        chosen_systems = [bab_modern, other_system]
        shuffle(chosen_systems)
        to_ancient_func, to_modern_func = chosen_systems

        to_a_ancient, to_a_modern, to_a_system = to_ancient_func()
        to_m_ancient, to_m_modern, to_m_system = to_modern_func()

        return {
            'to_a_modern': f'{int(to_a_modern):,}',
            'to_a_system': f'{to_a_system}',
            'to_a_ancient': f'{to_a_ancient}',
            'to_m_ancient': f'{to_m_ancient}',
            'to_m_system': f'{to_m_system}',
            'to_m_modern': f'{int(to_m_modern):,}',
            'test': '𓁨𓁨𓁨𓆐𓂭𓂭𓂭𓂭𓆼𓆼𓆼𓆼𓆼𓎆𓎆𓎆𓎆𓏺𓏺𓏺𓏺𓏺'
        }
