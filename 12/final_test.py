import pandas as pd
import matplotlib.pyplot as plt  # interface
from natsort import index_natsorted

COLUMN_1 = 'glucose level'
COLUMN_2 = 'time'
COLUMN_3 = 'date'


def main():
    exit = False

    while not exit:
        print()
        print('Welcome! This is a glucose level program that will help you to visualice your glucose tracks.')
        print()
        print('In wich way do you want to see your data?')
        print('please press 1 for a bar graph.')
        print('please press 2 to just see a list of the data')

        try:
            answer = int(input('Pick your visual approach: '))
            if answer == 1:
                csv = open_file('glucose_level.xlsx', 'glucose_level')
                print_plot(csv)
                exit = True
            elif answer == 2:
                csv = open_file('glucose_level.xlsx', 'glucose_level')
                show_full_data(csv)
                exit = True
            else:
                print_wrong_answer()
        except ValueError as val_err:
            print_wrong_answer()


"""     download_url = (
        "https://raw.githubusercontent.com/fivethirtyeight/"
        "data/master/college-majors/recent-grads.csv"
    )

    df = pd.read_csv(download_url)
    type(df)

    pd.set_option("display.max.columns", None)

    df.plot(x="Rank", y=["P25th", "Median", "P75th"], kind='pie')
    plt.show()  # showing GUI interface with the data """


def open_file(filename, sheet_name):
    # csv = pd.read_excel('.', 'glucose_level.xlsx')
    csv = pd.read_excel(filename, sheet_name=sheet_name)
    return csv


def print_plot(csv: pd.DataFrame):

    def split_dates(militar_time):
        print(militar_time)
        list_mapped = map(lambda column: [[column[0]], [
                          column[1]].strftime("%H%M%S")], militar_time)
        return list_mapped
        try:
            """             [hour, minutes] = militar_time.split(':')
            full_time = int(hour) + int(minutes)
            print(full_time) """
            print(int(militar_time.strftime("%H%M%S")))
            
            # return int(militar_time.strftime("%Y%m%d%H%M%S"))

        except ValueError as val_err:
            print(
                'please fill your xls with valid data in militar time EX:[17:15:59]')
            print(val_err)

    csv.sort_values(by='time', key=lambda col: split_dates(col))
    csv.plot(x='time', y=['glucose level'], kind='bar')
    plt.show()


def show_full_data(csv: pd.DataFrame):
    print(csv[COLUMN_1].tolist())


def print_wrong_answer():
    print('Please choose a valid option :( ...')
    print('Restarting program....')


if __name__ == "__main__":
    main()
