import string
import hashlib
from tkinter.filedialog import *


##Autor : Vitor Cunha

# Copyright 2018 Vitor Cunha
#
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class Cripty:
    alfa ='aAB1bCDEcFde2GfH3I4ghiJjk5lKmnoLMpN67OqrsPQtRS8uvwxTUVy9WXz0YZ'
    palavra_passe = b'123456789'
    hash_object = hashlib.md5(palavra_passe)
    hash_palavra = hash_object.hexdigest()

    chave = int(6) ##Número de movimentos no alfabeto 'alfa'. Deve ser positivo
    chave2 = int(3) ##Número de movimentos no alfabeto 'alfa'. Deve ser positivo
    chave3 = int(10) ##Número de movimentos no alfabeto 'alfa'. Deve ser positivo



    def encript(self,texto):
        i = 0
        hash = int(1)
        saida = ''
        for l in texto:
            if l in self.alfa:
                num = self.alfa.find(l) + self.alfa.find(self.hash_palavra[hash-1])
                print(num)

                if hash == 32:
                    hash = 1

                if i%3 == 0:
                    num = num + self.chave3
                elif i%2 == 0:
                    num = num + self.chave
                else:
                    num = num + self.chave2

                if num >= len(self.alfa):
                    num = num - len(self.alfa)
                elif num < 0:
                    num = num + len(self.alfa)

                saida = saida + self.alfa[num]

            else:
                saida = saida + l

            i = i + 1
            hash = hash + 1

        saida = saida[::-1]
        return saida


    def decript(self,texto):
        texto = texto[::-1]
        i = 0
        hash = int(1)
        saida = ''
        for l in texto:
            if l in self.alfa:
                num = self.alfa.find(l) - self.alfa.find(self.hash_palavra[hash-1])

                if hash == 32:
                    hash = 1

                if i%3 == 0:
                    num = num - self.chave3
                elif i%2 == 0:
                    num = num - self.chave
                else:
                    num = num - self.chave2


                if num >= len(self.alfa):
                    num = num - len(self.alfa)
                elif num < 0:
                    num = num + len(self.alfa)

                saida = saida + self.alfa[num]

            else:
                saida = saida + l

            i = i + 1
            hash = hash + 1

        return saida


    def encriptToTxt(self):
        janela = Tk()
        janela.withdraw()
        print('Selecione o arquivo para encripta-lo.....')
        print('BACKUP YOUR ARCHIVE BEFORE ENCRYPT')
        arqLer = askopenfilename(initialdir="C:/",
                              filetypes=(("Text File", "*.txt"),),
                              title="Selecione o arquivo para encriptação."
                              )

        try:
            arq = open(arqLer, 'r')
        except:
            print("Selecione uma pasta válida")
            sys.exit()

        texto = arq.read()
        saida = self.encript(texto)

        try:
            arq = open(arqLer, 'w')
        except:
            print("Erro ao abrir arquivo")
            sys.exit()

        arq.write(saida)
        arq.close()
        print("Arquivo encriptado com sucesso!")


    def decriptFromTxt(self):
        janela = Tk()
        janela.withdraw()
        print('Selecione o arquivo.....')
        print('BACKUP YOUR ARCHIVE BEFORE DECRYPT')
        arq = askopenfilename(initialdir="C:/",
                                filetypes=(("Text File", "*.txt"),),
                                title="Selecione o arquivo."
                                )

        try:
            arquivo = open(arq, 'r')
        except:
            print('Selecione um arquivo válido')
            sys.exit()

        texto = arquivo.read()

        try:
            arquivo = open(arq, 'w')
        except:
            print("Erro ao abrir arquivo")
            sys.exit()

        arquivo.write(self.decript(texto))
        arquivo.close()

        print("Arquivo decriptado com sucesso")