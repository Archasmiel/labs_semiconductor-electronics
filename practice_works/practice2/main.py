import practice_works.library.calc as calculus

calc1 = calculus.Calculus1()
calc2 = calculus.Calculus2()

materials = ["Германій", "Кремній", "Арсенід галію"]

# choose correct index from materials list
mat = 1
# write here your acceptor and donor concentrations in cm^-3
na = 2.16 * (10**17)
nd = 3.62 * (10**16)
# True if base has ntype semiconductor, False otherwise
is_base_ntype = na > nd


# table values from Borisov's book
mns = [1.64, 0.98, 0.067]
mps = [0.082, 0.19, 0.47]
tor_ns = [3900, 1500, 8500]
tor_ps = [1900, 450, 400]
delta_es = [0.72, 1.12, 1.43]
# ni^2 value only for this example from Borisov's book (cm^-6)
ni2 = 2.1 * 10**20


# material characteristics by your input index upper
material = materials[mat]
mn = mns[mat]
mp = mps[mat]
tor_n = tor_ns[mat]
tor_p = tor_ps[mat]
delta_e = delta_es[mat]


# computation of
# n-type (base)
n_ntype = calc2.get_n_ntype(nd, ni2)
p_ntype = calc2.get_p_ntype(nd, ni2)
sigma_ntype = calc1.get_sigma(n_ntype, tor_n, p_ntype, tor_p)
ro_ntype = calc1.get_ro(sigma_ntype)

# p-type (emitter)
n_ptype = calc2.get_n_ptype(na, ni2)
p_ptype = calc2.get_p_ptype(na, ni2)
sigma_ptype = calc1.get_sigma(n_ptype, tor_n, p_ptype, tor_p)
ro_ptype = calc1.get_ro(sigma_ptype)

# self (junction)
n_self = calc2.get_n_self(ni2)
p_self = calc2.get_p_self(ni2)
sigma_self = calc1.get_sigma(n_self, tor_n, p_self, tor_p)
ro_self = calc1.get_ro(sigma_self)

with open(f'materials.txt', 'w', encoding='utf-8') as f:

    f.write(f'Material is {material}\n\n')

    if is_base_ntype:
        f.write('Base: n-type\nEmitter: p-type\nJunction: self\n\n')
    else:
        f.write('Base: p-type\nEmitter: n-type\nJunction: self\n\n')

    f.write(f'n-type semiconductor{" (base)" if na > nd else " (emitter)"}:\n')
    f.write(f'n: {n_ntype} cm^-3\np: {p_ntype} cm^-3\nσ: {sigma_ntype} Sm/sm\nρ: {ro_ntype} Ohm*sm\n\n')

    f.write(f'p-type semiconductor{" (base)" if na < nd else " (emitter)"}:\n')
    f.write(f'n: {n_ptype} cm^-3\np: {p_ptype} cm^-3\nσ: {sigma_ptype} Sm/sm\nρ: {ro_ptype} Ohm*sm\n\n')

    f.write('self semiconductor:\n')
    f.write(f'n: {n_self} cm^-3\np: {p_self} cm^-3\nσ: {sigma_self} Sm/sm\nρ: {ro_self} Ohm*sm\n\n')

    phiT = calc2.get_phiT(300)
    phi0 = calc2.get_phi0(phiT, na, nd, ni2)
    # junction width calc - don't touch 10**6 if you using cm^-3 - its converting to m^-3
    j_width = calc2.get_junction_width(11.9, na*10**6, nd*10**6, phi0)
    jn_width = calc2.get_junction_n_width(j_width, na, nd)
    jp_width = calc2.get_junction_p_width(j_width, na, nd)
    f.write(f'φT = {phiT} V\n')
    f.write(f'φ0 = {phi0} V\n')
    f.write(f'junction_width = {j_width} m\n')
    f.write(f'junction_n_width  = {jn_width} m\n')
    f.write(f'junction_p_width  = {jp_width} m\n')
