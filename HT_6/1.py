import time

my_dict= [
        {"Red" : "Green"},
        {"Red" : "Green"},
        {"Red" : "Green"},
        {"Red" : "Green"},
        {"Yellow" : "Green"},
        {"Yellow" : "Green"},
        {"Green" : "Red"},
        {"Green" : "Red"},
        {"Green" : "Red"},
        {"Green" : "Red"},
        {"Yellow" : "Red"},
        {"Yellow" : "Red"}
        ]

while True:
    for symbol in my_dict:
        for key, value in symbol.items():
            print(key, value)
            time.sleep(1)
