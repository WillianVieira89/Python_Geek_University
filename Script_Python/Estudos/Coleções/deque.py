"""
Módulo Collectrions - Deque

Podemos dizer que o deque é uma lista de alta performance.
"""

# Importa

from collections import deque

# Criando deques

deq = deque('geek')
print(deq)

# Adicionando elementos no deque

deq.append('y')  # Adiciona no final da lista
print(deq)

deq.appendleft('k')  # Adiciona no começo da lista
print(deq)

# Remover elementos
print(deq.pop())  # Remove e retorna o último elemento
print(deq)

print(deq.popleft())  # Remove e retorna o primeiro elemento
print(deq)