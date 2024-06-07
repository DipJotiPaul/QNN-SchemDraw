"""
Created on Mon Mar 14 01:58:39 2022

@author: pauld
"""
import schemdraw
import schemdraw.elements as elm
from schemdraw import dsp
from matplotlib import pyplot as plt
import math
from qnn_elements.Tron import Tron

d= schemdraw.Drawing()
d+= elm.GroundSignal()
d+= (h1 := Tron().anchor('vs').right())
d+= elm.Line().left().length(0.1).at(h1.vg)
d+= elm.SourceI().left().reverse().length(0.5).label('$I_{gate}$', fontsize = 22)
d+= elm.Line().left().length(0.5)
d+= elm.Dot(open=True)

d+= elm.Line().up().length(0.1).at(h1.vd)
d.push()
d+= elm.Line().right().length(0.5).label('V$_{ch}$', fontsize = 18, loc='left')
d+= elm.Resistor().right().length(0.5).label('100kΩ', fontsize = 18, rotate=0)
d+= elm.Line().right().length(0.5)
d+= elm.Line().down().length(0.5)
d+= elm.GroundSignal()
d.pop()
d+= elm.Line().up().length(1.5)
d+= elm.SourceI().reverse().length(0.5).label('$I_{bias}$', fontsize = 22)
d+= elm.Line().up().length(0.5)
d+= elm.Dot(open=True)

d.draw()
d.save('example_Tron_IV.svg')