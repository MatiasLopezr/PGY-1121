cont_niño = 0
acum_niño = 0

cont_joven = 0
acum_joven = 0

cont_adulto = 0
acum_adulto = 0
sw = 0
while sw == 0:
    print("Cine Moro")
    print("---------------")
    print("lista de opciones")
    print("1.- entrada Niño = $5500")
    print("2.- entrada Joven = $7000 ")
    print("3.- entrada adulto = $9000")
    print("4.- salir")
    print("5.- generar ventas totales")
    try:
        op=int(input("escoga la opcion que desea: "))
        if op == 1:
            edad = int(input("ingrese edad:"))
            if edad >= 1 and edad <=13:
                ent_niño = int(input("ingrese la cantidad de entradas que desea: "))
                cont_niño = ent_niño
                acum_niño = cont_niño * 5500
                print('categoria = "Niño"')
                print(f"cantidad de entradas = {ent_niño}  ")
                print(f"Total, a pagar ={acum_niño} ")
                print("gracias por su compra, disfrute la funcion")
        elif op == 2:
            edad = int(input("ingrese edad:"))
            if edad >= 14 and edad <=21:
                ent_joven = int(input("ingrese la cantidad de entradas que desea: "))
                cont_joven = ent_joven
                acum_joven = cont_joven * 7000
                print('categoria = "joven"')
                print(f"cantidad de entradas = {ent_joven} ")
                print(f"Total, a pagar = {acum_joven} ")
                print("gracias por su compra, disfrute la funcion")
        elif op == 3:
            edad= int(input("ingrese edad:"))
            if edad>= 22:
                ent_adulto = int(input("ingrese la cantidad de entradas que desea: "))
                cont_adulto = ent_adulto
                acum_adulto = cont_adulto * 9000
                print('categoria = "adulto"')
                print(f"cantidad de entradas = {ent_adulto}   ")
                print(f"Total, a pagar = {acum_adulto} ")
                print("gracias por su compra, disfrute la funcion")
        elif op == 4:
            sw = 1

        elif op == 5:
            cantidad_entradas = cont_niño+cont_joven+cont_adulto
            total_ventas = acum_niño+acum_adulto+acum_joven
            print("Categoria niño")
            print("------------------")
            print(f"entradas vendidas de niños = {cont_niño}") 
            print(f"monto vendido de entradas para niños = {acum_niño}")
            print()
            print("Categoria joven")
            print("------------------")
            print(f"entradas vendidas de jovenes = {cont_joven}")
            print(f"monto reacudado de entradas joven = {acum_joven}")
            print()
            print("Categoria adulto")
            print("------------------")
            print(f"entradas vendidas de adulto = {cont_adulto}")
            print(f"monto reacudado de entradas adulto= {acum_adulto}")
            print()
            print(f"ventas totales de entrada = {cont_niño + cont_joven + cont_adulto}")
            print(f"total de monto recaudado = {acum_adulto + acum_joven+ acum_niño}")
            porcentaje = (cantidad_entradas / total_ventas) * 100
            print(f"Porcentaje de ventas: {porcentaje}")


    

    except:
        print("opcion invalida")