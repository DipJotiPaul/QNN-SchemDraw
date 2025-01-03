"""
Created on Wed Jul 13 01:58:39 2022

@author: johng
"""

import math
import schemdraw
from schemdraw.elements.elements import Element, gap
import schemdraw.elements as elm
from schemdraw.segments import Segment

class hTron(Element):
    def __init__(self, *d, **kwargs):
        super().__init__(*d, **kwargs)

        hwidth = 2
        hheight = 2

        self.segments.append(Segment([

            # Normal Heater
            (0, 0),
            (0, 0.5 * hheight),
            (0.25 * hwidth, 0.5 * hheight),
            (0.25 * hwidth, 0.75 * hheight),
            (0, 0.75 * hheight),
            (0, 1 * hheight),
            (0.25 * hwidth, 1 * hheight),
            (0.25 * hwidth, 1.25 * hheight),
            (0, 1.25 * hheight),
            (0, 1.75 * hheight),
            gap,

            # Nanowire
            (0.75 * hwidth, 0),
            (0.75 * hwidth, 0.625 * hheight),
            (0.4 * hwidth, 0.375 * hheight),
            (0.4 * hwidth, 1.375 * hheight),
            (0.75 * hwidth, 1.125 * hheight),
            (0.75 * hwidth, 1.75 * hheight)

        ]))

        # Anchors
        self.anchors['ndown'] = (0.75 * hwidth, 0)
        self.anchors['nup'] = (0.75 * hwidth, 1.75 * hheight)
        self.anchors['hdown'] = (0, 0)
        self.anchors['hup'] = (0, 1.75 * hheight)