"""
Created on Mon Mar 14 01:58:39 2022

@author: pauld
"""
import math
import schemdraw
from schemdraw.elements.elements import Element, gap
import schemdraw.elements as elm
from schemdraw.segments import Segment


length = 2.5
width = 0.5
gate = 3*length/16
arrow_x = width/2
arrow_y = arrow_x/math.tan(math.pi/4)

class Tron(Element):
    ''' nTron.
        Args:
            sign: Draw +/- labels at each input
        Anchors: 
            * vd
            * vs
            * vg
            testing
    '''
    def __init__(self, *d, sign: bool=True, **kwargs):
        super().__init__(*d, **kwargs)
        self.segments.append(Segment(
            [(0, 0), (0, length/2), (width, length/4), (width, length),
              gap, (0, 0), (0, -length/2), (width, -length/4), (width, -length),
              gap, (0, -gate), (-length/2, -gate),
              gap, (0, -gate), (-arrow_x, -gate + arrow_y),
              gap, (0, -gate), (-arrow_x, -gate - arrow_y)]))

        # if sign:
        #     self.segments.append(Segment(
        #         [(oa_lblx-oa_pluslen/2, oa_back/4),
        #           (oa_lblx+oa_pluslen/2, oa_back/4)]))
        #     self.segments.append(Segment(
        #         [(oa_lblx-oa_pluslen/2, -oa_back/4),
        #           (oa_lblx+oa_pluslen/2, -oa_back/4)]))
        #     self.segments.append(Segment(
        #         [(oa_lblx, -oa_back/4-oa_pluslen/2),
        #           (oa_lblx, -oa_back/4+oa_pluslen/2)]))

        self.anchors['vd'] = (width, length)
        self.anchors['vs'] = (width, -length)
        self.anchors['vg'] = (-length/2, -gate)
        # self.anchors['out'] = (oa_xlen, 0)
        # self.anchors['vd'] = (oa_xlen/3, .84)
        # self.anchors['vs'] = (oa_xlen/3, -.84)
        # self.anchors['n1'] = (oa_xlen*2/3, -.42)
        # self.anchors['n2'] = (oa_xlen*2/3, .42)
        # self.anchors['n1a'] = (oa_xlen*.9, -.13)
        # self.anchors['n2a'] = (oa_xlen*.9, .13)
        # self.params['drop'] = (oa_xlen, 0)