#! /usr/bin/python3.6

from pycatia.csv_tools import convert_units, unit_conversion


def test_units():
    input_unit = 5

    assert input_unit == (input_unit * unit_conversion['mm'])
    assert 50 == (input_unit * unit_conversion['cm'])
    assert 5000 == (input_unit * unit_conversion['m'])
    assert 5e+6 == (input_unit * unit_conversion['km'])
    assert 127 == (input_unit * unit_conversion['in'])
    assert 8046720 == (input_unit * unit_conversion['mile'])

# todo: add test for convert_units function.
