import pyfirmata
import csv
import time
from datetime import datetime


class ArduinBoardTester:
    PINS = (0, 1, 2, 3)
    board = pyfirmata.Arduino('COM3')
    test_iterator = 0
    cols=4
    values = [0.0] * cols
    filepath = 'tmp.csv'
    def __init__(self):
        it = pyfirmata.util.Iterator(self.board)
        it.start()
        for pin in self.PINS:
            self.board.analog[pin].enable_reporting()
        self.read()

    def read(self):
        while self.test_iterator < 60:
            if (self.board.analog[0].read() != None and self.board.analog[1].read() != None and self.board.analog[
                2].read() != None and self.board.analog[3].read() != None):
                for x1 in range(self.cols):
                    self.values[x1] += self.board.analog[x1].read() * 5.0 / 1023.0
            self.test_iterator += 1
            time.sleep(1)
            print(self.test_iterator)
        self.write_row()

    def write_row(self):
        for x1 in range(self.cols):
            self.values[x1] /= 60.0
            self.values[x1]=round(self.values[x1], 3)
        self.save()
    def save(self):
        with open(self.filepath, "a", newline='') as f:
            writer = csv.writer(f)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            writer.writerow([current_time, self.values[0],   self.values[1],   self.values[2],   self.values[3]])
            print([  self.values[0],   self.values[1],   self.values[2],   self.values[3]])
        for x1 in range(self.cols):
            self.values[x1] = 0.0
        self.test_iterator = 0







if __name__ == '__main__':
    tester = ArduinBoardTester()
    while (True):
        tester.read()
