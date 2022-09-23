from abc import ABCMeta, abstractmethod

"""监听模式的框架"""


class Observer(metaclass=ABCMeta):
    """观察者基类"""

    @abstractmethod
    def update(self, observable, obj):
        pass


class Observable:
    """被观察者基类"""

    def __init__(self):
        self.__observers = []

    def addObserver(self, observer):
        self.__observers.append(observer)

    def removeObserver(self, observer):
        self.__observers.remove(observer)

    def notifyObservers(self, obj=0):
        for o in self.__observers:
            o.update(self, obj)


class WaterHeater(Observable):
    def __init__(self):
        super().__init__()
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print("当前温度是:" + str(self.__temperature) + " C")
        self.notifyObservers()


class WashingMode(Observer):
    """洗澡模式"""

    def __init__(self):
        pass

    def update(self, observable, obj):
        if isinstance(observable, WaterHeater) \
                and 50 <= observable.getTemperature() < 70:
            print("水已好，可以用来洗澡了")


class DrinkingMode(Observer):
    """饮用模式"""

    def __init__(self):
        pass

    def update(self, observable, obj):
        if isinstance(observable, WaterHeater) and observable.getTemperature() >= 100:
            print("水已烧开，可以用来饮用")


if __name__ == "__main__":
    waterheater = WaterHeater()
    waterheater.addObserver(WashingMode())
    waterheater.addObserver(DrinkingMode())

    waterheater.setTemperature(40)
    waterheater.setTemperature(60)
    waterheater.setTemperature(120)
