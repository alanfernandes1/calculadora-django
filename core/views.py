from django.shortcuts import render

def calcular(request):
    resultado = None
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        operacao = request.POST['operacao']

        if operacao == 'soma':
            resultado = num1 + num2
        elif operacao == 'subtracao':
            resultado = num1 - num2
        elif operacao == 'multiplicacao':
            resultado = num1 * num2
        elif operacao == 'divisao':
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Erro: Divisão por zero!"
    return render(request, 'calculadora.html', {'resultado': resultado})
