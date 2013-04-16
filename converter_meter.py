#  converter.py
#  converter_meter.py
#  python-lenght-converter
#  
#  Created by Antonin Lacombe on 2013-04-16.
#  Copyright 2013 Antonin Lacombe. All rights reserved.
# 
from converter import BaseUnitConverter

class MeterConverter(BaseUnitConverter):
    """
    The meter converter
    this is the simplest convert because we use meter as base unit 
    """
    short_unit = "m"
    convert_ratio = 1    
    def to_meter(self, value):
        return value / self.convert_ratio
        
    def from_meter(self, value):
        return value * self.convert_ratio
    

        


