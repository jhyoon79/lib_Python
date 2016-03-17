#!/usr/bin/env python

import pylab as pl

def one2one(x,y,log=False,**kwargs):
	pl.plot([x,y],[x,y],**kwargs)

