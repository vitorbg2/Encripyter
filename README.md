# Encripyter, biblioteca Encripy.py


Biblioteca capaz de criptografar texto utilizando rotação iterativa,
combinada com rotação baseada em um hash da palavra-passe.

A palavra passe pode e deve ser alterada na biblioteca.

Existe uma função para criptografar e outra para descriptografar.

Existe ainda funções para caso queira utilizar como entrada/saída um arquivo de texto.

função encript: recebe o texto a ser criptografado como parâmetro e retorna o texto já cifrado.

função decript: recebe o texto criptografado como parâmetro e retorna o texto descriptografado.

OBS: UM TEXTO CRIPTOGRAFADO COM UMA PALAVRA-PASSE SÓ PODE SER DESCRIPTOGRAFADO COM A UTILIZAÇÃO DA MESMA PALAVRA-PASSE NO ESCOPO DA BIBLIOTECA.


Exemplos de uso:

from Encripy import Cripty #Importando biblioteca

cript = Cripty() #Instanciando a classe

text = cript.encript("Cryptography this text") #Criptografando o texto e gravando na variável 'text'

print(text) #Exibindo o texto criptografado

print(cript.decript(text)) #Exibindo o resultado do decript na tela