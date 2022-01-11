import sqlite3

# РОБОТА З БД

con = sqlite3.connect('maindata.db')
cur = con.cursor()

# СТВОРЮЄМО ТАБЛИЦЮ З КУПЮРАМИ

cur.execute('''CREATE TABLE IF NOT EXISTS inkasator_check
               (banknotes text, quantity integer)''')

banknotes = [

    ('1000', 100),
    ('500', 100),
    ('200', 100),
    ('100', 100),
    ('50', 100),
    ('20', 100),
    ('10', 100)
]
# cur.execute("UPDATE balance SET balance = 800 WHERE balance = 500")

for user in banknotes:
    exists = cur.execute('''SELECT banknotes, quantity FROM inkasator_check WHERE banknotes=?''', (user[0],)).fetchone()
    if not exists:
        cur.execute('''INSERT INTO inkasator_check VALUES (?, ?) ''', user)

same_list = []

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM inkasator_check")
    rows = cur.fetchall()

    for row in rows:
        same_list.append(row)

result_dict = dict()

for i in same_list:
    result_dict[i[0]] = i[1]

# СТВОРЮЄМО ТАБЛИЦЮ З БАЛАНСОМ КЛІЄНТІВ

cur.execute('''CREATE TABLE IF NOT EXISTS users_balance
               (username text, balance integer)''')

balance = [
    ('Pasha', 12500),
    ('Natasha', 11000)
]

for user in balance:
    exists = cur.execute('''SELECT username, balance FROM users_balance WHERE username=?''', (user[0],)).fetchone()
    if not exists:
        cur.execute('''INSERT INTO users_balance VALUES (?, ?) ''', user)

same_list_balance = []

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM users_balance")
    rows = cur.fetchall()

    for row in rows:
        same_list_balance.append(row)

result_dict_balance = dict()

for i in same_list_balance:
    result_dict_balance[i[0]] = i[1]

# СТВОРЮЄМО ТАБЛИЦЮ З ЛОГІНАМИ ТА ПАРОЛЯМИ КЛІЄНТІВ

cur.execute('''CREATE TABLE IF NOT EXISTS users
               (username text, password text, is_inkasator bit DEFAULT false)''')

users = [
    ('Pasha', 'qwerty123', 0),
    ('Natasha', 'kleop', 0),
    ('admin1', 'admin123456', 1),
    ('admin2', 'admin123456', 1)
]

for user in users:
    exists = cur.execute('''SELECT username, password, is_inkasator FROM users WHERE username=?''',
                         (user[0],)).fetchone()
    if not exists:
        cur.execute('''INSERT INTO users VALUES (?, ?, ?) ''', user)

same_list_users = []

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()

    for row in rows:
        same_list_users.append(row)

# СТВОРЮЄМО ТАБЛИЦЮ З ТРАНЗАКЦІЯМИ

cur.execute('''CREATE TABLE IF NOT EXISTS transactions
               (username text, trans cursor)''')

list_trans = [
    ('Pasha', "The client Pasha has replenished the sum of money of $500. The rest of money - 3500\n"
              "The client Pasha withdrew $300 from the account. The rest of money - 3200\n"),
    ('Natasha', "The client Natasha has replenished the sum of money of $4000. The rest of money - 9000\n"
                "The client Natasha withdrew $500 from the account. The rest of money - 8500\n")
]

for user in list_trans:
    exists = cur.execute('''SELECT username, trans FROM transactions WHERE username=?''', (user[0],)).fetchone()
    if not exists:
        cur.execute('''INSERT INTO transactions VALUES (?, ?) ''', user)

same_list_transactions = []

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM transactions")
    rows = cur.fetchall()

    for row in rows:
        same_list_transactions.append(row)

same_dict_trans = [list(x) for x in same_list_transactions]
result_trans_list = []