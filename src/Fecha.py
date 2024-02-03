from datetime import date


class Fecha:
    def crear_fecha(self, anio, mes, dia):
        try:
            nueva_fecha = date(anio, mes, dia)
            return nueva_fecha
        except ValueError as e:
            print(f"Error al crear la fecha: {e}")
            return None


if __name__ == '__main__':
    mi_fecha = Fecha()
    mi_fecha.crear_fecha(2024, 2, 29)
    print("Fecha :", mi_fecha)

