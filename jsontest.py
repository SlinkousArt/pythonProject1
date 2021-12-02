import json

import bcrypt
#
# # some json
# x = '{"name":"John", "age":"30", "city":"New York"}'
#
# # parse x:
# y = json.loads(x)
#
# # the result is a Python dictionary:
# print(y["age"])
#
# username = input('pick your username').lower()
#

# passwd = input('input your password')
#
# salt = bcrypt.gensalt()
# hashed = bcrypt.hashpw(passwd.encode('utf-8'), salt)
#
# print(salt)
# print(hashed)

#
# class user:
#     def __init__(self, name, hash):
#         self.name = username
#         self.hash = hashed
#
x =  '{ "name":"John", "age":30, "city":"New York"}'
info = json.loads(x)

file = open("test.txt", "w")
file.write(info["name"])
file.close()
