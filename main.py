import requests as consulta

#https://restcountries.com/
#Busque una informacion de un pais buscado por su nombre en ingles
#implementar MVC
nombre= input("Introduzca el pais al que desea acceder: ")
url = f'https://restcountries.com/v3.1/name/{nombre}'
response = consulta.get(url)
respuesta = response.json()
diccionario= respuesta[0]
print("Nombre del país: ",diccionario['name']['common'])
print("Capital: ",diccionario['capital'])
print("Moneda: ",list(diccionario['currencies'].values())[0]['name'])#Buscar aqui como acceder solo al nombre
print("Continente: ",diccionario['continents'])

