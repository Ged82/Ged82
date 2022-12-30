# El ejercicio consiste en crear un programa que muestre por consola la carta de un restaurante
# donde añadiremos diferentes platos y después escogeremos que queramos para comer. Una
# vez hecha esto se tendrá que calcular el precio de la comida, el programa nos tiene que decir
# con qué billetes y monedas tenemos que pagar.


#Ejercicio pidiendo 2 coffee, 1 drinks y 3 donuts.
'''NOTA: para mostrar el ejemplo del producto que no aparece en el MENU hay que pedir "1 chocolate" y habilitar ["chcolate"] en la variable
confirmacion_lista_de_pedido.'''



#Monedas y billetes para pagar.

moneda1 = 0.5
moneda2 = 1
moneda3 = 2
billete1 = 5
billete2 = 10
billete3 = 20
billete4 = 50




# Menú del Restaurante.

print("MENU")
menu_fast_food = ("sandwich-----$2.50", "mexican tacos-----$1.50", "burger-----$2.50", "hot dog-----$2.50", "pizza-----$3.50", "chicken nuggets----$3.00",
"french fries  $2.00", "donuts-----$1.50", "drinks-----$1.50", "coffee----$1.50")

for n in menu_fast_food:
    print(n)



#Bienvenida y Solicitudes de pedido.

pedido_inicial = input("Buenas.¿Qué quiere ordenar?")

pedido_adicional = input("¿Desea algo más?")

print("Ya le traigo su pedido")



#Lista de pedido.
lista_de_pedido = ["2 coffee" + "1 drinks" + "3 donuts"]

confirmacion_lista_de_pedido =["coffee----$1.50","drinks-----$1.50","donuts-----$1.50"] #["chcolate"]

for n in confirmacion_lista_de_pedido:
    print(n in menu_fast_food)



# Precio de lista_de_pedido.

item1 = "coffee"
item2 = "drinks"
item3 = "donuts"


cantidad_item1 = 2
cantidad_item2 = 1
cantidad_item3 = 3


precio_item1 = 1.50
precio_item2 = 1.50
precio_item3 = 1.50


valor_a_pagar = ((cantidad_item1 * precio_item1) + (cantidad_item2 * precio_item2) + (cantidad_item3 * precio_item3))



x = (n in menu_fast_food)

if x == True:

     print("El valor total a pagar son  " + str(valor_a_pagar) + " euros")

else:
     print("El producto no existe")
