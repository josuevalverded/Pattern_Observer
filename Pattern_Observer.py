#En este programa tendremos dos Observadores uno llamado Andrey, otro Josué. 
# Cada uno descubrirá en cuanto está la temperatura, los observadores están divididos por Estaciones
# Hay valores ya establecidos en cuanto a la temperatura. 
# Una vez que la temperatura varíe, notificará a solo uno de los observadores.
#  Y veremos como el otro observador que interactúa con la temperatura ya no será notificado de ese cambio

# abc Define y usa clases de base abstractas para la verificación de la interfaz.
import abc

#Comenzaremos creando una interfaz para el tema llamado Subject. 
# Esta declarará tres métodos: addObserver(), removeObserver(), y doNotify().
class Subject(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add_observer(self, observer):
        pass

    @abc.abstractmethod
    def remove_observer(self, observer):
        pass

    @abc.abstractmethod
    def do_notify(self):
        pass

#También crearemos una interfaz para los observadores. Cuenta con un método,Update()
class Observer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def do_update(self, temperature):
        pass

#La clase WeatherEstación implementa al Subject. Es nuestra clase de asignaturas. 
# se agregan los métodos addObserver()y eliminar---> removeObserver(). 
# Cuando Subjec del estado cambia a través de setTemperature(),
# doNotify()llama al método, que contacta todo los Observers 
# con la temperatura a través de sus métodos.
class WeatherEstacion(Subject):
    def __init__(self, temperature):
        self.observers = []
        self.temperature = temperature

    def add_observer(self, weather):
        self.observers.append(weather)

    def remove_observer(self, weather):
        self.observers.remove(weather)

    def do_notify(self):
        for observer in self.observers:
            observer.do_update(self.temperature)

    def set_temperature(self, temperature):
        print("La temperatura es de : %s" % temperature)
        self.temperature = temperature
        self.do_notify()

#es un clase para el primer observador que implementa la clase Observer. 
# Su método obtiene la temperatura actual del WeatherEstación y la muestra.
class Weather_Estacion_Norte(Observer):
    def do_update(self, temperature):
        print("Josué acaba de ser notificado que la temperatura está: %s" % temperature)

# segunda clase similar a la del primer observador
class Weather_Estacion_Sur(Observer):
    def do_update(self, temperature):
        print("Andrey acaba de ser notificado que la temperatura está: %s" % temperature)

#En el main se demuestra el patrón de observador. 
# Los dos clientes se agregan como observadores a la estación meteorológica.
# Entonces por medio del método setTemperature()se llama al método de la estación meteorológica. 
# Esto hace que cambie el estado de la estación meteorológica y 
# los clientes sean notificados de esta actualización de temperatura.
#  A continuación, la Estacion_Norte se elimina de la colección de observadores de la estación. 
# Entonces, el método setTemperature()se llama nuevamente. 
# lo que genera como resultado la notificación de la Estación_Sur.
if __name__ == '__main__':
    estacion = WeatherEstacion(40)

    Josue= Weather_Estacion_Norte()
    Andrey= Weather_Estacion_Sur()
    estacion.add_observer(Josue)
    estacion.add_observer(Andrey)

    estacion.set_temperature(45)
    estacion.remove_observer(Josue)
    estacion.set_temperature(50) 