# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 08:26:57 2019

@author: Karsyn
"""

from gurobi.py import*
mod = model("soldiers")
x1 = mod.addvar