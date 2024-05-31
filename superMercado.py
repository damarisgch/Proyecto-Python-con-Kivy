from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen


class SupermercadoScreenManager(ScreenManager):
    inventario = {}
    pro = ObjectProperty()
    codigo = ObjectProperty()
    costo = ObjectProperty()
    busqueda = ObjectProperty()
    producto = StringProperty("")
    precio = StringProperty("")

    def save(self):
        # Agregamos a el diccionario los datos si no son nulos
        if self.codigo.text and self.costo.text and self.pro.text:
            self.inventario[self.codigo.text] = [self.pro.text, self.costo.text]
            print(f"Producto {self.pro.text} guardado con éxito.")
        else:
            print("Supermercado no puede almacenar datos null")
        # Limpiamos los campos de la ventana
        self.codigo.text = ""
        self.pro.text = ""
        self.costo.text = ""

    def buscando(self):
        # Asignamos el parámetro que ingreso el usuario para buscarlo
        busqueda = self.busqueda.text
        if busqueda in self.inventario:
            # Traemos los datos del diccionario
            resultado = self.inventario[busqueda]
            # Asignamos los datos a la ventana a mostrar
            self.producto = resultado[0]
            self.precio = resultado[1]
            print("Búsqueda exitosa!")
        else:
            print("Error de búsqueda o no disponible")
            self.producto = "No Disponible"
            self.precio = "No Disponible"
        # Limpiamos la ventana en el campo de búsqueda
        self.busqueda.text = ""


class SuperMercadoApp(App):
    def build(self):
        return SupermercadoScreenManager()


if __name__ == '__main__':
    SuperMercadoApp().run()
