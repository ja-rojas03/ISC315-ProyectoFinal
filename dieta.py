import schemeParser
import math
import views

def calcularGrasaCorporal(sexo, peso, edad, altura, window ):

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
        value =schemeParser.evaluate(grasaCorporal)
        views.printToScreen(value, 'Grasa Corporal', 10, window)

# calcularGrasaCorporal("Masculino", 81.6466 ,22, 180 )
