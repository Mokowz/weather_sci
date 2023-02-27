import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from math import pi,cos

import streamlit as st

df = pd.read_table("weather.txt", delimiter=',')

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('Weather Data Plots')

x = df["Tmax"].to_numpy()
x_100 = x[:100]

y = df["day"].to_numpy()
y_100 = y[:100]

plt.plot(x,y, '.')
st.pyplot()

def line(t, a, b, c):
    return a * np.cos(2*pi*t+b) + c

popt, pcov=  curve_fit(line, x_100, y_100)

e=np.repeat(10., 100)

plt.errorbar(x_100,y_100,yerr=e, fmt="none")
st.pyplot()

popt, pcov=curve_fit(line, x_100,y_100, sigma=e)

plt.errorbar(x_100,y_100,yerr=e, fmt="none")

xfine=np.linspace(0., 100., 100)
plt.plot(xfine, line(xfine,popt[0], popt[1], popt[2]), 'r-')
st.pyplot()