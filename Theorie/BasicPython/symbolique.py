#!/usr/bin/env python
# coding: utf-8

from sympy import *

x  = Symbol('x')
pi = Symbol('pi')
L  = Symbol('L')


# $$F(x) = sin (\frac{\pi}{L} x)$$

fx = sin(pi/L*x)

print('Derivee:',diff(fx,x))

