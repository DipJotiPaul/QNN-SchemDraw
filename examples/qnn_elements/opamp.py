''' Operation amplifier '''

import math

from schemdraw.elements.elements import Element, gap
import schemdraw.elements as elm
from schemdraw.segments import Segment


oa_back = 2.5
oa_xlen = oa_back * math.sqrt(3)/2
oa_lblx = oa_xlen/8
oa_pluslen = .2


class Opamp(Element):
    ''' Operational Amplifier.

        Args:
            sign: Draw +/- labels at each input

        Anchors: 
            * in1
            * in2
            * out
            * vd
            * vs
            * n1
            * n2
            * n1a
            * n2a
            testing
    '''
    def __init__(self, *d, sign: bool=True, **kwargs):
        super().__init__(*d, **kwargs)
        self.segments.append(Segment(
            [(0, 0), (0, oa_back/2), (oa_xlen, 0), (0, -oa_back/2), (0, 0),
             gap, (oa_xlen, 0)]))

        if sign:
            self.segments.append(Segment(
                [(oa_lblx-oa_pluslen/2, oa_back/4),
                 (oa_lblx+oa_pluslen/2, oa_back/4)]))
            self.segments.append(Segment(
                [(oa_lblx-oa_pluslen/2, -oa_back/4),
                 (oa_lblx+oa_pluslen/2, -oa_back/4)]))
            self.segments.append(Segment(
                [(oa_lblx, -oa_back/4-oa_pluslen/2),
                 (oa_lblx, -oa_back/4+oa_pluslen/2)]))

        self.anchors['center'] = (oa_xlen/2, 0)
        self.anchors['in1'] = (0, oa_back/4)
        self.anchors['in2'] = (0, -oa_back/4)
        self.anchors['out'] = (oa_xlen, 0)
        self.anchors['vd'] = (oa_xlen/3, .84)
        self.anchors['vs'] = (oa_xlen/3, -.84)
        self.anchors['n1'] = (oa_xlen*2/3, -.42)
        self.anchors['n2'] = (oa_xlen*2/3, .42)
        self.anchors['n1a'] = (oa_xlen*.9, -.13)
        self.anchors['n2a'] = (oa_xlen*.9, .13)
        self.params['drop'] = (oa_xlen, 0)




class RFamp(Element):
    ''' Operational Amplifier.

        Args:
            sign: Draw +/- labels at each input

        Anchors:
            * in1
            * in2
            
            
            * out
            * vd
            * vs
            * n1
            * n2
            * n1a
            * n2a
    '''
    
    def __init__(self, *d, sign: bool=True, resistor: bool = True, **kwargs):
        super().__init__(*d, **kwargs)
        oa_back = 3
        oa_xlen = oa_back * math.sqrt(3)/2
        oa_lblx = oa_xlen/8
        oa_pluslen = .2
        resheight = 0.09     # Resistor height
        reswidth = 0.5 / 6   # Full (inner) length of resistor is 1.0 data unit
        gndgap = 0.12
        gnd_lead = 0.4
        resheight1 = 0.2 #kate

        if resistor:
            self.segments.append(Segment(
            [(0, 0), (0, oa_back/2), (oa_xlen, 0), (0, -oa_back/2), (0, 0), gap, (oa_xlen, 0)]))
            
            self.segments.append(Segment(
            [(-oa_xlen/6, oa_back/8),
             (oa_xlen/6, oa_back/8), (oa_xlen/6, oa_back/12)]))
            
            self.segments.append(Segment(
            [(oa_xlen/6, oa_back/8), (oa_xlen/6, oa_back/12),
            (oa_xlen/6+resheight, oa_back/12-0.5*reswidth), 
            (oa_xlen/6-resheight, oa_back/12-1.5*reswidth),
            (oa_xlen/6+resheight, oa_back/12-2.5*reswidth),
            (oa_xlen/6-resheight, oa_back/12-3.5*reswidth),
            (oa_xlen/6+resheight, oa_back/12-4.5*reswidth),
            (oa_xlen/6-resheight, oa_back/12-5.5*reswidth), 
            (oa_xlen/6, oa_back/12-6*reswidth)
            ]))
            
            self.segments.append(Segment(
            [(-oa_xlen/6, -oa_back/8), 
            (oa_xlen/6, -oa_back/8),
            (oa_xlen/6, -oa_back/12)]))
            
            # self.segments.append(Segment(
            # [(-oa_xlen/6, -oa_back/8), (-oa_xlen/6, -oa_back/4), (-oa_xlen/6, -oa_back/4-gnd_lead), 
            #   (-oa_xlen/6-resheight1, -oa_back/4-gnd_lead), (-oa_xlen/6, -oa_back/4-gnd_lead*2),
            # (-oa_xlen/6+resheight1, -oa_back/4-gnd_lead), (-oa_xlen/6, -oa_back/4-gnd_lead)]))
            
            self.segments.append(Segment(
            [(-oa_xlen/6, -oa_back/8), (-oa_xlen/6, -oa_back/4), (-oa_xlen/6, -oa_back/4-gnd_lead)]))
            
            ground_sym=[(0, 0), (0, -gnd_lead), (-resheight1, -gnd_lead), (0, -gnd_lead*2),
              (resheight1, -gnd_lead), (0, -gnd_lead)]
            for i in range(len(ground_sym)):
                coord=[ground_sym[i], (-oa_xlen/6, -oa_back/4-gnd_lead)]
                res = [sum(i) for i in zip(*coord)]
                ground_sym[i]=res
            # ground_sym.append((-oa_xlen/6, -oa_back/4-gnd_lead))
            self.segments.append(Segment(ground_sym))
            
            
            # self.segments.append(Segment(
            # [(0, 0), (0, -gnd_lead), (-resheight, -gnd_lead), (0, -gnd_lead*2),
            #  (resheight, -gnd_lead), (0, -gnd_lead)]))
            # self.segments.append(elm.GroundSignal())
        
        if sign: 
          self.segments.append(Segment(
            [(0, 0), (0, oa_back/2), (oa_xlen, 0), (0, -oa_back/2), (0, 0),
             gap, (oa_xlen, 0)]))
          self.segments.append(Segment(
                [(oa_lblx-oa_pluslen/2, oa_back/4),
                 (oa_lblx+oa_pluslen/2, oa_back/4)]))
          self.segments.append(Segment(
                [(oa_lblx-oa_pluslen/2, -oa_back/4),
                  (oa_lblx+oa_pluslen/2, -oa_back/4)]))
          self.segments.append(Segment(
                [(oa_lblx, -oa_back/4-oa_pluslen/2),
                  (oa_lblx, -oa_back/4+oa_pluslen/2)])) 
          
        self.anchors['center'] = (oa_xlen/2, 0)
        self.anchors['in1'] = (0, oa_back/8)
        self.anchors['in2'] = (0, -oa_back/4)
        self.anchors['out'] = (oa_xlen, 0)
        self.anchors['vd'] = (oa_xlen/3, .84)
        self.anchors['vs'] = (oa_xlen/3, -.84)
        self.anchors['n1'] = (oa_xlen*2/3, -.42)
        self.anchors['n2'] = (oa_xlen*2/3, .42)
        self.anchors['n1a'] = (oa_xlen*.9, -.13)
        self.anchors['n2a'] = (oa_xlen*.9, .13)
        self.params['drop'] = (oa_xlen, 0)