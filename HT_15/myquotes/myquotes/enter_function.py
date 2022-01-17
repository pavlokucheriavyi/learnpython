from datetime import datetime


def enter_date():
    """
    The function asks the user to enter the date
    and checks if it is correct

    :return: date entered by the client
    """
    flag = True
    while flag:
        try:
            date = input('Enter the date of the news you would like to read, '
                         'in format - day, month, year. example(5.1.2022): ')

            date_format = "%d.%m.%Y"
            start = datetime.strptime(date, date_format)
            now = datetime.now()

            if start > now:
                print('Your date in the future, please enter again')
            else:
                my_string = date.split('.')
                # the var 'res_string' initializes the date in a format
                # suitable for concatenation from the main scraper url
                res_string = "/".join(reversed(my_string)) + '/'
                # with return exits the infinite loop if the date is entered correctly
                return res_string
        except ValueError:
            print('You entered the wrong date. Please repeat again. Example(12.11.2021)')


# a variable to send the date to the scraper
var_for_spider = enter_date()

# the variable formats the result of the function 'enter_date'
# function to pass the date in the name of the future csv file
var_for_name_of_file = '_'.join(var_for_spider.split('/'))[:-1:]


# print(help(enter_date))                                   # uncomment to review the documentation