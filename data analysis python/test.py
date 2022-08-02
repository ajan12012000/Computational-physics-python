''' required physical constants given in SI units'''
m_el   = 9.1094e-31      # mass of electron in [kg]
hbar   = 1.0546e-34      # Planck's constant over 2 pi [Js]
e_el   = 1.6022e-19      # electron charge in [C]
L_bohr = 5.2918e-11      # Bohr radius [m]

# YOUR CODE HERE
import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def solve(energy, func):
    x = np.linspace(0, L_bohr, 1000)
    sol = odeint(func, [0, 1], x, args=(energy,))
    return sol[999,0]
def eqn(y, x, energy):
    psi, dpsi = y
    diff = [dpsi, (2*m_el/hbar**2)*(0 - energy)*psi]
    return diff

value1 = solve(100*e_el, eqn)
i = 100
while value1 > 0:
    i += 0.1
    value1 = solve(i*e_el, eqn)
i = round(i, 1)
print('The ground state to the nearest tenth decimal is', i)

# solution to part (b)
# YOUR CODE HERE

def solve2(energy, func):
    x = np.linspace(-10*10**-11, 10*10**-11, 1000)
    sol = odeint(func, [0, 1], x, args=(energy,))
    return sol[:, 0]
def eqn2(y, x, energy):
    psi, dpsi = y
    diff = [dpsi, (2*m_el/hbar**2)*(50*e_el*(x**2)*10**22 - energy)*psi]
    return diff

def result():
    energy = np.linspace(0, 900, 900)
    boundary = []
    for i in range(len(energy)-1):
        boundary.append(solve2(energy[i] * e_el, eqn2)[-1])
    rougheigen = []
    for j in range(len(boundary)-1):
        if (boundary[j] > 0 and boundary[j+1] < 0) or (boundary[j] < 0 and boundary[j+1] > 0):
            rougheigen.append(j)
    difference = []
    for k in range(len(rougheigen)-1):
        difference.append(abs(rougheigen[k+1]-rougheigen[k]))
    difference = np.array(difference)
    return np.average(difference)

print('The difference between eigenvalues is', result())
def normalising(psi):
    integral = np.dot(psi, psi)
    p = psi/np.sqrt(integral)
    p = p.reshape(4, 250)
    pdel = np.delete(p, 3, 0)
    pdel = np.delete(pdel, 1, 0)
    pdel = pdel.reshape(500,)
    return pdel

x = np.linspace(-5*10**-11, 5*10**-11, 500)
groundstate = normalising(solve2(137*e_el, eqn2))
firststate = normalising(solve2(413*e_el, eqn2))
secondstate = normalising(solve2(689*e_el, eqn2))
plt.plot(x, groundstate, 'b', label='groundstate')
plt.plot(x, firststate, 'r', label='firststate')
plt.plot(x, secondstate, 'g', label='secondstate')
plt.title('Normalised wavefunction')
plt.xlabel('x')
plt.ylabel('psi value')
plt.show()