from django.shortcuts import render


# Create your views here.

def calc(request, first: int, mark, second):
    result = "none"
    if mark == "+":
        result = first + second
    elif mark == "-":
        result = first - second
    elif mark == "*":
        result = first * second
    elif mark == "%" and second == 0:
        result = "∞"
    elif mark == '%':
        result = float(first)/float(second)
        print(result)
    else:
        result = "Go read documentation!"
    return render(request, 'calc.html', {"first": first, "mark": mark, "second": second, "result": result})
