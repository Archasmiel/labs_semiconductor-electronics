import matplotlib.pyplot as plt
import library.ploterrorgraph as peg
import library.xlsxio as io

index1 = 0
index2 = 1

columns = [[chr(i) for i in range(ord('A'), ord('F')+1)]] * 4
rows = [[2, 22], [2, 22], [2, 30], [2, 22]]


all_sheets = io.get_all_sheets_from_file('../../data/lab5/data.xlsx', columns, rows)
peg.get_graph_with_errors(plt, all_sheets[index1][2], all_sheets[index1][4], all_sheets[index1][3],
                          all_sheets[index1][5], 2, 0.5, 2, 'k', True, f'Ud, В', f'Id, мА')
peg.get_graph_with_errors(plt, all_sheets[index2][2], all_sheets[index2][4], all_sheets[index2][3],
                          all_sheets[index2][5], 2, 0.5, 2, 'k', False, f'Ud, В', f'Id, мА')
plt.plot([-0.5, 1.5], [0, 0], color='k')
plt.plot([0, 0], [-20, 20], color='k')
plt.title('Діод 1 - ВАХ')
plt.grid()


plt.show()
