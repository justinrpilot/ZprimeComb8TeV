#!/usr/bin/env python

class masspoint:
    def __init__(self, mass, exp, exp68up, exp68dn, exp95up, exp95dn, obs):
        self.mass = mass
        self.exp = exp
        self.exp68up = exp68up
        self.exp68dn = exp68dn
        self.exp95up = exp95up
        self.exp95dn = exp95dn
        self.obs = obs

def get_limits_from_file(input_file_):
    #
    # input file format:
    #
    # * each line contains the limits for 1 mass hypothesis
    #   in the following format
    #
    #   mass exp exp68up exp68dn exp95up exp95dn obs
    #
    # * each value has to separated by 1 whitespace

    mp_list = []

    f = open(input_file_,'r')
    for line in f:
        vals = line.split()
        if len(vals) != 7:
            print '\n@@@ FATAL -- uncorrect input file format. stopping script. ('+input_file_+')\n'
            raise SystemExit

        mass = float(vals[0])
        exp = float(vals[1])
        exp68up = float(vals[2])
        exp68dn = float(vals[3])
        exp95up = float(vals[4])
        exp95dn = float(vals[5])
        obs = float(vals[6])

        mp_list.append(masspoint(mass, exp, exp68up, exp68dn, exp95up, exp95dn, obs))

    return mp_list
