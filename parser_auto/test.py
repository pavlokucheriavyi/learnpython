test_dict1 = {'silver': 4, 'gold': 2, 'diamond': 5, 'silver2': 4, 'gold3': 2, 'diamond4': 5}

def reverse_dict(dict_main):
    final_dict = {}

    # переворачиваем екстенд дикт
    x = list(dict_main.items())

    for k, v in reversed(x):
        final_dict[k] = v

    # и расширяем его с начальным диктом
    return final_dict

test2 = {'sa': 2, 'z': 4}

test_dict1.update(test2)
print(test_dict1)








