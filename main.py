from clases.areas import CalculadoraAreas
if __name__ == "__main__":
    calc = CalculadoraAreas()
    rect = calc.area_rectangulo(5, 10)
    tri = calc.area_triangulo(8, 7)
print("Área del rectángulo :"+ str(rect))
print("Área del triángulo :"+str(tri) )
