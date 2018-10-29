import sys
import mainwindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from scanhost import manager
import threading


def on_reg(data):
    return 'hhahah'

def on_text(data):
    return f'一段文本{data}'

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = mainwindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    def listen():
        manager.reg_msg_handler('reg', on_reg)
        manager.reg_msg_handler('text', on_text)
        manager.listen()

    threading.Thread(target=listen).start()


    # manager.heartbeat()
    sys.exit(app.exec_())

