print("Act 9 clase humano")
print("Paola Torres Mat: 22308051281109")
#Zona de clases
class Humano1109:
    #Zona de atributos
    nombre = "Pao"
    cumple = "28 de enero"
    hobbie = "Escuchar musica"
    persfav = "Tinkerbell"


    #Zona de funciones dentro de la clase
    def pintar1109(self,n):
        print(f"{n} pinto un dibujo")
    def dormir1109(self,n):
        print(f"{n} se durmio")
    def bailar1109(self,n):
        print(f"{n} esta bailando")

#Zona de creacion de objetos
pao = Humano1109()
leo = Humano1109()

#Zona de usando objetos
print("")
print("Resultados para Pao")
print(f"Nombre : {pao.nombre}")
print(f"Cumple : {pao.cumple}")
print(f"Hobbie : {pao.hobbie}")
print(f"Personaje favorito ¿ : {pao.persfav}")
pao.pintar1109("Pao")
pao.dormir1109("Pao")
pao.bailar1109("Pao")


print("")
print ("Resultados para Leo")
leo.nombre = "Leo"
leo.cumple = "11 de junio"
leo.hobbie = "Dibujar"
leo.persfav = "Spider - Man"
print(f"Nombre : {leo.nombre}")
print(f"Cumple : {leo.cumple}")
print(f"Hobbie : {leo.hobbie}")
print(f"Personaje favorito ¿ : {leo.persfav}")
leo.pintar1109("Leo")
leo.dormir1109("Leo")
leo.bailar1109("Leo")
