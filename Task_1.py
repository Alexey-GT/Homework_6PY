#Задача№1
#Программа которая вычисляет арифметическое выражение заданной строкой

ln_in = input("Введите выражение: ").split()

def aka_eval(args):
    while len(args) != 1:

        while '*' in args or '/' in args:
            try:
                mult_index = args.index('*')
            except:
                mult_index = 100
            try:
                div_index = args.index('/')
            except:
                div_index = 100
            
            if mult_index < div_index:
                args[mult_index - 1] = int(args[mult_index - 1]) * int(args[mult_index + 1])
                args.pop(mult_index + 1)
                args.pop(mult_index)
            else:
                args[div_index - 1] = int(args[div_index - 1]) / int(args[div_index + 1])
                args.pop(div_index + 1)
                args.pop(div_index)

        while '+' in args or '-' in args:
            try:
                sum_index = args.index('+')
            except:
                sum_index = 100
            try:
                deg_index = args.index('-')
            except:
                deg_index = 100
            
            if sum_index < deg_index:
                args[sum_index - 1] = int(args[sum_index - 1]) + int(args[sum_index + 1])
                args.pop(sum_index + 1)
                args.pop(sum_index)
            else:
                args[deg_index - 1] = int(args[deg_index - 1]) - int(args[deg_index + 1])
                args.pop(deg_index + 1)
                args.pop(deg_index)
    #print(args[0])
    return args[0]
     

#__________Вычисляем выражения в скобках____

while '(' in ln_in: # проверяем пока есть скобки
    sk_zak = ln_in.index(')') # Находим первую закрывающуюся скобку
    for i in range(sk_zak): 
        if ln_in[i] == '(': #ищем последнюю открывающуюся скобку
            sk_otk = i

    v_ln_in = ln_in[sk_otk + 1:sk_zak]; # выделяем список в скобках
    #print(v_ln_in)
    number = aka_eval(v_ln_in) # вычисляем выражение в скобках
    #print(number)
    ln_in[sk_otk:sk_zak + 1] = str(number)# полученное число  вставляем в список
    #print(ln_in)
aka_eval(ln_in)

print(f'Результат вычисления: {ln_in[0]}')

