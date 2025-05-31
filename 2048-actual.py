def modo_maquina():
    generar_tablero_inicial()
    tablero_inicial = copy.deepcopy(tablero)
    print("Configuración inicial:")
    mostrar_tablero(tablero_inicial)

    primero = random.choice(["Jugador", "Máquina"])
    segundo = "Máquina" if primero == "Jugador" else "Jugador"
    print(f"{primero} empieza.\n")

    if primero == "Jugador":
        mov1, mayor1 = jugar_turno(tablero_inicial, "Jugador")
        mov2, mayor2 = jugar_turno(tablero_inicial, "Máquina")
    else:
        mov1, mayor1 = jugar_turno(tablero_inicial, "Máquina")
        mov2, mayor2 = jugar_turno(tablero_inicial, "Jugador")

    print("\nResultados finales:")
    print(f"{primero} - movimientos: {mov1}, mayor: {mayor1}")
    print(f"{segundo} - movimientos: {mov2}, mayor: {mayor2}")

    if mayor1 > mayor2:
        print(f"¡{primero} gana!")
    elif mayor2 > mayor1:
        print(f"¡{segundo} gana!")
    else:
        if mov1 < mov2:
            print(f"¡{primero} gana por menos movimientos!")
        elif mov2 < mov1:
            print(f"¡{segundo} gana por menos movimientos!")
        else:
            print("¡Empate total!")

def manejar_modo(modo):
    if modo == 1:
        print("Modo Normal")
        modo_individual()
    elif modo == 2:
        print("Modo Jugador vs Jugador")
        modo_multijugador()
    elif modo == 3:
        print("Modo Jugador vs Máquina")
        modo_maquina() 