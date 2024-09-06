## SOAL 01


def fact (angka):
    if angka ==0 or angka ==1:
        return 1
    else:
        return angka * fact(angka-1)

print (fact(9))



## SOAL 02


def function (angka):
        return list (map(lambda number : 'Ganjil' if number % 2 != 0 else 'Genap', angka))


angkaInput = [22,17,19,20,14]
print (function(angkaInput))


##SOAL 03

def filterGaji (gajiList):
    def filterAtas (gaji):
        return gaji * 0.95 > 9000000
    
    return list (filter(filterAtas, gajiList))

gajiList = [9100000,9800000,9500000,10300000,9300000]

hasilFilter = filterGaji(gajiList)
print(hasilFilter)