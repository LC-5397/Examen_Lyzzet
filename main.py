from clases.areas import CalculadoraAreas
if __name__ == "__main__":
    calc = CalculadoraAreas()
    rect = calc.area_rectangulo(5, 10)
    tri = calc.area_triangulo(8, 7)
    
    calc = CalculadoraAreas()
    radio = float(input("Ingrese el radio del círculo: "))

    area = calc.area_circulos(radio)

   
    print("Área del rectángulo :"+ str(rect))
    print("Área del triángulo :"+str(tri) )
    print("El área del círculo con radio "+str(radio)+" es= "+ str(area))
   