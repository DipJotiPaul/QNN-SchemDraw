"""
Created on Wed Jul 13 01:58:39 2022

@author: pauld
"""

import math
import schemdraw
from schemdraw.elements.elements import Element, gap
import schemdraw.elements as elm
from schemdraw.segments import Segment
from schemdraw.segments import SegmentArc
from schemdraw.util import linspace

length = 1.5
width = 0.5
resheight = 0.25

fuser = .12
fusey = [math.sin(x) * resheight for x in linspace(0, 2 * math.pi)]
fusex = linspace(-width * 2, -width)
fusex2 = linspace(-width * 3, -width * 2)
fusex3 = linspace(-width * 4, -width * 3)


class SNSPD(Element):
    def __init__(self, *d, **kwargs):
        super().__init__(*d, **kwargs)
        self.segments.append(Segment(
            [(0, 0), (0, length/2), (width, length/4), (width, length),
              gap, (0, 0), (0, -length/2), (width, -length/4), (width, -length)]))

        # photon tail
        self.segments.append(Segment(list(zip(fusex, fusey))))
        self.segments.append(Segment(list(zip(fusex2, fusey))))
        # self.segments.append(Segment(list(zip(fusex3, fusey))))

        # photon arrow
        self.segments.append(Segment([(-width, 0), (-0.125, 0)], arrow='->', arrowwidth=resheight))

        # label
        self.label('\u210e\u03BD', loc='photon_label', fontsize = 20)

        # Anchors
        self.anchors['photon_label'] = (-width * 2.5, resheight * 1.5)
        self.anchors['vd'] = (width, length)
        self.anchors['vs'] = (width, -length)
