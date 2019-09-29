# -*- encoding: utf-8 -*-

import sys
import time
import pandas as pd

from get_code import getCode
from get_futures_tick import getFuturesTick
from get_index_tick import getIndexTick
from calculate import calculate

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# setting pandas DataFrame's display parameters
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

class MyTable(QTableWidget):

    def __init__(self, parent=None):
        super(MyTable, self).__init__(parent)
        self.setWindowTitle("Real-Time Basis")
        self.setWindowIcon(QIcon("icon.png"))
        self.resize(500, 420)
        self.setColumnCount(4)
        self.setRowCount(12)
        self.setHorizontalHeaderLabels(['Futures Code', 'Futures Prices', 'Index Prices', 'Real Basis'])
        self.setVerticalHeaderLabels(['IF当月','IF下月','IF下季','IF隔季','IH当月','IH下月','IH下季','IH隔季','IC当月','IC下月','IC下季','IC隔季'])

    # updating table items
    def update_item_data(self, data):
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                self.setItem(i, j, QTableWidgetItem(str(data.iloc[i, j])))


class UpdateData(QThread):

    update_date = pyqtSignal(pd.DataFrame)

    def __init__(self, parent=None):
        super(UpdateData, self).__init__(parent)
        self.future_codes = getCode()
        self.index_codes = ['000300.SH', '000016.SH', '000905.SH']

    def run(self):
        while True:
            future_ticks = getFuturesTick(self.future_codes['IF'] + self.future_codes['IH'] + self.future_codes['IC'])
            index_ticks = getIndexTick(self.index_codes)
            result = calculate(future_ticks, index_ticks)
            self.update_date.emit(result)
            # print(result)
            time.sleep(1)


if __name__ == '__main__':

    # Initializing the monitor table
    app = QApplication(sys.argv)
    myTable = MyTable()

    # starting the updating thread
    update_data_thread = UpdateData()
    # connecting signal
    update_data_thread.update_date.connect(myTable.update_item_data)
    update_data_thread.start()

    # setting the table's coordinates
    desktop = QApplication.desktop()
    x = (desktop.width() - myTable.width()) // 1.2
    y = (desktop.height() - myTable.height()) // 1.2
    myTable.move(x, y)

    # show the table
    myTable.show()
    app.exit(app.exec_())