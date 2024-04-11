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