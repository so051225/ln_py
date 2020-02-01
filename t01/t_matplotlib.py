
from matplotlib.pyplot import *


def simple_plot(data, x_label, y_label, title_str):
    plot(data)
    xlabel(x_label)
    ylabel(y_label)
    title(title_str)
    show()

simple_plot([1, 2, 3, 10], 'x', 'y', 'title')

plot([1, 2, 3, 10])

xlabel("x- axis")
ylabel("random numbers")
title('my figure')

show()



