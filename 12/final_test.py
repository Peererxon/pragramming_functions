from logging import raiseExceptions
from math import ceil
import pandas as pd
import matplotlib.pyplot as plt  # interface
from natsort import index_natsorted

COLUMN_1 = 'glucose level'
COLUMN_2 = 'time'
COLUMN_3 = 'date'


def main():
    exit = False
    valid_option = False
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
                valid_option = True
            elif answer == 2:
                csv = open_file('glucose_level.xlsx', 'glucose_level')
                show_full_data(csv)
                valid_option = True
            else:
                print_wrong_answer()

            if valid_option:
                answer = input(
                    'Would you like to see your data in a different way? yes/no: ')
                answer = answer.lower()
                if answer == 'yes':
                    exit = False
                elif answer == 'no':
                    print('Thanks for tried our program!')
                    program_rate = evaluate_program()
                    print(
                        f'For you our program is rated at {program_rate} starts. Thanks')
                    exit = True
                else:
                    exit = False
                    print_wrong_answer()
        except ValueError as val_err:
            print(val_err)
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

    csv_sorted = csv.sort_values(by='time')
    csv_sorted.plot(x='time', y=['glucose level'], kind='bar')
    plt.show()


def show_full_data(csv: pd.DataFrame):
    print(csv[COLUMN_1].tolist())


def print_wrong_answer():
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('Please choose a valid option :( ...')
    print('Restarting program....')
    print()


def calculate_average(satisfaction, enjoy, competitive):
    try:
        avg = (satisfaction + enjoy + competitive) / 3
        avg = round(avg, 2)
        return avg

    except TypeError as val_err:
        print(val_err)
        raise TypeError('Arguments are not numbers')


def evaluate_program():
    print('We are going to ask you a couple of question in order that you can evaluate our program :)')
    sat = int(input(
        'From 1 to 5 how much to you feel satisfied using our program?: '))
    enj = int(input('From 1 to 5 how much do you enjoyed our program?: '))
    comp = int(input(
        'From 1 to 5 how much do you think our program is competitive?: '))
    try:

        if (sat > 5 or enj > 5 or comp > 5) or (sat < 1 or enj < 1 or comp < 1):
            raise ValueError('ERROR: Values has to be between 1 and 5 ')
        average_points = calculate_average(sat, enj, comp)
        return average_points
    except ValueError as val_err:
        print()
        print(val_err)
        print_wrong_answer()


if __name__ == "__main__":
    main()
