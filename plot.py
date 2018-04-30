#! /usr/bin/env python
# -*- coding: utf-8 -*-
from numpy import *
from matplotlib.pyplot import *

x = linspace( 0, 2 * pi, 50)
plot( x, sin(x), 'r^-', x, sin(2 * x), 'bo-')
legend(['sin', 'cos'])
title('huitu')
grid()
show()