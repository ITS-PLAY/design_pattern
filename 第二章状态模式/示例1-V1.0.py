from abc import ABCMeta, abstractmethod


"""以水为例子，通过水的不同状态改变，测试状态模式设计"""
class Water:
    """水"""

    def __init__(self, state):
        self.__temperature = 25
        self.__state = state

    def getTemperature(self):
        return self.__temperature

    def changeState(self, state):
        if self.__state:
            print("由 {} 变为 {} \t".format(self.__state.getName(), state.getName()))
        else:
            print("初始化为 {} \t".format(state.getName()))
        self.__state = state

    def setTemperature(self, temperature):
        self.__temperature = temperature
        if self.__temperature <= 0:
            self.changeState(SolidState("固态"))
        elif self.__temperature <= 100:
            self.changeState(LiquidState("液态"))
        else:
            self.changeState(GaseousState("气态"))

    def riseTemperature(self, step):
        self.setTemperature(self.__temperature + step)

    def reduceTemperature(self, step):
        self.setTemperature(self.__temperature - step)

    def behavior(self):
        self.__state.behavior(self)


class State(metaclass=ABCMeta):
    """不同状态模式的基类"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @abstractmethod
    def behavior(self, water):
        """不同状态下的行为"""
        pass


class SolidState(State):
    """固态"""
    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print("固态, 当前体温是 {}".format(water.getTemperature()))


class LiquidState(State):
    """液态"""

    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print("液态, 当前体温是 {}".format(water.getTemperature()))


class GaseousState(State):
    """气态"""

    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print("气态, 当前体温是 {}".format(water.getTemperature()))


if __name__ == "__main__":
    water = Water(LiquidState("液态"))

    water.behavior()

    water.setTemperature(-4)
    water.behavior()

    water.setTemperature(18)
    water.behavior()

    water.setTemperature(110)
    water.behavior()
