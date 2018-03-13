# -*- coding: utf-8 -*-
"""
Zisheng Wang

The gas network simulation code.

This gas flow and pressure is based on the paper 
'Solving the Natural Gas Flow Problem using Semidefinite Program Relaxation' 2017
by A. Ojha, V. Kekatos and R. Baldick.
"""

import gas_errors

class GasNetworkEdge:
    # @in start, an int indicate the start of the edge
    # @in end, an int indicate the end of the edge
    # @in gas_constant, a constant related to the length, diameter, impedence of the 
    #       pipeline. The definition of it may refer to the 'Simulation and Analysis
    #       of the Gas Network' page 78, equation 4.28
    def __init__(self,start,end,gas_constant):
        if start==end:
            raise(gas_errors.EdgeStartEndSameError(self))
        self.start = start
        self.end   = end
        self.K     = gas_constant
    # return the copy of current class
    def copy(self):
        import copy
        return copy.deepcopy(self)
class GasNetworkCompressor:
    # @in edge: Class GasNetworkEdge, indicate which pipeline the compressor belongs to.
    # @in alpha: the compressor ratio. linear multiple the square of the pressure
    # @in r: the location ratio, represent where is the Compressor
    def __init__(self, edge, alpha, r):
        self.edge  = edge.copy()
        self.alpha = alpha
        self.r     = r    

class GetNetworkNode:
    # @in number: the number or label of the gas network node
    # @in damend: the gas damend of this node, positive for comuser, nagetive for
    #               supplier.
    def __init__(self, number, demand):
        self.number = number
        self.demand = demand

class GasNetworkModel:
    # @in nodes: the list of node flows,
    # @in edges: the list of the edges, the element is a edge class.
    # @in cps: the list of the compressor, the element is the compressor class
    # @in name: the name of the gas network model
    def __init__(self, nodes, edges, cps, name):
        self.nodes = nodes.copy()
        self.edges = edges.copy()
        self.compressor = cps.copy()
    # @in filename, a local file that we can read the network into the ram
    # we don't check whether this file is actually exist. We let the program 
    # crash.
    # The input file of the Gas Network is as follow,
    # Gas Network Description
    # [node]
    # Number[comma]Demand[\r\n] -- int,float
    # [edge]
    # Number[comma]Start[comma]End[comma]GasConstant[\r\n] -- int,int,int,float
    # [compressor]
    # Number[comma]EdgeNumber[comma]Alpha[comma]R[\r\n] -- int,int,float,float.
    # End of Gas Network Description
    # !!! - I don't check whether the number in the file is illegal.
    def __init__(self, filename):
        self.edges = []
        self.nodes = []
        self.compressor = []
        import csv
        file = open(filename,'r')
        
        
        
def Gas_Network_Simulation():
    print('Hellow')
    
a = GasNetworkEdge(1,1,0.1)