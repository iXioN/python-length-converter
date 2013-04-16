#  converter.py
#  converter_yard.py
#  python-lenght-converter
#  
#  Created by Antonin Lacombe on 2013-04-16.
#  Copyright 2013 Antonin Lacombe. All rights reserved.
# 
from converter import BaseUnitConverter

class YardConverter(BaseUnitConverter):
    """
    The yard converter
    """
    short_unit = "y"
    convert_ratio = 1.0936
    
    def to_meter(self, value):
        return value / self.convert_ratio
        
    def from_meter(self, value):
        return value * self.convert_ratio