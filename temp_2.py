#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Converts temperatures from one scale to another"""

def temp_convert(temp_c=0, temp_k=0):
    """Converts Kelvin to Celsius and Fahrenheit and Celsius to Fahrenheit.

    Args:
        temp_c (int): temperature in Celsius to convert to Fahrenheit.
		      Default=0.
        temp_k (int): temperature in Kelvin to convert to Fahrenheit and
		      Celsius. Default=0.

    Returns:
        int: all arguemnts converted to another temperature scale. Order listed
             Kelvin to Celsius, Celsius to Fahrenheit, Kelvin to Fahrenheit.

    Examples:
        >>> temp_convert(temp_c=50)
        (-273.15, 122, -459.67

        >>> temp_convert(temp_c=60, temp_k=200)
        (-73.14999999999998, 140, -99.67000000000002)
    """

    k_to_c = temp_k - 273.15
    c_to_f = temp_c * 1.8 + 32
    k_to_f = temp_k * 1.8 - 459.67

    return (k_to_c, c_to_f, k_to_f).format(
