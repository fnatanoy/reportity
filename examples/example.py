import pandas as pd
import numpy as np

# from . context import reportity
import matplotlib as mpl
from matplotlib.lines import Line2D

from reportity import reportity
from matplotlib import pyplot as plt

pd.options.display.float_format = '{:,}'.format

def main():
    dataframe = get_dataframe()

    fig1 = get_figure_1()
    fig2 = get_figure_2(
        dataframe=dataframe,
    )
    fig3 = get_figure_3()

    report = reportity.Reportity(
        title='Reportity Example',
    )
    report.print_header(
        text='Description',
        level=1,
    )
    report.print_paragraph(
        text='This is an example of Reportity'
    )
    report.print_header(
        text='Data',
        level=2,
    )
    report.print_paragraph(
        text='The data'
    )
    report.print_dataframe(
        dataframe=dataframe,
        max_rows=5,
    )
    report.print_header(
        text='Figures',
        level=2,
    )
    report.print_figure(
        figure=fig1,
        image=True,
    )
    report.print_figure(
        figure=fig2,
    )
    report.print_header(
        text='Complicated Figures',
        level=2,
    )
    report.print_paragraph(
        text='Here we have a complicated figure that mpld3 doesn\'t know how to convert properly. In this case we will use an image insted of an interactive figure'
    )
    report.print_figure(
        figure=fig3,
    )
    report.print_figure(
        figure=fig3,
        image=True,
    )
    report.show()

def get_dataframe():
    raw_data = {
        'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'], 
        'age': [42, 52, 36, 24, 73], 
        'preTestScore': [4, 24, 31, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70],
        'cost': [2523423.423432, 923423423.44, 243457, 4343462, 74343210],
    }

    return pd.DataFrame(raw_data)

def get_figure_1():
    fig, ax = plt.subplots()
    x = np.linspace(0, 2 * np.pi, 500)
    y1 = np.sin(x)
    y2 = np.sin(3 * x)
    ax.fill(x, y1, 'b', x, y2, 'r', alpha=0.3)
    plt.xlabel('XX')
    plt.ylabel('Cool Graph')
    plt.grid(
        b=True,
    )
    plt.title('Cool Graph',fontsize=20)

    return fig


def get_figure_2(
    dataframe,
):
    fig = plt.figure()
    plt.scatter(dataframe['age'],dataframe['preTestScore'],s=dataframe['preTestScore'])

    plt.xlabel('Age')
    plt.ylabel('Pre Test Score')
    plt.grid(
        b=True,
    )
    plt.title('Scores Vs Age Scatter Plot',fontsize=20)

    return fig


def get_figure_3():
    points = np.ones(5)  # Draw 3 points for each line
    text_style = dict(horizontalalignment='right', verticalalignment='center',
                    fontsize=12, fontdict={'family': 'monospace'})
    marker_style = dict(color='cornflowerblue', linestyle=':', marker='o',
                        markersize=15, markerfacecoloralt='gray')

    def format_axes(ax):
        ax.margins(0.2)
        ax.set_axis_off()

    def nice_repr(text):
        return repr(text).lstrip('u')

    fig, ax = plt.subplots()

    # Plot all fill styles.
    for y, fill_style in enumerate(Line2D.fillStyles):
        ax.text(-0.5, y, nice_repr(fill_style), **text_style)
        ax.plot(y * points, fillstyle=fill_style, **marker_style)
        format_axes(ax)
        ax.set_title('fill style')

    return fig


if __name__ == "__main__":
    main()
