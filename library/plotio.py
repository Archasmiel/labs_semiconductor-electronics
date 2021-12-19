
def get_graph_with_errors(plot, x, y, error_x, error_y, capsize, elinewidth, dot_size, dot_color, new_fig,
                          x_label, y_label):
    if new_fig:
        plot.figure()
    plot.scatter(x, y, s=dot_size, color=dot_color)
    plot.errorbar(x, y, xerr=error_x, yerr=error_y, capsize=capsize, elinewidth=elinewidth, ls='none')
    plot.xlabel(x_label)
    plot.ylabel(y_label)
