import requests
import json

url = 'https://www.4devs.com.br/ferramentas_online.php'
header = {
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.4devs.com.br',
    'referer': 'https://www.4devs.com.br/gerador_de_pessoas',
}
data = 'acao=gerar_pessoa&sexo=I&pontuacao=S&idade=0&cep_estado=&txt_qtde=1&cep_cidade='
solicitacao = requests.post(url, headers=header, data=data).json()

# Convertendo 'solicitação' para uma String json
dadosBrutos = json.dumps(solicitacao)
# removendo os caracteres "[" e "]" para transformar cada item em um objeto json e não todos em uma única lista
dadosBrutos = dadosBrutos.replace("[", "")
dadosBrutos = dadosBrutos.replace("]", "")
# retornando para json
dadosPessoa = json.loads(dadosBrutos)

# Agora cada item pode ser acessado usando a chave referente ao valor
print(dadosPessoa['nome'])
print(dadosPessoa['cpf'])
