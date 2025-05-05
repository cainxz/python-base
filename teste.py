#!/usr/bin/env python3
"""
hello world multi linguas

dependendo da lingua configurada no ambiente o programa exibe a mensagem correspondente.

como usar: 

tenha a variavel lang devidamente coonfigurada ex: 

    export LANG=pt_BR

Execução: 

  python3 hello.py
  ou
  ./hello.py
"""
__version__ = "0.0.1"
__author__= "kaio"
__license__= "Unlicense"

import os 


current_language = os.getenv("LANG")
msg = "Hello, world!" 

if current_language == "pt_BR":
    msg= "Olá, Mundo!" 

elif current_language == "it_IT":     
   msg= "Ciao, mondo!"




print(msg)
