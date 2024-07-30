import random

messages = ['certamente',
    'é definitivamente',
    'sim, com certeza',
    'essa é dificil, tente novamente',
    'pergunte novamente mais tarde',
    'concentre-se e tente novamente',
    'minha resposta é nao', 
    'muito duvidoso'
]

print(messages[random.randint(0, len(messages) - 1)])