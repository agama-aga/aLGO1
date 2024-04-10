# from PyQt5.QtCore import QSize, Qt
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
# app = QApplication([])
# t = QWidget()
# t.setWindowTitle("1")
# n = QPushButton("Начать")
# е = QWidgets.QLabel('программа для определения состояния здоровья')
# t = QWidgets.QLabel('Проба Руфье — это нагрузочный тест, который определяет работоспособность сердца во время и после физических нагрузок.  Проводится тестирование быстро, длится не более 5 минут, не требует использования специального оборудования, поэтому его можно выполнять в домашних условиях.  Исследование показывает:  адаптацию организма к интенсивным нагрузкам;  физическую выносливость;  отклонения в работе сердца;  способность сердца восстанавливаться после кратковременных нагрузок;  состояние вегетативной нервной системы.  Главная задача теста Руфье — оценить резервные возможности сердечной мышцы и на основании полученной информации подобрать для ребёнка оптимальный вариант физической активности, котор')
# t.resize(400, 200)
# t.show()
# v_line = QVBoxLayout()
# h_line = QHBoxLayout()
# v_line.addWidget(e, alignment = Qt.AlignCenter)
# t.setLayout(v_line)
# def rt():

#     t.setLayout(v_line)
#     n.clicked.connect(rt)
# app.exec_()

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
app = QApplication([])
t = QWidget()
t.setWindowTitle("1")
n = QLabel("Начать")
t.resize(400, 200)
t.show()
v_line = QVBoxLayout()
h_line = QHBoxLayout()
v_line.addWidget(n, alignment = Qt.AlignCenter)
t.setLayout(v_line)
app.exec_()
