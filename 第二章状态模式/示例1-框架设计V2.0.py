from abc import ABCMeta, abstractmethod

"""状态模式的框架设计"""
class Context(metaclass=ABCMeta):
    """状态模式的上下文环境类"""
    def __init__(self):
        self.__states = []              #用于存储不同的状态，避免if else的判断
        self.__curState = None
        self.__stateInfo = 0            #用于保存对象的关键属性

    def addState(self, state):
        """state采用单例模式"""
        if state not in self.__states:
            self.__states.append(state)

    def changeState(self, state):
        if state is None:
            return False
        if self.__curState is None:
            print("初始化为 {}".format(state.getName()))
        else:
            print("由 {} 变为 {} \t".format(self.__curState.getName(), state.getName()))
        self.__curState = state
        self.addState(state)
        return True

    def getState(self):
        return self.__curState

    def _setStateInfo(self, stateInfo):
        self.__stateInfo = stateInfo
        for state in self.__states:
            if state.isMatch(stateInfo):
                self.changeState(state)

    def _getStateInfo(self):
        return self.__stateInfo


class State:
    """状态的基类"""
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def isMatch(self, stateInfo):
        return False

    @abstractmethod
    def behavior(self, context):
        pass



"""基于框架的改进"""
class Water(Context):

    def __init__(self):
        super(Water, self).__init__()
        self.addState(SolidState("固态"))
        self.addState(LiquidState("液态"))
        self.addState(GaseousState("气态"))
        self.setTemperature(25)

    def getTemperature(self):
        return self._getStateInfo()

    def setTemperature(self, temperature):
        return self._setStateInfo(temperature)

    def riseTemperature(self, step):
        self.setTemperature(self.getTemperature() + step)

    def reduceTemperature(self, step):
        self.setTemperature(self.getTemperature() - step)

    def behavior(self):
        state = self.getState()
        if isinstance(state, State):
            state.behavior(self)


"""单例的装饰器"""
def singleton(cls, *args, **kwargs):
    instance = {}

    def __singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return __singleton


@singleton
class SolidState(State):
    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return stateInfo < 0

    def behavior(self, context):
        print("固态, 当前体温是 {}".format(context._getStateInfo()))


@singleton
class LiquidState(State):
    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return 0 <= stateInfo < 100

    def behavior(self, context):
        print("液态, 当前体温是 {}".format(context._getStateInfo()))


@singleton
class GaseousState(State):
    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return stateInfo >= 100

    def behavior(self, context):
        print("气态, 当前体温是 {}".format(context._getStateInfo()))


if __name__ == "__main__":
    water = Water()

    water.setTemperature(-4)
    water.behavior()

    water.setTemperature(16)
    water.behavior()

    water.setTemperature(110)
    water.behavior()


