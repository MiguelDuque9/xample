import sys

name = input("Digite su primer nombre")
edad = int(input("Digite su edad"))

if edad >= 18:
  print("Usted cumple la edad para donar")

  ult_dona = (input("Ha pasado 3 meses despues de su ultima donación? Si/No"))
  ult_ciru = (input("Ha pasado 3 meses despues de su ultima cirugia? Si/No"))

  if ult_dona == "si" and ult_ciru == "si":
    print("Si puede donar")
  else:
    print("No puede donar")
    sys.exit()

  plaquetas = int(input("Digite la cantidad de plaquetas que arrojó su prueba"))

  if plaquetas > 200000:
    print(f"El/la paciente {name} con la edad de {edad} pudo donar y la cantidad de plaquetas que arrojó su prueba fue de {plaquetas} por tanto puede hacer transfusión")
  else:
    print(f"El/la paciente {name} con la edad de {edad} pudo donar y la cantidad de plaquetas que arrojó su prueba fue de {plaquetas} por tanto no puede hacer transfusión")

else:
  print("No pudo donar por no cumplir la edad requerida")

  "cambio de la nueva rama"