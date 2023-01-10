"""
Módulo Collections - Default Dict

# Recap Dicionarios

dicionario = {'curso': 'Programação em Python Essencial'}
print(dicionario)
print(dicionario['curso'])
print(dicionario['outro'])  # ??? Key Error

Default Dict → Ao criar um dicionário utilizando-o, nos informamos um valor default,
podemos utilizar um lambda para isso. Este valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será
criada e o valor default será atribuido

OBS. Lambda são funções sem nome, que podem ou não receber parâmetros de entrada
e retornar valores.

"""

from collections import defaultdict
dicionario = defaultdict(lambda: 0)
dicionario['curso'] = 'Programação em Python: Essencial'
print(dicionario)
print(dicionario['outro'])  # Key Error no dicionário comum, mas no default dict retorna o valor indicado
print(dicionario)



