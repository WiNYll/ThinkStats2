"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys
from operator import itemgetter

import first
import thinkstats2


def Mode(hist):
    """Returns the value with the highest frequency.

    hist: Hist object

    returns: value from Hist
    """
    parityfreq = [(freq, val) for val, freq in hist.Items()]
    freqmode, mode = max(parityfreq)
    
    return mode

def AllModes(hist):
    """Returns value-freq pairs in decreasing order of frequency.

    hist: Hist object

    returns: iterator of value-freq pairs
    """
    
    return sorted(hist.Items(), key=itemgetter(1), reverse=True)

def CompareWeight(live, firsts, others):
    
    meanlive = live.totalwgt_lb.mean()
    meanfirsts = firsts.totalwgt_lb.mean()
    meanothers = others.totalwgt_lb.mean()
    
    print('Mean')
    print('Firsts', meanfirsts)
    print('Others', meanothers)
    
    print('Difference in lbs', meanfirsts-meanothers)
    print('Difference in %', (meanfirsts-meanothers) / meanlive * 100)

    varfirsts = firsts.totalwgt_lb.var()
    varothers = others.totalwgt_lb.var()
    
    print('Variance')
    print('Firsts', varfirsts)
    print('Others', varothers)
    
    d = thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
    print('Cohen effect', d)
    
def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    
    live, firsts, others = first.MakeFrames()
    hist = thinkstats2.Hist(live.prglngth)

    # test Mode    
    mode = Mode(hist)
    print('Mode of preg length', mode)
    assert mode == 39, mode

    # test AllModes
    modes = AllModes(hist)
    assert modes[0][1] == 4693, modes[0][1]

    for value, freq in modes[:5]:
        print(value, freq)
       
    CompareWeight(live, firsts, others)
    
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
