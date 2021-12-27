import math
import scipy.constants as const
from sympy import *
import practice_works.library.calc as calculus

calc = calculus.Calculus2

rb = 3.06
re = 9.68
Rb = rb + re

phiT = calc.get_phiT(300)
l0 = 0.185 * 10**-4
ni = 1.45 * 10**10
t_ef = 2.5 * 10**-3

q = const.e
S = 2.02 * 10**-5
ni2 = (1.45 * 10**10)**2
Dp = 12.5
Dn = 36
Lp = 1 * 10**-3
Ln = 2 * 10**-3
Nd = 3.62 * 10**16
Na = 2.16 * 10**17
pn0 = 4000

I0 = q*S*ni2*(Dp/Lp/Nd + Dn/Ln/Na)
Ir = q*S*l0*ni/2/t_ef
Ih = q*S*pn0*Dp/Lp
Ig = q*S*l0*ni/2/t_ef
print(I0, Ir)
print(Ih + Ig)

# var('x y')
# plot_implicit(Eq(I0*((math.e**((x - y*Rb)/phiT)) - 1), y), xlim=(-2, 0), ylim=(-20, 20))
# plt.plot([0, 1], [0, 1])

# plt.grid()
# plt.show()
