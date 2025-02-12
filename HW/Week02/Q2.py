"""
Author: [Harry Wu]
Assignment / Part: HW2 - Q2
Date due: Feb 13, 11:50pm
I pledge that I have completed this assignment without collaborating
with anyone else, in conformance with the NYU School of engineering Policies and Procedures on Academic Misconduct.
"""

import math

w = float(input("What is the frequency?"))
T = int(input("What us the time duration of the sound wave?"))

fourier_transform = round( ((2 * (math.sin(w * T))) / w), 3)

print("The amplitude spectrum of this Fourier transform is:", fourier_transform)