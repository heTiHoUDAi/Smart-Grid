# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 22:36:45 2018

@author: Zisheng Wang
The Error happen in the gas network
"""

class EdgeStartEndSameError(Exception):
    def __init__(self,edge):
        print('Gas Simulation Error in '+self.__str__()+' \
              The edge start and end should not be the same')
        


