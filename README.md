python-length-converter
=======================
the goal is to implement a simple library that converts lengths in different units. For example:
    6m to yard = 6.562yd 
    2.5yd to inch = 90in

The units to be supported are: metre (m), yard (yd) and inch (in). You can easily add new units

It also support representing the measures as user­friendly strings (e.g., "2.3 m", "6 yd", "0.4 in").

Usage as library
=================
here is an exemple of how to use the converter as library
    
    >>> import converter 
    #create a converter instance
    >>> converter_instance = Converter()
    
    #the easier way to convert is to use the convert method
    >>> converter_instance.convert('6m', 'yd', as_string=True)
    6.6 yd
    
    #you can also use the low level api
    >>> converter_instance.set_value('3.45', 'yd')
    >>> converter_instance.convert_to_unit('m')
    3.15468

Run the unit tests
====================
to run the tests cases:
    
    $ python test_cases.py
    ..............
    ----------------------------------------------------------------------
    Ran 14 tests in 0.001s
    OK

Command Line Interface
========================
you can use the converter with the cli:

    $ python converter.py --help
    Usage: converter.py filename
    
    Options:
      --version             show program's version number and exit
      -h, --help            show this help message and exit
      -v VALUE, --value=VALUE
                            the value to convert woth unit ex: '2.5yd'
      -u TRG_UNIT, --unit=TRG_UNIT
                            the target unit ex: 'm'
      -t, --tidy            print the result user friendly (rounded and with unit)

some exemple:
    
    #2.5 yards in meters with tidy result
    $ python converter.py -v 2.5yd -u in -t
    90.1 in
    
    #6 meters in yards
    $ python converter.py -v 6m -u yd
    6.561678 
    
    #11.4 yards in inches 
    $ python converter.py -v 111.4yd -u in -t
    4010.5 in
    
