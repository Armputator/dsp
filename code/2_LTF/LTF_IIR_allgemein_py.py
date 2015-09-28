#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
# LTF_IIR_allgemein_py.py =========================================
# 
#
# Kapitel "LTI-Systeme im Frequenzbereich"
#
# Code zu �bung "Allgemeine IIR-Struktur" 
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

import dsp_fpga_lib as dsp
#------------------------------------------------------------------------
# ... Ende der gem. import-Anweisungen
alpha = 0.9; f_S = 1 
b = [1, 0] # z + 0
# b = [1 0 0] # z^2 + 0
a = [1, -alpha] # z - 0.9; Add., 1 Verz�gerung
#a = [1 +alpha] # z + 0.9; Subtr., 1 Verz.
#a = [1 0 -alpha] # z^2 - 0.9; Add., 2 Verz.
#a = [1 0 +alpha] # z^2 - 0.9; Subtr., 2 Verz.
figure(1) 
dsp.zplane(b,a)  # Plotte P/N Diagramm
# H(f) entlang der oberen H�lfte des EK:
[W,H] = sig.freqz(b,a,1024, f_S)
figure(2) 
plot(W/(2*pi),abs(H),linewidth = 2) # H(F)
xlabel(r'$F$  bzw. $\Omega / 2 \pi$') 
ylabel(r'$|H(F)| \; \rightarrow$')
# Berechne 20 Werte der Impulsantwort:
[himp,t] = dsp.impz(b,a,20,f_S) 
figure(3)
(ml, sl, bl) = stem(t,himp) # Impulsantwort
plt.setp(ml,'markerfacecolor','r',
	'markersize',8)
plt.setp(sl,'linewidth',2)
xlabel('$n$'); ylabel(r'$h[n]$')
plt.show()