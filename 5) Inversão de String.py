#Escreva um programa que inverta os caracteres de um string.

#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

def inverter_string(s):
    resultado = ""
    for char in s:
        resultado = char + resultado
    return resultado

string = input("Informe uma string: ")
print(f"String invertida: {inverter_string(string)}")