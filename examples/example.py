import pandas as pd
import numpy as np

import plotly.graph_objects as go
import matplotlib as mpl
from matplotlib.lines import Line2D

from ..reportity import reportity
from matplotlib import pyplot as plt


pd.options.display.float_format = '{:,}'.format

def main():
    dataframe = get_dataframe()

    fig1 = get_figure_1()
    fig2 = get_figure_2(
        dataframe=dataframe,
    )
    fig3 = get_figure_3()
    plotly_fig = get_plotly_figure()

    report = reportity.Reportity(
        title='Reportity Example',
    )
    report.print_header(
        text='Description',
        level=1,
    )
    report.print_paragraph(
        text='This is an example of Reportity<br>Look how easy it is'
    )
    report.print_header(
        text='Data',
        level=1,
    )
    report.print_paragraph(
        text='This is a dataframe with some data'
    )
    report.print_dataframe(
        dataframe=dataframe,
        max_rows=5,
    )
    report.print_header(
        text='Figures',
        level=1,
    )
    report.print_paragraph(
        text='Some graphs, We strongly recommend to use Plotly but you can use matplotlib if you want '
    )
    report.print_header(
        text='Plotly Figures',
        level=2,
    )
    report.print_figure(
        figure=plotly_fig
    )
    report.print_header(
        text='Matplotlib Figures',
        level=2,
    )
    report.print_figure(
        figure=fig1,
        image=False,
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

    report.save_as_html(
        path='example_report.html',
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
    x = np.arange(10)
    y = x ** 2
    plt.plot(x,y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(
        b=True,
    )
    plt.title('y=x^2',fontsize=20)

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
    points = np.ones(5)
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

    for y, fill_style in enumerate(Line2D.fillStyles):
        ax.text(-0.5, y, nice_repr(fill_style), **text_style)
        ax.plot(y * points, fillstyle=fill_style, **marker_style)
        format_axes(ax)
        ax.set_title('fill style')

    return fig

def get_plotly_figure():
    x = np.arange(10)
    fig = go.Figure(data=go.Scatter(x=x, y=x**2))

    fig.update_layout(
        width=1000,
        paper_bgcolor="LightSteelBlue",
        title='y = x^2',
        xaxis_title="X",
        yaxis_title='Y',
            font=dict(
            size=18,
        )
    )

    return fig


if __name__ == "__main__":
    main()
