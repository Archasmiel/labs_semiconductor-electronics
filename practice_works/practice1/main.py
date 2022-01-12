import practice_works.library.calc as calculus

labels = []
calc = calculus.Calculus1()

na = 3.81 * (10**16)
nd = 2.67 * (10**17)

materials = ["Германій", "Кремній", "Арсенід галію"]
temps = [i+273.15 for i in [20, 75, 130]]
mns = [1.64, 0.98, 0.067]
mps = [0.082, 0.19, 0.47]
tor_ns = [3900, 1500, 8500]
tor_ps = [1900, 450, 400]
delta_es = [0.67, 1.12, 1.42]

for cur in range(3):

    material = materials[cur]
    mn = mns[cur]
    mp = mps[cur]
    tor_n = tor_ns[cur]
    tor_p = tor_ps[cur]
    delta_e = delta_es[cur]
    ns = [[], []]
    ps = [[], []]
    sigmas = [[], []]
    ros = [[], []]

    labels.append('Матеріал: ' + str(material))
    labels.append('Концентрація акцептора: ' + str(na) + ' см^-3')
    labels.append('Концентрація донора: ' + str(nd) + ' см^-3')
    labels.append('Ефективна маса електрона: ' + str(mn))
    labels.append('Ефективна маса дірки: ' + str(mp))
    labels.append('Рухливість електрона: ' + str(tor_n) + ' см^2/(В*с)')
    labels.append('Рухливість дірки: ' + str(tor_p) + ' см^2/(В*с)')
    labels.append('Ширина забороненої зони: ' + str(delta_e) + ' еВ')

    for i in range(len(materials)):
        labels.append('----------------------------------------------------------')

        temp = temps[i]
        labels.append('T = ' + str(temp) + ' K')

        nc = calc.get_nc(mn, temp) * 10**-6   # множитель 10**-6 для перевода из м^-3 в см^-3
        nv = calc.get_nv(mp, temp) * 10**-6   # множитель 10**-6 для перевода из м^-3 в см^-3
        ni2 = calc.get_ni2(nc, nv, temp, delta_e)
        labels.append('Nc = ' + str("{:.2e}".format(nc)) + ' см^-3')
        labels.append('Nv = ' + str("{:.2e}".format(nv)) + ' см^-3')
        labels.append('Ni^2 = ' + str("{:.2e}".format(ni2)) + ' см^-6')

        labels.append('\n')
        labels.append('Власний')
        self_n = calc.get_self_n(ni2)
        self_p = calc.get_self_p(ni2)
        self_sigma = calc.get_sigma(self_n, tor_n, self_p, tor_p)
        self_ro = calc.get_ro(self_sigma)
        labels.append('n = ' + str("{:.2e}".format(self_n)) + ' см^-3')
        labels.append('p = ' + str("{:.2e}".format(self_p)) + ' см^-3')
        labels.append('σ = ' + str("{:.2e}".format(self_sigma)) + ' 1/(Ом*см)')
        labels.append('ρ = ' + str("{:.2e}".format(self_ro)) + ' Ом*см')
        ns[0].append(self_n)
        ps[0].append(self_p)
        sigmas[0].append(self_sigma)
        ros[0].append(self_ro)

        labels.append('\n')
        labels.append('Компенсований')
        compensate_n = calc.get_compensate_n(na, nd, ni2)
        compensate_p = calc.get_compensate_p(na, nd, ni2)
        compensate_sigma = calc.get_sigma(compensate_n, tor_n, compensate_p, tor_p)
        compensate_ro = calc.get_ro(compensate_sigma)
        labels.append('n = ' + str("{:.2e}".format(compensate_n)) + ' см^-3')
        labels.append('p = ' + str("{:.2e}".format(compensate_p)) + ' см^-3')
        labels.append('σ = ' + str("{:.2e}".format(compensate_sigma)) + ' 1/(Ом*см)')
        labels.append('ρ = ' + str("{:.2e}".format(compensate_ro)) + ' Ом*см')
        ns[1].append(compensate_n)
        ps[1].append(compensate_p)
        sigmas[1].append(compensate_sigma)
        ros[1].append(compensate_ro)

    labels.append('----------------------------------------------------------')
    labels.append('        n         Власний             Компенсований')
    for i in range(len(ros[1])):
        labels.append(str(temps[i]) + ' :    ' + str(ns[0][i]) + ' см^-3      ' + str(
            ns[1][i]) + ' см^-3')
    labels.append('----------------------------------------------------------')
    labels.append('----------------------------------------------------------')
    labels.append('         p        Власний             Компенсований')
    for i in range(len(ros[1])):
        labels.append(str(temps[i]) + ' :    ' + str(ps[0][i]) + ' см^-3      ' + str(
            ps[1][i]) + ' см^-3')
    labels.append('----------------------------------------------------------')
    labels.append('----------------------------------------------------------')
    labels.append('         σ        Власний             Компенсований')
    for i in range(len(ros[1])):
        labels.append(str(temps[i]) + ' :    ' + str(sigmas[0][i]) + ' См/см      ' + str(
            sigmas[1][i]) + ' См/см')
    labels.append('----------------------------------------------------------')
    labels.append('----------------------------------------------------------')
    labels.append('         ρ        Власний             Компенсований')
    for i in range(len(ros[1])):
        labels.append(str(temps[i]) + ' :    ' + str(ros[0][i]) + ' Ом*см      ' + str(
            ros[1][i]) + ' Ом*см')
    labels.append('----------------------------------------------------------')
    labels.append('\n\n\n#############################################################################\n\n\n')


with open(f'materials.txt', 'w', encoding='utf-8') as f:
    for i in labels:
        f.write(str(i) + '\n')
