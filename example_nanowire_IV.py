"""
Created on Mon Mar 14 01:58:39 2022

@author: pauld
"""
import schemdraw
import schemdraw.elements as elm
from schemdraw import dsp
from matplotlib import pyplot as plt
import math
from qnn_elements.Tron import Constriction

d= schemdraw.Drawing()
d+= elm.GroundSignal()
d+= (h1 := Constriction().anchor('vs').right())

d+= elm.Line().up().length(0.001).at(h1.vd)
d+= elm.Line().up().length(0.25).label('V$_{ch}$', fontsize = 22, loc='right',ofst = (-0.25,0.75))
d.push()
d+= elm.Line().up().length(1)
d+= elm.Resistor().up().length(0.5).label('1kΩ', fontsize = 18, rotate=0)
d+= elm.Line().up().length(1)
d+= elm.Dot(open=True)
d+= elm.Line().label('V$_{bias}$', fontsize = 18, loc='right',ofst = (0.2,0)).length(0.01)

d.pop()
d+= elm.Dot(open=True)
d+= elm.Line().right().length(0.7)
d+= elm.Resistor().right().length(0.5).label('1MΩ', fontsize = 18, rotate=0)
d+= elm.Line().right().length(0.5)
d+= elm.Line().down().length(0.5)
d+= elm.GroundSignal()

d.draw()
d.save('example_nanowire_IV.svg')