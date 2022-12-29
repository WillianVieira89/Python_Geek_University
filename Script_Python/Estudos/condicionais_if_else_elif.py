"""
Estruturas condicionais
if (Se), else (Se não), elif (Se, Se não)

elif não existe nem no C nem no Java.
No bloco podemos ter vários elif, mas apenas um if e um else.
"""

idade = 19
if idade < 18:
    print('Menor de idade')  # sempre usar indentação no bloco

elif idade == 18:
    print('Tem 18 anos')

else:
    print('Maior de idade')
