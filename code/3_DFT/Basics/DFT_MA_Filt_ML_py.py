#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
#===========================================================================
# DFT_MA_Filt_ML_py.py
#
# Python Musterl�sung zu "DFT des MA-Filters"
#
# Berechnung und Darstellung der DFT in Python
#
#
#
#
# (c) 2014-Feb-04 Christian M�nker - Files zur Vorlesung "DSV auf FPGAs"
#===========================================================================
from __future__ import division, print_function, unicode_literals # v3line15

import numpy as np
import numpy.random as rnd
from numpy import (pi, log10, exp, sqrt, sin, cos, tan, angle, arange,
                    linspace, array, zeros, ones)
from numpy.fft import fft, ifft, fftshift, ifftshift, fftfreq
import scipy.signal as sig
import scipy.interpolate as intp

import matplotlib.pyplot as plt
from matplotlib.pyplot import (figure, plot, stem, grid, xlabel, ylabel,
    subplot, title, clf, xlim, ylim)

#import dsp_fpga_lib as dsp
#------------------------------------------------------------------ v3line30
# ... Ende der Import-Anweisungen
h = [1,1,1,1]
n = arange(len(h))
figure(1);
subplot(211)
stem(n,h)
ylabel(r"$h[n] \; \rightarrow$")
xlabel(r"$n \; \rightarrow$")
subplot(212)
H = abs(fft(h,256))
k = arange(len(H)/2)
stem(k,H[:len(k)])
xlabel(r"$k \; \rightarrow$")
ylabel(r"$|H[k]| \; \rightarrow$")
plt.tight_layout()
plt.show()
