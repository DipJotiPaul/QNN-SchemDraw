"""
Created on Wed Jul 13 01:58:39 2022

@author: johng
"""
import math
import schemdraw
from schemdraw.elements.elements import Element, gap
import schemdraw.elements as elm
from schemdraw.segments import Segment
from schemdraw.segments import SegmentCircle

length = 2.5
width = 0.5

class yTron(Element):
    def __init__(self, *d, **kwargs):
        super().__init__(*d, **kwargs)

        self.segments.append(SegmentCircle((0, 0.4), 0.2))

        self.segments.append(Segment([

            # Constriction
            (0.2, 0.2),
            (0.2, length / 2),
            (width, length / 4),
            (width, length),
            gap,
            (0.2, 0.2),
            (0.2, -length / 2),
            (width, -length / 4),
            (width, -length),
            gap,

            # Y arm left
            (-0.2, 0.5),
            (-2*width, length/1.5),
            (-2*width, length)

        ]))

        # Anchors
        self.anchors['nanowire_bottom'] = (width, -length)
        self.anchors['nanowire_top'] = (width, length)
        self.anchors['y_arm'] = (-2*width, length)