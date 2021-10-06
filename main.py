import requests
import json
    
def consultacep(cep):
    url = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    endereco = url.json()
    if url.status_code == 200:
        print("Conexão feita com sucesso")
        for keys in endereco:
            if keys == 'erro':
                print("Seu CEP é inválido.")
            else:
                print(f'{keys}: {url.json()[keys]}')  
    elif url.status_code == 400:
        print("Não foi possível conectar com o servidor. Verifique se o CEP está correto.")
   

cep_input = input("Diga-me o seu CEP que eu direi o seu endereço:\n")
consultacep(cep_input)
