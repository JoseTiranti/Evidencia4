class MaquinaDeGrabados:
    def __init__(self, potencia_max, velocidad_grabado_max):
        self.potencia_max = potencia_max
        self.velocidad_grabado_max = velocidad_grabado_max
        self.__estado = False  # La máquina comienza apagada
        self.__material_grabado = 0  # No hay material al inicio

    # Representación en cadena
    def __str__(self):
        estado_actual = 'apagada' if not self.__estado else 'encendida'
        return (f"Máquina de Grabados [Potencia: {self.potencia_max}, "
                f"Velocidad: {self.velocidad_grabado_max}, Estado: {estado_actual}]")

    # Obtener el estado actual de la máquina
    def estado(self):
        return self.__estado

    # Encender la máquina
    def encender(self):
        if self.__estado:
            raise ValueError('La máquina ya está encendida!')
        self.__estado = True

    # Apagar la máquina
    def apagar(self):
        if not self.__estado:
            raise ValueError('La máquina ya está apagada!')
        self.__estado = False

    # Obtener la cantidad de material grabado
    @property
    def material_grabado(self):
        return self.__material_grabado

    # Agregar material para grabar
    def iniciar_grabado(self, cantidad_material):
        if not self.__estado:
            raise ValueError('La máquina debe estar encendida para grabar material.')

        if cantidad_material > self.potencia_max:
            raise ValueError('La cantidad de material excede la capacidad máxima de grabado!')

        if (self.__material_grabado + cantidad_material) > self.potencia_max:
            raise ValueError('No se puede grabar más material, se ha alcanzado la capacidad máxima.')

        self.__material_grabado += cantidad_material

    # Calcular el tiempo necesario para el grabado
    def tiempo_necesario_para_grabar(self):
        if not self.__material_grabado:
            raise ValueError("No hay material para grabar.")
        tiempo_procesado = (self.__material_grabado / self.potencia_max) * self.velocidad_grabado_max
        return round(tiempo_procesado, 1)
