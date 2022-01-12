import practice_works.library.calc as calculus

calc1 = calculus.Calculus1()
calc2 = calculus.Calculus2()

materials = ["Германій", "Кремній", "Арсенід галію"]

# choose correct index from materials list
mat = 1
# write here your acceptor and donor concentrations in cm^-3
na = 3.12 * (10**15)
nd = 4.25 * (10**16)
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

    if is_base_ntype:
        f.write('База: n-тип напівпровідника\nЕмітер: p-тип напівпровідника\npn-перехід: власний напівпровідник\n\n\n')
    else:
        f.write('База: p-тип напівпровідника\nЕмітер: n-тип напівпровідника\npn-перехід: власний напівпровідник\n\n\n')

    f.write(f'Матеріал: {material}\n')
    f.write(f'Ефективна маса електрона: {mn}\n')
    f.write(f'Ефективна маса дірки: {mp}\n')
    f.write(f'Рухливість електрона: {tor_n} см^2/(В*с)\n')
    f.write(f'Рухливість дірки: {tor_p} см^2/(В*с)\n')
    f.write(f'Ширина забороненої зони: {delta_e} еВ\n')

    f.write(f'Концентрація акцептора: {"{:.2e}".format(na)} cm^-3\n')
    f.write(f'Концентрація донора: {"{:.2e}".format(nd)} cm^-3\n\n\n')
    f.write(f'#######################################\n\n')

    f.write(f'Напівпровідник n-типу {"(база)" if na > nd else "(емітер)"}:\n')
    f.write(f'n: {"{:.2e}".format(n_ntype)} см^-3\np: {"{:.2e}".format(p_ntype)} см^-3\nσ: '
            f'{"{:.2e}".format(sigma_ntype)} См/см\nρ: {"{:.2e}".format(ro_ntype)} Ом*см\n\n')

    f.write(f'Напівпровідник p-типу {"(база)" if na < nd else "(емітер)"}:\n')
    f.write(f'n: {"{:.2e}".format(n_ptype)} см^-3\np: {"{:.2e}".format(p_ptype)} см^-3\nσ: '
            f'{"{:.2e}".format(sigma_ptype)} См/см\nρ: {"{:.2e}".format(ro_ptype)} Ом*см\n\n')

    f.write('Власний напівпровідник:\n')
    f.write(f'n: {"{:.2e}".format(n_self)} см^-3\np: {"{:.2e}".format(p_self)} см^-3\nσ: '
            f'{"{:.2e}".format(sigma_self)} См/см\nρ: {"{:.2e}".format(ro_self)} Ом*см\n\n')

    phiT = calc2.get_phiT(300)
    phi0 = calc2.get_phi0(phiT, na, nd, ni2)
    # junction width calc - don't touch 10**6 if you using cm^-3 - its converting to m^-3
    j_width = calc2.get_junction_width(11.9, na*10**6, nd*10**6, phi0)
    jn_width = calc2.get_junction_n_width(j_width, na, nd)
    jp_width = calc2.get_junction_p_width(j_width, na, nd)
    f.write(f'φT: {phiT} B\n')
    f.write(f'φ0: {phi0} B\n')
    f.write(f'Ширина переходу: {"{:.2e}".format(j_width)} м\n')
    f.write(f'Ширина переходу в n-типі: {"{:.2e}".format(jn_width)} м\n')
    f.write(f'Ширина переходу в p-типі: {"{:.2e}".format(jp_width)} м\n')
