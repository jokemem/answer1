from PyQt5.QtWidgets import QLabel, QWidget

menu_win = QWidget()
lb_quest = QLabel('Введіть запитання:')
lb_rights_ans = QLabel('Введіть правильну відповідь')
lb_wrong_ans1 = QLabel('Введіть першу хибну відповідь')
lb_wrong_ans2 = QLabel('Введіть другу хибну відповідь')
lb_wrong_ans3 = QLabel('Введіть третю хибну відповідь')

le_question = QLineEdit()
