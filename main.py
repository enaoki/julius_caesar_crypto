from api import API as API
import os, json, hashlib


class Example:
    """ Julious Caesar's cryptography (AceleraDev's challenge)
        https://www.codenation.dev/aceleradev/python-online-4/challenge/dev-ps

        - "substituição da letra do alfabeto avançado um determinado número de casas"
        - As mensagens serão convertidas para minúsculas tanto para a criptografia quanto para descriptografia.
        - No nosso caso os números e pontos serão mantidos

        O primeiro passo é você salvar o conteúdo do JSON em um arquivo com o nome answer.json, que irá usar no restante do desafio.

        Você deve usar o número de casas para decifrar o texto e atualizar o arquivo JSON, no campo decifrado.
        O próximo passo é gerar um resumo criptográfico do texto decifrado usando o algoritmo sha1 e atualizar novamente o arquivo JSON.
        OBS: você pode usar qualquer biblioteca de criptografia da sua linguagem de programação favorita para gerar o resumo sha1 do texto decifrado

        API espera um arquivo sendo enviado como multipart/form-data, como se fosse enviado por um formulário HTML, com um campo do tipo file com o nome answer. Considere isso ao enviar o arquivo.
    """
    @staticmethod
    def static_init() -> None:
        return API.static_init()

    @staticmethod
    def get_data() -> str:
        return API.get_data()


file_full_path = "answer.json"

Example.static_init()

if os.stat(file_full_path).st_size == 0:

    print("carregando dados via api...")

    data = Example.get_data()

    with open(file_full_path, "a" if os.path.exists(file_full_path) else "x") as out_file:
        json.dump(data, out_file)

with open(file_full_path) as json_file:
    d = json.load(json_file)

cifrado = d['cifrado']
numero_casas = d['numero_casas']
decifrado = ''
start = 97

for elem in cifrado:
    # decode only a to z char
    if not 97 <= ord(elem) <= 122:
        decifrado += elem
        continue

    start = ord(elem) if ord(elem) - numero_casas >= 97 else 123 - (97 - ord(elem))
    
    decifrado += chr(start - numero_casas)

print('Decifrado via console "{0}"'.format(decifrado))

print('Decifrado via JSON {0}'.format(d['decifrado']))

d['decifrado'] = decifrado

resumo_criptografico = hashlib.sha1(decifrado.encode()) 

d['resumo_criptografico'] = resumo_criptografico.hexdigest()

with open(file_full_path, "w")  as out_file:
    json.dump(d, out_file)

result = API.send_file('answer', 'answer.json', file_full_path)

print(result)