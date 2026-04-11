def correct(s):
    resultado = ""
    for char in s:
        if char == "5":
            resultado += "S"
        elif char == "0":
            resultado += "O"
        elif char == "1":
            resultado += "I"
        else:
            resultado += char
    return resultado


assert correct("L0ND0N") == "LONDON"
assert correct("DUBL1N") == "DUBLIN"
assert correct("51NGAP0RE") == "SINGAPORE"
assert correct("BUDAPE5T") == "BUDAPEST"
assert correct("PAR15") == "PARIS"
print("All pass")
