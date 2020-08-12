import schemeParser
import math
import views

def calcularGrasaCorporal(sexo, peso, edad, altura, window, tmb ):

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
    views.printToScreen(value, 'Grasa Corporal', 10, window)


def calcularCaloriasDiarias(sexo,peso, altura, edad, tmb):

    if (sexo == "Masculino"):
        mult1 = "(* 13.7 " + str(peso) + ")"
        mult2 = "(* 5 " + str(altura) + ")"
        mult3 = "(* 6.75 " + str(edad) + ")"
        suma = "(+ 66 " + mult1 + " " + mult2 + " " + mult3 + ")" 
    else:
        mult1 = "(* 9.6 " + str(peso) + ")"
        mult2 = "(* 1.8 " + str(altura) + ")"
        mult3 = "(* 4.7 " + str(edad) + ")"
        suma = "(+ 665 " + mult1 + " " + mult2 + " " + mult3 + ")"

    result = "(* " + tmb + " " + suma + ")"
    calories = schemeParser.evaluate(result)
    return calories
