from abc import ABCMeta, abstractmethod


"""以热水器为被观察者，不同的使用模式作为观察者，测试监听模式"""
class WaterHeater:
    def __init__(self):
        self.__observers = []
        self.__temperature = 25

    def getTemperature(self):
        return  self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        self.notifies()

    def addObserver(self, observer):
        self.__observers.append(observer)

    def notifies(self):
        for o in self.__observers:
            o.update(self)


class Observer(metaclass=ABCMeta):
    """观察者的基类"""
    @abstractmethod
    def update(self, waterHeater):
        pass


class WashingMode(Observer):
    """洗澡模式"""
    def update(self, waterHeater):
        if 70 > waterHeater.getTemperature() >= 50:
            print("水已烧好！ 温度正好")


class DrinkingMode(Observer):
    """饮用模式"""
    def update(self, waterHeater):
        if waterHeater.getTemperature() >= 100:
            print("水已烧好！ 可以用来饮用")


if __name__ == '__main__':
    heater = WaterHeater()
    washingObser = WashingMode()
    drinkingObser = DrinkingMode()

    heater.addObserver(washingObser)
    heater.addObserver(drinkingObser)

    heater.setTemperature(40)
    heater.setTemperature(60)
    heater.setTemperature(100)