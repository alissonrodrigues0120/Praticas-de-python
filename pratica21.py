print("cadastramento:")

usuario=input("usuario: ")

senha=input("senha: ")


print("autenticação:")

usuario2=input("usuario: ")
senha2=input("senha: ")
print('\n'[1:])
if (hash(usuario2)==hash(usuario)) and (hash(senha2)==hash(senha)):
      print("true")
else:
    print("false")