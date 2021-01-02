import plotly.graph_objects as go
    
class StayledFigures:
    @staticmethod
    def get_figure():
        fig = go.Figure()
        fig = StayledFigures.update_layout(fig)
        fig = StayledFigures.update_axes(fig)
        return fig
    @staticmethod
    def get_subplot_figure(
        rows,
        cols,
    ):
        return NotImplementedError
    @staticmethod
    def update_layout(fig):
        fig.update_layout(
            paper_bgcolor="#F9F9F9",
            plot_bgcolor="#F9F9F9",
            title='',
            xaxis_title='',
            yaxis_title='',
            font=dict(
                size=18,
            )
        )
        return fig

    @staticmethod
    def update_axes(fig):
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#E9E9E9')
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#E9E9E9')
        fig.update_xaxes(zeroline=True, zerolinewidth=2, zerolinecolor='#E9E9E9')
        fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='#E9E9E9')
        return fig

class Colors:
    blue_dark = '#4e4187'
    blue_light = '#3083dc'
    green = '#37ae9d'
    orange = '#f75c03'
    pink = '#d90368'
    red = '#ba2d0b'
    purple = '#820263'
    black = '#291720'
    gray = '#a49fa0'
    green_light = ' #70ee9c'
