class Agenda:
    def __init__(self):
        self.contactos = []
        self.freno = 0
        while self.freno != 5:
            try:
                self.freno = int(input("""1- Añadir contacto.\n2- Listar contactos.\n3- Buscar contacto.\n4- Editar contacto.\n5- Cerrar agenda.\n\nElija una opción: """))
            except ValueError:
                print("Ingresá un número, no una letra!!\n")

            if self.freno == 1:
                self.agregar_contacto(Contacto())
                print("\nContacto agregado!\n")
            elif self.freno == 2:
                self.listar_contactos()
            elif self.freno == 3:
                nombreContacto = input("Ingrese el nombre a buscar: ").upper()
                self.buscar_contacto(nombreContacto)
            elif self.freno == 4:
                contacto = input("Ingrese el contacto a editar: ").upper()
                self.editar_contacto(contacto)
            elif self.freno == 5:
                self.cerrar_agenda()
            else:
                print("Ingrese un número del 1 al 5.")

    def agregar_contacto(self,contacto):
        self.contactos.append(contacto)

    def listar_contactos(self):
        n = 1
        if len(self.contactos) == 0:
            print(f"No hay contactos guardados.")
        else:
            for x in self.contactos:
                print(f"Contacto Nº{n}: Nombre: {x.nombre}, teléfono: {x.telefono}, E-mail: {x.email}.")
                n +=1
        print("")

    def buscar_contacto(self,contacto):
        vacio = 0
        for x in self.contactos:
            if contacto == x.nombre:
                print(f"""Nombre: {x.nombre}; Teléfono {x.telefono}; Email: {x.email};""")
                vacio = 1
        if vacio == 0:
            print(f"Ese contacto no está en la agenda.")
        print("")
        
    
    def editar_contacto(self,contacto):
        vacio = 0
        for x in self.contactos:
            if contacto == x.nombre:
                x.nombre = input("Ingrese el nuevo nombre del contacto: ").upper()
                x.telefono = input("Ingrese el nuevo teléfono del contacto: ").upper()
                x.email = input("Ingrese el nuevo email del contacto: ").upper()
                vacio = 1
                print("Contacto editado!!")
        if vacio == 0:
            print(f"Ese contacto no está en la agenda.")
        print("")

    def cerrar_agenda(self):
        print("Gracias, ¡¡Vuelvas prontos!!")
        self.freno = 5


class Contacto:
    def __init__(self):
        self.nombre = input(f"Ingrese el nombre del contacto: ").upper()
        self.telefono = input(f"Ingrese el teléfono del contacto: ").upper()
        self.email = input(f"Ingrese el email del contacto: ").upper()

agendita = Agenda()