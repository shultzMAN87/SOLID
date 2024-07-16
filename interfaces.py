from abc import ABC, abstractmethod


class PrinterInterface(ABC):

    @abstractmethod
    def printing(self):
        pass

    @abstractmethod
    def scaning(self):
        pass

    @abstractmethod
    def coping(self):
        pass

class Printer(PrinterInterface):

    def printing(self):
        print('Я печатаю')
    def scaning(self):
        raise NotImplemented('Метод не реализован в данном классе')

    def coping(self):
        raise NotImplemented('Метод не реализован в данном классе')

class Scanner(PrinterInterface):

    def printing(self):
        raise NotImplemented('Метод не реализован в данном классе')
    def scaning(self):
        print('Я сканирую')

    def coping(self):
        raise NotImplemented('Метод не реализован в данном классе')


printer = Printer()
printer.scaning()
# scanner = Scanner()