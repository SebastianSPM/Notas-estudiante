#Su uso es para limpiar la consola cuando se ejecuta
import os

os.system('cls' if os.name == 'nt' else 'clear')


#Declaracion de variables
grades = []
highest = 0
comparison_value = 0.0
flag = True
keep_running = True

while keep_running:
    print("\n", 6*"*", " SISTEMA DE CALIFICACIONES PARA CALCULAR PROMEDIO ", 6*"*")# Menu de entrada
    
    while flag:
        try:   #Ingresando calificacion
            grade = float(input(f"\nINGRESA LA CALIFICACIÓN (0-100) PARA SABER SI APROBO O REPROBO: "))

            if 0 <= grade <= 100: #Verificacion de promedio si aprueba o no
                if grade >= 60:
                    print("\nAPROBASTE")
                else:
                    print("\nREPROBASTE")
                flag = False
            else:
                print("\n¡LA CALIFICACIÓN DEBE ESTAR ENTRE UN RANGO 0 Y 100!")

        except ValueError:
            print("\nINGRESA UN VALOR NUMÉRICO")

    flag = True
    if grade >= 0:#Condicion se cumple si el usuario ingreso un dato en el anterior bloque de codigo
        while flag:
            try:
                grades_str = input("\nIngrese calificaciones separadas por comas: ").strip() #Tiene que ingresar numeros y se les quita los espacios
                grades = [float(i) for i in grades_str.split(",") if float(i) > 0]
                """
                Tenemos un operador ternario aqui para guardar cada valor que el usuario ingrese, separado por coma, se covierte a flotante y se compara
                si ese dato es mayor a 0
                """


                if len(grades) > 0: #Se comprueba si la variable tiene un valor mayor a 0
                    average = sum(grades) / len(grades)
                    print(f"\nPromedio: {average:.2f}")
                else:
                    print("\nNo se ingresaron calificaciones.")

                flag = False
            except ValueError:
                print("\nIngresa calificaciones válidas(NUMEROS), separadas por comas:")

    flag = True
    if average > 0:
        while flag:
            try:
                comparison_value = float(input("\nIngrese un valor para comparar cuales son mayores: ")) #Le pedimos al usuario el valor a comparar
                if comparison_value <= 0 or comparison_value > 100: #si comparacion esta en el rango no podra continuar y se repite
                    print("\nEl valor debe ser mayor a 0 y menor 101.")
                    continue
                flag = False
                
            except ValueError:
                print("\nEntrada inválida. Ingrese un número.")

        if len(grades) > 0:
            count = 0
            for i in grades: #comparamos si algun valor de la lisa es mayor al valor a comparar
                if i > comparison_value:
                    count += 1

            if count > 0:#Condicion para mostrar el resultado solo si contador tiene algo, sino sera 0
                print(f"\nCalificaciones mayores que {comparison_value}: {count}")
            else:
                print(f"\nNinguna calificación mayor a {comparison_value}")
        else:
            print("\nNo hay calificaciones para comparar.")


    flag = True
    if average > 0:
        while flag:
            try:
                specific_grade = float(input("\nIngrese una calificación específica para verificar cuántas veces aparece: "))  # Verificar si aparece varias veces

                if len(grades) == 0:
                    print("\nNo hay calificaciones para buscar.")
                    flag = False

                if specific_grade <= 0 or specific_grade > 100:
                    print("\nLa calificación específica debe ser mayor a 0 y menor 101")
                    continue

                count = 0
                for i in grades:
                    if i == specific_grade:  # Comparando si es exactamente igual al valor dentro
                        count += 1

                if count > 0:
                     print(f"\nLa calificación {specific_grade} aparece {count} veces.")  # Mostrando resultado si contador tiene algo
                else:
                    print("\nNo aparece la calificación ingresada.")

                flag = False  # solo salimos si todo fue correcto

            except ValueError:
                print("\nEntrada inválida. Ingrese un número.")

    if True: #Salida del programa o si se quiere volver a entrar
        exit_program = input("\n¿Quieres salir del programa? (s/n): ")
        if exit_program.lower() == 's' or exit_program.lower() == "si":
            keep_running = False
