import matplotlib.pyplot as plt
import numpy as np

import library.ploterrorgraph as peg
import library.xlsxio as io

index1 = 2
index2 = 3

columns = [[chr(i) for i in range(ord('A'), ord('F')+1)]] * 4
rows = [[2, 22], [2, 22], [2, 30], [2, 22]]


all_sheets = io.get_all_sheets_from_file('../../data/lab5/data.xlsx', columns, rows)
peg.get_graph_with_errors(plt, all_sheets[index1][2], all_sheets[index1][4], all_sheets[index1][3],
                          all_sheets[index1][5], 2, 0.5, 2, 'k', True, f'Ud, мВ', f'Id, мА')
plt.plot([-0.1, 1.5], [0, 0], color='k')
plt.plot([0, 0], [-1, 20], color='k')
plt.title('Діод 2 - прямий')
plt.grid()


peg.get_graph_with_errors(plt, np.array(all_sheets[index2][2]) * 0.001, all_sheets[index2][4],
                          np.array(all_sheets[index2][3]) * 0.001,
                          all_sheets[index2][5], 2, 0.5, 2, 'k', True, f'Ud, мВ', f'Id, мА')
plt.plot([-0.5, 0.1], [0, 0], color='k')
plt.plot([0, 0], [-20, 1], color='k')
plt.title('Діод 2 - зворотний')
plt.grid()

plt.show()
