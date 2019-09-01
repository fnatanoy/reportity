import pandas as pd

# from . context import reportity
from reportity import reportity
from matplotlib import pyplot as plt


def main():
    data = get_test_data()

    fig1 = plt.figure()
    plt.plot(data['age'],data['preTestScore'],'.')
    plt.xlabel('Age')
    plt.ylabel('Pre Test Score')
    plt.grid(
        b=True,
    )
    plt.title('Scores Vs Age',fontsize=20)

    fig2 = plt.figure()
    plt.scatter(data['age'],data['preTestScore'],s=data['preTestScore'])

    plt.xlabel('Age')
    plt.ylabel('Pre Test Score')
    plt.grid(
        b=True,
    )
    plt.title('Scores Vs Age Scatter Plot',fontsize=20)

    report = reportity.Reportity(
        title='Test',
    )
    report.print_header(
        text='Description',
        level=1,
    )
    report.print_paragraph(
        text='This is data of pepole'
    )
    report.print_header(
        text='Data',
        level=2,
    )
    report.print_paragraph(
        text='The data - '
    )
    report.print_dataframe(
        dataframe=data,
        max_rows=5,
    )
    report.print_header(
        text='Figures',
        level=1,
    )
    report.print_figure(
        figure=fig1,
    )
    report.print_figure(
        figure=fig2,
    )
    report.print_paragraph(
        text='here mpld3 is not supporting scatter plot, so an image is presented'
    )
    report.show()

def get_test_data():
    raw_data = {
        'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'], 
        'age': [42, 52, 36, 24, 73], 
        'preTestScore': [4, 24, 31, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70],
    }

    return pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])


if __name__ == "__main__":
    main()
