def smash(words):
    resultado = ""

    for i, word in enumerate(words):
        if i == 0: 
            resultado += word
        else:
            resultado += " " + word
       
    return resultado