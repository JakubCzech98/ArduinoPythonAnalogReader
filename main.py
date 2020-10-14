import pyfirmata
import time
import csv
class Volatege_Meter:
    PINS = (0, 1, 2, 3)
    board = pyfirmata.Arduino('COM3')
    test_flag = True
    def __init__(self):
        it = pyfirmata.util.Iterator(self.board)
        it.start()
        for pin in self.PINS:
            self.board.analog[pin].enable_reporting()
        self.test()

    def test(self):
        while self.test_flag:
             if(self.board.analog[0].read() != None and self.board.analog[1].read() != None and self.board.analog[2].read() != None  and self.board.analog[3].read() != None ):
                for pin in self.PINS:
                    print("Pin %i : %s" % (pin, self.board.analog[pin].read()))
                print("-----------------------------------------")
                with open('voltage_test.csv', 'a+') as file:
                    writer = csv.writer(file)
                    writer.writerow([ self.board.analog[0].read(),  self.board.analog[1].read(),  self.board.analog[2].read(), self.board.analog[3].read()])
                    time.sleep(1)

if __name__ == '__main__':
    tester = Volatege_Meter()

