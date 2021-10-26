from django.shortcuts import render


# Create your views here.

def calc(request, first, do, second):
    if do == '%' and second == 0:
        res = 'error: you can not divide by zero'
    elif do == '*':
        print(first * second)
        res = first * second
    elif do == '%':
        print(first / second)
        res = first / second

    elif do == '+':
        print(first + second)
        res = first + second

    elif do == '-':
        print(first - second)
        res = first - second
    else:
        res = 'error: invalid operator'

    return render(request, 'calculator.html', {'first': first, 'do': do, 'second': second, 'result': res})
