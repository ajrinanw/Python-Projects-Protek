#CAHPTER 08 PYTHON PROJECT 07
def termahal(dictionary):
    key = list(dictionary.keys())
    values = tuple(dictionary.values())
    hargaTermahal = max(values)
    indexhargaTermahal = values.index(hargaTermahal)
    print(key[indexhargaTermahal])

buah = {'apel':5000,
        'jeruk':8500,
        'mangga':7800,
        'duku':6500}

termahal(buah)
