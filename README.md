python-lenght-converter
=======================

a simple library convert between length units


The units to be supported are: metre (m), yard (yd) and inch (in).


usage
=======

you can use the converter with the cli:

    >>>python converter.py --help
    Usage: converter.py filename
    
    Options:
      --version             show program's version number and exit
      -h, --help            show this help message and exit
      -v VALUE, --value=VALUE
                            the value to convert woth unit ex: '2.5yd'
      -u TRG_UNIT, --unit=TRG_UNIT
                            the target unit ex: 'm'
      -t, --tidy            tidy the converted output

some exemple:
    
    >>>python converter.py -v 2.5yd -u in -t
    # 2.5 yards in meters with tidy result
    90 in
    >>>python converter.py -v 6m -u yd
    # 6 meters in yards
    6.5616798   
    >>>python converter.py -v 111.4yd -u in -t
    #11.4 yards in inches
    4010.4 in
    
