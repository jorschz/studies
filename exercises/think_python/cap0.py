# Import statements
import math

"""
Conceitos:
*Expression* = A collection of **operators** and numbers and has a **value**
*Statement* = is a unit of code that has an effect but no value. **evaluation** and **execution**
*Functions* = function head is: "def function_name(parameter):" and then the body that is a sequence of **statements**
*Arguments* = The **expression** in parenthesis in a function call de uma function com **parameters**
*Encasulation* = wrapping a piece of code up in a **function**
*Generalization* = Adding a **parameter** to a function
*Refactoring* = Improving the code without changing tis behavior
"""
# Substituição do input para testes automáticos
def input(prompt):
    #print(prompt, end='')  # Mostra o prompt
    # Respostas fixas para teste
    reply = {
        "Hora de inicio (0-11): ": "15",
        "Duração em horas: ": "3"
    }
    #print(reply)  # Mostra a resposta simulada
    return reply.get(prompt, "0")  # Retorna como se tivesse sido digitado (Para um dicionario é necesario ter o .get)

# Variaves globais
a, b, c, d, e, f = -30, 12, 43, 8, 6, 7 

# Função sem parameter
def lista_operacoes():
    """Cria e retorna uma lista de tuplas (descrição, resultado).""" #docstring
    lista = [ #Lista de tuplas
        (f"{a} + {b}", abs(a + b)),          # Soma e abs
        (f"{c} / {d}", round(c / d)),        # Divisão com round
        (f"{e} // {f}", e // f),             # Divisão inteira
        (f"{b} ** {e}", float(b ** e)),      # Potencia convertida para float
        
        ("12 + 5 * 6", 12 + 5 * 6),          # Ordem das operaçõeses sem parenteses
        ("(12 + 5) * 6", (12 + 5) * 6),      # Ordem das operações com parenteses
        
        (f"({a} * {e} / {c})", round(abs((a*e)/c), 2)), # abs e round com duas casas
        
        ("√π", math.sqrt(math.pi)), # Usando math
    ]
    return lista # Retorna a lista criada

# Função com parameter
def imprimir_operacoes(operacoes):
    """Imprime cada operação e seu resultado formatado."""
    for descricao, resultado in operacoes: # For loop que percorrer a lista de tuplas
        print(f"{descricao} = {resultado}") # Retorna um print

# Função generalizada
def clock_arithmetic(start, duration):
    """Calcula a hora de término de um evento usando aritmética modular."""
    end = (start + duration) % 12 # Modulus operator
    print(f"Se o evento começa as {start} e tem a duração de {duration} então ele acaba as {end}...")
    return end

#Função recursiva
def recursive():
    pass

# Função de entrada
def main():
    
    print("Lista de calculos" + " para estudo") # String com +concatenação
    
    ##function call de um (function())
    imprimir_operacoes(lista_operacoes())
    
    fim = "fim " * 5 # String com *concatenação
    print(fim, f"\nAcima tem: {len(fim)} caracteres e o tipo é {type(fim)}") # Len e type function chamando uma variavel

    #function call com (parameters) e input de usuario
    start, duration = int(input("Hora de inicio (0-11): ")), int(input("Duração em horas: ")) # Convertendo para int
    end_evento = clock_arithmetic(start, duration)
    
    #Boolean com chained e Nested conditionals
    if end_evento < 4:
        print("Eu não vou estar atrasado")
    elif 4 <= end_evento <= 6: #chained
        if end_evento < 5: #nested
            print("Eu vou precisar correr")
        else:
            print("Eu vou precisar pegar um uber")
    else:
        print("Melhor nem ir")

main()