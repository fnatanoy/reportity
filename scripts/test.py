import reportity_c
import pandas as pd
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


    reportity = reportity_c.Reportity(
        title='Test',
    )
    reportity.add_header(
        text='Description',
        level=1,
    )
    reportity.add_paragraph(
        text='This is data of pepole'
    )
    reportity.add_header(
        text='Data',
        level=2,
    )
    reportity.add_paragraph(
        text='The data - '
    )
    reportity.add_dataframe(
        dataframe=data,
    )
    reportity.add_header(
        text='Figures',
        level=1,
    )
    reportity.add_figure(
        figure=fig1,
    )
    reportity.add_figure(
        figure=fig2,
    )
    reportity.add_paragraph(
        text='here mpld3 is not supporting scatter plot, so an image is presented'
    )
    reportity.show()

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