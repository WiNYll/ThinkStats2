"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import first
import thinkstats2
import thinkplot

def PmfMean(pmf):
    mean=0.0
    
    for x,p in pmf.Items():
        mean+=p*x
    return mean

def PmfVar(pmf):
    var=0.0
    
    for x,p in pmf.Items():
        var+=p*(x-pmf.Mean())**2
    return var
    
def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    
    prglngth = live.prglngth
    pmf = thinkstats2.Pmf(prglngth)
    mean = PmfMean(pmf)
    var = PmfVar(pmf)
    
    assert(mean == pmf.Mean())
    print('PmfMean()/pmf.Mean() preg length', mean, pmf.Mean())

    assert(var == pmf.Var())
    print('PmfVar()/pmf.Var() preg length', var, pmf.Var())

    print('%s: All tests passed.' % script)
    
if __name__ == '__main__':
    main(*sys.argv)
