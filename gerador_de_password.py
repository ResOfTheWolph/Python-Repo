#    ___   ___  _____ __      __   |
#   | _ \ / _ \|_   _|\ \    / /   |   Rúben Cavaco
#   |   /| (_) | | |   \ \/\/ /    |   rcavaco@protonmail.ch
#   |_|_\ \___/  |_|    \_/\_/     |   https://github.com/ResOfTheWolph/
#                                  |


#   importação de Bibliotecas
#   importing Libraries
import random



#   secção responsável pela mixagem do string através da função DO
#   section responsible to mix all the string through the uso of the function DO
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)



#   secção principal do programa
#   main Section of the Program
uppercaseLetter1=chr(random.randint(65,90))
uppercaseLetter2=chr(random.randint(65,90))
uppercaseLetter3=chr(random.randint(65,90))
uppercaseLetter4=chr(random.randint(65,90))
uppercaseLetter5=chr(random.randint(65,90))
uppercaseLetter6=chr(random.randint(65,90))
uppercaseLetter7=chr(random.randint(65,90))
uppercaseLetter8=chr(random.randint(65,90))
uppercaseLetter9=chr(random.randint(65,90))
uppercaseLetter10=chr(random.randint(65,90))



#   gerar passwords usand todos os caracteres, em ordem aleatória
#   generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + uppercaseLetter4 + uppercaseLetter5 + uppercaseLetter6 + uppercaseLetter7 + uppercaseLetter8 + uppercaseLetter9 + uppercaseLetter10
password = shuffle(password)

#   escrita da Password gerada
#   writing of the generated password
print(password)