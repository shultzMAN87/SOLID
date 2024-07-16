from abc import ABC, abstractmethod


class PrintingInterface(ABC):
    @abstractmethod
    def printing(self):
        pass

class ScaningUnterface(ABC):
    @abstractmethod
    def scaning(self):
        pass

class CopingInterface(ABC):
    @abstractmethod
    def coping(self):
        pass

class Printer(PrintingInterface):
    def printing(self):
        print('Я принтер и я печатаю')

class Scanner(ScaningUnterface):
    def scaning(self):
        print('Я сканер и я сканирую')

class MultifunctionalDevice(PrintingInterface, ScaningUnterface, CopingInterface):
    def printing(self):
        print('Я МФУ и я печатаю')

    def scaning(self):
        print('Я МФУ и я сканирую')

    def coping(self):
        print('Я МФУ и я копирую')

pr = Printer()
pr.printing()

mfd = MultifunctionalDevice()
mfd.scaning()

# sc = Scanner()
# sc.printing()



