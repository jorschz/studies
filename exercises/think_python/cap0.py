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

# Variaves globais: Apenas imutaveis
pi = 3.14

# Substituição do input para testes automáticos. Não use apenas input() para não redefinir a função built-in
def simulated_input(prompt):
    #print(prompt, end='')  # Mostra o prompt
    # Respostas fixas para teste
    reply = {
        "Hora de inicio (0-11): ": "15",
        "Duração em horas: ": "3"
    }
    #print(reply)  # Mostra a resposta simulada
    return reply.get(prompt, "0")  # Retorna como se tivesse sido digitado (Para um dicionario é necesario ter o .get)

# Função sem parameter
def lista_operacoes(a, b, c, d, e, f):
    """Cria e retorna uma lista de tuplas (descrição, resultado).""" #docstring
    lista = [ #Lista de tuplas
        (f"{a} + {b}", abs(a + b)),          # Soma e abs
        (f"{c} / {d}", round(c / d)),        # Divisão com round
        (f"{e} // {f}", e // f),             # Divisão inteira
        (f"{b} ** {e}", float(b ** e)),      # Potencia convertida para float
        
        ("12 + 5 * 6", 12 + 5 * 6),          # Ordem das operaçõeses sem parenteses
        ("(12 + 5) * 6", (12 + 5) * 6),      # Ordem das operações com parenteses
        
        (f"({a} * {e} / {c})", round(abs((a*e)/c), 2)), # abs e round com duas casas
        
        (f"√{pi}", math.sqrt(pi)), # Usando math
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
    return end

#Boolean com chained e Nested conditionals
def hora_chegada(hora):
    if hora < 4:
        return "Eu não vou estar atrasado"
    elif 4  <= hora <= 6:
        if hora < 5:
            return "Eu vou precisar correr"
        else:
            return "Eu vou precisar pegar um uber"
    else:
        return "Melhor nem ir"

#Função recursiva
def fibonacci(n):
    """Calcula o n-ésimo número da sequência de Fibonacci."""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Função de entrada
def main():

    print("Lista de calculos" + " para estudo") # String com +concatenação
    ##function call de um (function())
    operacoes = lista_operacoes(-30, 12, 43, 8, 6, 7 )
    imprimir_operacoes(operacoes)
    
    print(f"fibonacci: {fibonacci(7)}")
    
    fim = "fim " * 5 # String com *concatenação
    print(fim, f"\nAcima tem: {len(fim)} caracteres e o tipo é {type(fim)}") # Len e type function chamando uma variavel

    #function call com (parameters) e input de usuario~. Convertendo para int
    start = int(simulated_input("Hora de inicio (0-11): "))
    duration = int(simulated_input("Duração em horas: "))        
    end_evento = clock_arithmetic(start, duration)
    
    print(f"Se o evento começa às {start} e tem duração de {duration} horas, então acaba às {end_evento}...")
    mensagem = hora_chegada(end_evento)
    print(mensagem)
    
    

if __name__ == "__main__":
    main()


"""
Dicas de refatoração:
- Evitar variaveis globais mutaveis
- Separar lógica de apresentação e facil debugg
- Usar um dicionario de mensagens (encapsulação de regras) para condicionais
- Deixar o `main()` limpo
"""