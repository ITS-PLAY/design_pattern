from abc import ABCMeta, abstractmethod
import time


class Observer(metaclass=ABCMeta):
    """观察者基类"""

    @abstractmethod
    def update(self, observable, obj):
        pass


class Observable(object):
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


class Account(Observable):
    def __init__(self):
        super().__init__()
        self.__latestip = {}
        self.__latestRegion = {}

    def login(self, name, ip, time):
        region = self.__getRegion(ip)
        if self.__isLongDistance(name, region):
            self.notifyObservers({"name": name, "ip": ip, "region": region, "time": time})

        self.__latestRegion[name] = region
        self.__latestip[name] = ip

    def __getRegion(self, ip):
        ipRegion = {
            "101.47.18.9": "浙江省杭州市",
            "67.218.147.69": "吉林省长春市"
        }
        region = ipRegion.get(ip)
        return "" if region is None else region

    def __isLongDistance(self, name, region):
        latestRegion = self.__latestRegion.get(name)
        return latestRegion is not None and latestRegion != region


class SmsSender(Observer):
    def update(self, observable, obj):
        print("短信发送" + obj.get("name") + " 登录时间:" + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(obj.get("time"))))


class MailSender(Observer):
    def update(self, observable, obj):
        print("邮件发送" + obj.get("name") + " 登录时间:" + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(obj.get("time"))))


if __name__ == "__main__":
    account = Account()
    account.addObserver(SmsSender())
    account.addObserver(MailSender())

    account.login("Tony", "101.47.18.9", time.time())
    account.login("Tony", "67.218.147.69", time.time())
