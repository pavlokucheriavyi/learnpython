class Books(object):
    def __init__(self, author, pages, year):
        self.author = author
        self.pages = pages
        self.year = year


class HighSchool(Books):
    def __init__(self, author, pages, year, country):
        super().__init__(author, pages, year)
        self.cot = 'high school'
        self.lov = country

    def check_language(self):
        if self.lov == 'Ukraine':
            self.lov = 'ukrainian'
            return f'This book is {self.year} year. Book author - {self.author}. The book has {self.pages} pages. This book is {self.lov} literature. Designed for {self.cot} students.'
        elif self.lov == 'Russia':
            self.lov = 'russian'
            return f'This book is {self.year} year. Book author - {self.author}. The book has {self.pages} pages. This book is {self.lov} literature. Designed for {self.cot} students.'
        else:
            self.lov = 'foreign'
            return f'This book is {self.year} year. Book author - {self.author}. The book has {self.pages} pages. This book is {self.lov} literature. Designed for {self.cot} students.'



class MidlleSchool(Books):
    def __init__(self, author, pages, year, country):
        super().__init__(author, pages, year)
        self.cot = 'midlle school'
        self.lov = country

    def check_language(self):
        if self.lov == 'Ukraine':
            self.lov = 'ukrainian'
            return f'This book is {self.year} year. Book author - {self.author}. The book has {self.pages} pages. This book is {self.lov} literature. Designed for {self.cot} students.'
        elif self.lov == 'Russia':
            self.lov = 'russian'
            return f'This book is {self.year} year. Book author - {self.author}. The book has {self.pages} pages. This book is {self.lov} literature. Designed for {self.cot} students.'
        else:
            self.lov = 'foreign'
            return f'This book is {self.year} year. Book author - {self.author}. The book has {self.pages} pages. This book is {self.lov} literature. Designed for {self.cot} students.'

class PrimarySchool(Books):
    def __init__(self, author, pages, year, country_of_text):
        super().__init__(author, pages, year)
        self.cot = 'primary school'
        self.lov = country_of_text

    def check_language(self):
        if self.lov == 'Ukraine':
            self.lov = 'ukrainian'
            return f'This book is {self.year} year. Book author - {self.author}. The book has {self.pages} pages. This book is {self.lov} literature. Designed for {self.cot} students.'
        elif self.lov == 'Russia':
            self.lov = 'russian'
            return f'This book is {self.year} year. Book author - {self.author}. The book has {self.pages} pages. This book is {self.lov} literature. Designed for {self.cot} students.'
        else:
            self.lov = 'foreign'
            return f'This book is {self.year} year. Book author - {self.author}. The book has {self.pages} pages. This book is {self.lov} literature. Designed for {self.cot} students.'


obj_1 = HighSchool('Oruell', 250, 2008, 'England')


result_var = obj_1.check_language()
print(result_var)