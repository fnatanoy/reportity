import re
import os
import mpld3
import base64
import plotly
import matplotlib

from io import BytesIO
from mpld3._server import serve
from matplotlib import pyplot as plt

import pandas as pd


current_path = os.path.dirname(__file__)
resources_path = os.path.abspath(
    os.path.join(
        current_path,
        'resources',
    )
)
favicon_path = os.path.join(
    resources_path,
    'favicon.png',

)
class Reportity():
    def __init__(
        self,
        title,
    ):
        self.html = ''
        self.figures_next_id = 0
        self.figures_href = ''
        self.html_ended = False

        self.html = '''
            <!DOCTYPE html>
            <html lang="en">

            <head>
                <style>
                body {{
                    margin:20;
                    padding:20
                }}
                div {{
                margin: 25px;
                }}
                .center {{
                    display: block;
                    margin-left: auto;
                    margin-right: auto;
                    width: 50%;
                }}
                .plotly-graph-div {{
                    display: block;
                    margin-left: auto;
                    margin-right: auto;
                    width: 50%;
                }}
                hr {{ 
                    display: block;
                    margin-top: 0.5em;
                    margin-bottom: 0.5em;
                    margin-left: auto;
                    margin-right: auto;
                    border-style: inset;
                    border-width: 1px;
                }}
                </style>
                <title>{title}</title>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel="icon" href={favicon_path}>
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
                <script src="https://cdn.plot.ly/plotly-latest.min.js"></script> 
            </head>
            <body>
        '''.format(
            title=title,
            favicon_path=favicon_path,
        )

        self.html += '<h1 align="center", style="font-size:400%">{title}</h1><hr>figures_hrefs'.format(
            title=title,
        )

    def __end_html__(
        self,
    ):
        if self.html_ended:
            return

        self.html_ended = True
        self.html += '''
            </body>
            </html>
        '''

        self.figures_href = '<h1 >Figures List</h1>' + self.figures_href
        self.html = re.sub(
            pattern='figures_hrefs',
            repl=self.figures_href,
            string=self.html,
        )

    def print_paragraph(
        self,
        text,
    ):
        self.html += '<div><p>{text}</p></div>'.format(
            text=text,
        )

    def print_header(
        self,
        text,
        level,
    ):
        self.html += '<h{level}>{text}</h{level}>'.format(
            level=level,
            text=text,
        )

    def print_dataframe(
        self,
        dataframe,
        max_rows=100,
    ):
        html_table = '<div class="container">'
        html_table += dataframe.to_html(
            max_rows=max_rows,
        )
        html_table += '</div>'

        html_table = re.sub(
            pattern=r'<table.+>',
            repl='<table class="table table-hover table-striped">',
            string=html_table,
        )

        self.html += html_table

    def print_figure(
        self,
        figure,
        figure_name=None,
        image=False,
    ):
        if type(figure) == matplotlib.figure.Figure:
            fig_html, figure_name = self._convert_matplotlib_figure(
                figure=figure,
                image=image,
                figure_name=figure_name,
            )

        if type(figure) == plotly.graph_objs._figure.Figure:
            fig_html, figure_name = self._convert_plotly_figure(
                figure=figure,
                image=image,
                figure_name=figure_name,
            )

        figure_id = self.get_next_id()
        figure_name_html = '<div><p id="{figure_id}">{figure_name}</p></div>'.format(
            figure_id=figure_id,
            figure_name=figure_name,
        )
        self.figures_href += '<a href="#{figure_id}">{figure_name}</a><br>'.format(
            figure_id=figure_id,
            figure_name=figure_name,
        )

        self.html += figure_name_html
        self.html += fig_html

    def get_figure_image_html(
        self,
        figure,
    ):
        buf = BytesIO()
        figure.savefig(
            buf,
            format='png',
        )
        data = base64.b64encode(buf.getbuffer()).decode('ascii')
        fig_html = '<img src=\'data:image/png;base64,{data}\' class="center" />'.format(
            data=data,
        )

        return fig_html

    def get_next_id(
        self,
    ):
        self.figures_next_id += 1

        return self.figures_next_id

    def show(
        self,
    ):
        
        self.__end_html__()
        serve(self.html)

    def save_as_html(
        self,
        path,
    ):
        self.__end_html__()

        with open(
            file=path,
            mode='w',
        ) as f: 
            f.write(self.html) 

    def save_as_pdf(
        self,
        path,
    ):
        self.__end_html__()

        raise NotImplementedError

    def _convert_matplotlib_figure(
        self,
        figure,
        figure_name,
        image,
    ):
        if not figure_name:
            try:
                figure_name = figure.axes[0].get_title()
            except:
                figure_name = 'figure'

        if image:
            fig_html = self.get_figure_image_html(
                figure=figure,
            )
        else:
            try:
                fig_html = mpld3.fig_to_html(figure).split('<div ')
                fig_html = fig_html[0] + '<div align="center" ' + fig_html[1]

            except:
                fig_html = self.get_figure_image_html(
                    figure=figure,
                )

        return fig_html, figure_name

    def _convert_plotly_figure(
        self,
        figure,
        figure_name,
        image,
    ):
        if not figure_name:
            try:
                figure_name = figure['layout']['title']['text']
            except KeyError:
                figure_name = 'figure'


        fig_html = plotly.offline.plot(figure, include_plotlyjs=False, output_type='div')

        return fig_html, figure_name