# any output from cProfile can be read liek this...
import pstats

def main():
    '''access and reveal the cProfile report'''
    p = pstats.Stats('profile_output')
    p.print_stats()

if __name__ == '__main__':
    main()