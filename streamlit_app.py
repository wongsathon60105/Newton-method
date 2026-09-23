import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
st.title("Newton-Raphson Method")
def f(x):
    return x**3+4*x**2+x-1
def df(x):
    return 3*x**2+8*x+1
#main
err=1000
x=st.sidebar.number_input('Enter initial guess')
plt.plot(x, f(x), 'ko')  # Mark the initial guess on the plot
k=0
while(err>=0.0001):
    k=k+1
    xnp1 = x - f(x)/df(x)
    err = abs(xnp1-x)
    x = xnp1
    plt.plot(x, f(x), 'y*')  # Mark the new guess on the plot
st.write('Root is', xnp1)
st.write('No. of iteration', k)
x_vals = np.linspace(-5, 5, 100)
y_vals = [f(x) for x in x_vals]
plt.plot(x_vals, y_vals)
plt.plot(xnp1, f(xnp1), 'ro')  # Mark the root on the plot
plt.plot(x, f(x), 'ro')
plt.grid(True)
st.pyplot(plt)
