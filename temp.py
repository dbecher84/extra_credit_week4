#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Converts temperatures from one scale to another"""

def temp_convert(temp_c=0, temp_k=0):
    """Converts Kelvin to Celsius and Fahrenheit and Celsius to Fahrenheit.

    Args:
        temp_c (int): temperature in Celsius to convert to Fahrenheit. Default=0.
        temp_k (int): temperature in Kelvin to convert to Fahrenheit and Celsius.
                      Default=0.

    Returns:
        str: all arguemnts converted to another temperature scale and put in a
             to from statement.

    Examples:
        >>> temp_convert(temp_c=50, temp_k=100)
        100 Degrees Kelvin is -173.15 Degrees Celsius
        50 Degrees Celsius is 122 Degrees Farhenheit
        100 Degrees Kelvin is -279.67 Degrees Fahre

       >>> temp_convert(temp_c=-100, temp_k=300)
        300 Degrees Kelvin is 26.85 Degrees Celsius
        -100 Degrees Celsius is -148 Degrees Farhenheit
        300 Degrees Kelvin is 80.33 Degrees Fahrenheit

        >>> temp_convert(temp_k=40, temp_c=120)
        40 Degrees Kelvin is -233.15 Degrees Celsius
        120 Degrees Celsius is 248 Degrees Farhenheit
        40 Degrees Kelvin is -387.67 Degrees Fahrenheit
    """

    k_to_c = temp_k - 273.15
    c_to_f = temp_c * 1.8 + 32
    k_to_f = temp_k * 1.8 - 459.67

    print temp_k, 'Degrees', 'Kelvin', 'is', k_to_c, 'Degrees', 'Celsius'
    print temp_c, 'Degrees', 'Celsius', 'is', c_to_f, 'Degrees', 'Farhenheit'
    print temp_k, 'Degrees', 'Kelvin', 'is', k_to_f, 'Degrees', 'Fahrenheit'
