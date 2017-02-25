def GuGuDan(number):
    for i in range(2, number+1):
        for j in range(2, 10):
            print(i, 'X', j, '=', i*j)
        print('\r')

GuGuDan(3)
