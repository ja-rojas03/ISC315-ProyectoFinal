import schemeParser
import math
import views
import reglas

def calcularGrasaCorporal(sexo, peso, edad, altura, tmb, window  ):

    IMC = (int)(float(peso))/((int)(int(altura)/100)^2)
    mult1 = "(* 1.20 " + str(IMC) + ")"
    mult2 = "(* 0.23 " + str(edad) + ")"
    if (sexo == "Masculino"):
        mult3 = "(* 10.8 1)"
    else:
        mult3 = "(* 10.8 0)"

    sum = "(+ " + mult1 + " " + mult2 + ")"
    actualSum = schemeParser.evaluate(sum)
    grasaCorporal = "(- (- " + str(actualSum) + " " + mult3 +") 5.4)"
    value = schemeParser.evaluate(grasaCorporal)
    calories = calcularCaloriasDiarias(sexo, peso, altura, edad, tmb)
    recetas = reglas.getRecetas()
    values = {}
    values['less_calories'] = []
    values['same_calories'] = []
    values['more_calories'] = []

    for key in recetas:
        if float(recetas[key]) < calories:
            values['less_calories'].append(key)
        if float(recetas[key]) == calories:
            values['same_calories'].append(key) 
        if float(recetas[key]) > calories:
            values['more_calories'].append(key) 

    values['fat'] = value
    values['calories'] = calories


    views.printToScreen(values, 'Grasa Corporal', 14, window)


def calcularCaloriasDiarias(sexo,peso, altura, edad, tmb):

    if (sexo == "Masculino"):
        mult1 = "(* 13.7 " + str(peso) + ")"
        mult2 = "(* 5 " + str(altura) + ")"
        mult3 = "(* 6.75 " + str(edad) + ")"
        suma = "(+ 66 " + mult1 + ") "
        sum2 = "(+ " + mult2 + " " + mult3 + ")"
        totalSum = "(+" + suma + " " + str(sum2) + ")"
    else:
        mult1 = "(* 9.6 " + str(peso) + ")"
        mult2 = "(* 1.8 " + str(altura) + ")"
        mult3 = "(* 4.7 " + str(edad) + ")"
        suma = "(+ 665 " + mult1 + ") "
        sum2 = "(+ " + mult2 + " " + mult3 + ")"
        totalSum = "(+" + suma + " " + sum2 + ")"

    resSum = schemeParser.evaluate(totalSum)
    print(resSum)
    result = "(* " + tmb + " " + str(resSum) + ")"
    calories = schemeParser.evaluate(result)
    return calories
