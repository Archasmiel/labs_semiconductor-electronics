import practice_works.library.make_tkinter_window as win
import practice_works.library.calc as calculus1
import tkinter as tk

labels = []
root = tk.Tk()
calc = calculus1.Calculus1()

na = 2.16 * (10**17)
nd = 3.62 * (10**16)

materials = ["Германій", "Кремній", "Арсенід галію"]
temps = [i+273.15 for i in [20, 75, 130]]
mns = [1.64, 0.98, 0.067]
mps = [0.082, 0.19, 0.47]
tor_ns = [3900, 1500, 8500]
tor_ps = [1900, 450, 400]
delta_es = [0.72, 1.12, 1.43]

for cur_material in range(3):

    material = materials[cur_material]
    mn = mns[cur_material]
    mp = mps[cur_material]
    tor_n = tor_ns[cur_material]
    tor_p = tor_ps[cur_material]
    delta_e = delta_es[cur_material]
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
        labels.append('Nc = ' + str(nc) + ' см^-3')
        labels.append('Nv = ' + str(nv) + ' см^-3')
        labels.append('Ni^2 = ' + str(ni2) + ' см^-6')

        labels.append('\n')
        labels.append('Власний')
        self_n = calc.get_self_n(ni2)
        self_p = calc.get_self_p(ni2)
        self_sigma = calc.get_sigma(self_n, tor_n, self_p, tor_p)
        self_ro = calc.get_ro(self_sigma)
        labels.append('n = ' + str(self_n) + ' см^-3')
        labels.append('p = ' + str(self_p) + ' см^-3')
        labels.append('σ = ' + str(self_sigma) + ' 1/(Ом*см)')
        labels.append('ρ = ' + str(self_ro) + ' Ом*см')
        ros[0].append(self_ro)

        labels.append('\n')
        labels.append('Компенсований')
        compensate_n = calc.get_compensate_n(na, nd, ni2)
        compensate_p = calc.get_compensate_p(na, nd, ni2)
        compensate_sigma = calc.get_sigma(compensate_n, tor_n, compensate_p, tor_p)
        compensate_ro = calc.get_ro(compensate_sigma)
        labels.append('n = ' + str(compensate_n) + ' см^-3')
        labels.append('p = ' + str(compensate_p) + ' см^-3')
        labels.append('σ = ' + str(compensate_sigma) + ' 1/(Ом*см)')
        labels.append('ρ = ' + str(compensate_ro) + ' Ом*см')
        ros[1].append(compensate_ro)

    labels.append('----------------------------------------------------------')
    labels.append('                  Власний     Компенсований')
    for i in range(len(ros[1])):
        labels.append(str(temps[i]) + ' :    ' + str(ros[0][i]) + ' Ом*см      ' + str(ros[1][i]) + ' Ом*см')

    win.make_window(root, 'Test', '800x700', labels)
    labels.clear()

root.mainloop()
