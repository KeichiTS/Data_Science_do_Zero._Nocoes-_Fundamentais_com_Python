# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 17:28:21 2024

@author: KeichiTS
"""

users = [
        {'id' : 0, 'name': 'Hero'},
        {'id' : 1, 'name': 'Dunn'},
        {'id' : 2, 'name': 'Sue'},
        {'id' : 3, 'name': 'Chi'},
        {'id' : 4, 'name': 'Thor'},
        {'id' : 5, 'name': 'Clive'},
        {'id' : 6, 'name': 'Hicks'},
        {'id' : 7, 'name': 'Devin'},
        {'id' : 8, 'name': 'Kate'},
        {'id' : 9, 'name': 'Klein'},
        ]

friendship_pairs= [(0,1), (0,2), (1,2), (1,3), (2,3), (3,4),
                   (4,5), (5,6), (5,7), (6,8), (7,8), (8,9)]

#Inicialize o dict com uma lista vazia para cada id do usuário:
friendships = {users['id'] : [] for users in users}

#Em seguida, execute um loop pelos pares de amigos para preenchê-la:
for i, j in friendship_pairs:
    friendships[i].append(j) #adiciona j como amigo do usuário i
    friendships[j].append(i) #adiciona i como amigo do usuário j


#Função que calcula o total de conexões de um usuário
def number_of_friends(user):
    "Quantos amigos tem o user_?"
    user_id = user['id']
    friends_ids = friendships[user_id]
    return len(friends_ids)
    
#Calcula a soma de conexões de todos os usuários
total_connections = sum(number_of_friends(user) for user in users) #24

#Calculando o número médio de conexões:
num_users = len(users) #Tamanho da lista de usuários
avg_connections = total_connections/num_users # 24 / 10= 2.4

#Colocando em ordem decrescente dos que tem "mais amigos" para os que tem "menos amigos":

#Crie uma lista (user_id,number_of_friends)
num_friends_by_id = [(user['id'], number_of_friends(user)) for user in users]

#Classifica a lista de maior para menor
num_friends_by_id.sort(key = lambda id_and_friends: id_and_friends[1], reverse = True)


#Código para iterar os amigos e coletar os amigos dos amigos
def foaf_id_bad(user):
    """foaf significa "friend of a friend" """
    return[foaf_id for friend_id in friendships[user['id']]
                   for foaf_id in friendships[friend_id]
          ]

foaf_var = foaf_id_bad(users[0]) #amigos de amigos de Hero [0, 2, 3, 0, 1, 3]

#Criando a contagem de amigos em comum, porém excluindo as pessoas que o usuário já conhece 

from collections import Counter 

def friend_of_friends(user):
    user_id = user['id']
    return Counter(foaf_id 
                   for friend_id in friendships[user_id]     #Para cada amigo meu,
                   for foaf_id in friendships[friend_id]     #encontree um amigo deles
                   if foaf_id != user_id                     #que não sejam eu
                   and foaf_id not in friendships[user_id]   #e não sejam meus amigos. 
        )

#print(friend_of_friends(users[3]))   #Counter({0: 2, 5: 1}) - 2 amigos em comum com Hero e 1 com Clive


#lista de interesses dos usuários 

interests = [
    (0, 'Hadoop'), (0, 'Big Data'), (0, 'HBase'), (0, 'Java'), (0, 'Spark'), (0, 'Storm'), (0, 'Cassandra'),
    (1, 'NoSQL'), (1, 'MongoBD'), (1, 'Cassandra'), (1, 'HBase'), (1, 'Postgres'),
    (2, 'Pytho'), (2, 'scikit-learn'), (2, 'scipy'), (2, 'numpy'), (2,'statsmodels'), (2, 'pandas'),
    (3, 'R'), (3, 'Python'), (3, 'statistics'), (3,'regression'), (3,'probability'), 
    (4, 'machine learning'), (4, 'regression'), (4, 'deision trees'), (4, 'libsvm'),
    (5, 'Python'), (5, 'R'), (5, 'Java'), (5, 'C++'), (5, 'Haskell'), (5, 'programing languages'),
    (6, 'statistics'), (6, 'probability'), (6,'mathematics'), (6, 'theory'), 
    (7, 'machine learning'), (7, 'scikit-learn'), (7, 'Maheout'), (7, 'neural networks'), 
    (8, 'neural networks'), (8, 'deep learning'), (8, 'Big Data'), (8, 'artificial intelligence'),
    (9, 'Hadoop'), (9, 'Java'), (9, 'MapReduce'), (9, 'Big Data')
    ]

#Construindo uma função para encontrar usuários com os mesmos interesses:
    
def data_scientists_who_like(target_interest):
    """Encontre os ids dos usuários cm o mesmo interesse"""
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest
            ]

print(data_scientists_who_like('Hadoop')) #[0, 9] - o usuário 0 e o 9 se interessam por Hadoop

#Construindo um índice para usuários:
from collections import defaultdict

#As chaves são interesses, os valores são listas de user_ids com o interesse em questão 
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

#Agora de usuário para interesses

#As chaves são user_ids, os valores são listas de interesses do user_id em questão
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)
    
