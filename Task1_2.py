""" Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z  для всех значений предикат.  """



def checkPredicate(array):
    left = not (array[0] or array[1] or array[2])
    right = not array[0] and not array[1] and not array[2]
    result = left == right
    return result

a = [
    [0,0,0],
    [0,0,1],
    [0,1,0],
    [0,1,1],
    [1,0,0],
    [1,0,1],
    [1,1,0],
    [1,1,1],]
print (len(a))

for i in range(len(a)):
    #print (a[i])
    if checkPredicate(a[i]):
        print(f'Для значений X:{a[i][0]} Y:{a[i][1]} Z:{a[i][2]} Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ИСТИННО')
    else:
        print(f'Для значений X:{a[i][0]} Y:{a[i][1]} Z:{a[i][2]} Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ЛОЖНО')

exit()

statement = inputNumbers(3)

if checkPredicate(statement):
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")
