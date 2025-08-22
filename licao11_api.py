# import requests

# cidade=input("qual sua cidade?")
# url=f"https://wttr.in/{cidade}?format=j1"
# resposta= requests.get(url)

# if resposta.status_code == 200:
#     print("ok, 200")
#     dados= resposta.json()
#     temperatura= dados["current_condition"]
#     print(temperatura[(0)]["temp_C"])
# elif resposta.status_code == 400:
#     print("nao, 400 bro")
    
# else:
#     print("mermao num sei oq vc procurou mas n achei n")import requests

import requests

url=f"https://randomuser.me/api/"
resposta= requests.get(url)

if resposta.status_code == 200:
    print("ok, 200")
    dados= resposta.json()
    resultado=dados["results"]
    b=resultado[(0)]["name"] ["first"] 
    c=resultado[(0)]["name"] ["last"]
    print (f"{b} {c}")

    
elif resposta.status_code == 400:
    print("nao, 400 bro")
    
else:
    print("mermao num sei oq vc procurou mas n achei n")