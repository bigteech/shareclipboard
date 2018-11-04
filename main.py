import sys
import mainwindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtCore import Qt
from quamash import QEventLoop
from scanhost import manager
import asyncio
import pyperclip


loop = QEventLoop(QApplication(sys.argv))
asyncio.set_event_loop(loop)
MainWindow = QMainWindow()
ui = mainwindow.Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

label_height = 0

def flush_user():
    [x.setParent(None) for x in ui.users.children()]
    i = 0
    for z, y in manager.get_hosts().items():
        label = QLabel(ui.users)
        label.setText(y[0])
        label.move(0, i * 10)
        i += 1
        label.show()

def get_text_from_editor():
    return ui.textEdit.toPlainText()

def get_label(data):
    label = QLabel(ui.history)
    label.setText(data)
    label.setTextInteractionFlags(Qt.TextSelectableByMouse)
    label.setMaximumWidth(300)
    return label

def get_btn(data):
    btn = QPushButton(ui.history)
    btn.setText('copy')
    btn.clicked.connect(lambda x: pyperclip.copy(data))
    return btn

def on_reg(data, addr):
    manager.reg(data, addr)
    flush_user()
    return 'success'

def on_text(data, addr):
    init_history(data)
    return 'success'


def init_history(data):
    global label_height
    label = get_label(data)
    label.move(80, label_height + 6)
    label.show()

    btn = get_btn(data)
    btn.move(0, label_height)
    btn.show()

    label_height += (label.height() + 10)

def listen():
    manager.reg_msg_handler('reg', on_reg)
    manager.reg_msg_handler('text', on_text)
    manager.listen()


def send_msg():
    data = get_text_from_editor()
    ui.textEdit.clear()
    manager.send_msg(data)


def set_name():
    name = ui.nameInput.toPlainText()
    manager.set_name(name or 'anonymous')


ui.nameInput.textChanged.connect(set_name)
ui.submit.clicked.connect(send_msg)
listen()
loop.create_task(manager.heartbeat(flush_user))
sys.exit(loop.run_forever())

