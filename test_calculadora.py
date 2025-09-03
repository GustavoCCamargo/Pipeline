from calculadora import somar, dividir, subtrair, multiplicar

def test_somar():
    assert somar(5,5) == 10
    
def test_subtrair():
    assert subtrair(10, 5)== 5

def test_dividir():
    assert subtrair(4, 2) == 2

def test_multiplicar():
    assert multiplicar(5, 6) ==30