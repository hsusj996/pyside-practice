import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt, QSize, pyqtSignal
from PyQt6.QtGui import QFont
class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # 현재 레이블 인덱스 초기화
        self.current_label_index = 0
        self.setWindowTitle("주차장 키오스크")
        self.setGeometry(100, 100, 400, 600)
        self.setStyleSheet("background-color: #2E3348;")
        
        # 중앙 위젯 설정
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        # 메인 레이아웃
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # 상단 라벨
        top_label = QLabel("이 차량 번호가 맞나요?", self)
        top_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        top_label.setStyleSheet("color: white; font-size: 30px;")  # 크기를 더 키움
        main_layout.addWidget(top_label, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # 차량 번호 레이아웃
        car_number_widget = QWidget(self)
        car_number_layout = QVBoxLayout()
        car_number_widget.setLayout(car_number_layout)
        car_number_layout1 = QHBoxLayout()
        car_number_layout2 = QHBoxLayout()
        car_number_layout.addLayout(car_number_layout1)
        car_number_layout.addLayout(car_number_layout2)
        main_layout.addWidget(car_number_widget, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.car_number_labels = []
        for i in range(8):  # 8자리로 수정
            # 레이블 생성 시 ClickableLabel 사용
            label = ClickableLabel(" ", self)
            label.setFixedSize(40, 40)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.setStyleSheet("border: 1px solid black; background-color: white; font-size: 20px; border-radius: 3px; color: black;")
            label.clicked.connect(self.label_clicked)  # 클릭 이벤트 연결
            if i < 4:
                car_number_layout1.addWidget(label)
            else:
                car_number_layout2.addWidget(label)
            self.car_number_labels.append(label)
        
        car_number_layout1.setSpacing(5)  # 간격 조정
        car_number_layout2.setSpacing(5)  # 간격 조정
        
        # 더미 데이터 설정
        dummy_data = "11가 1111"
        for i, char in enumerate(dummy_data):
            self.car_number_labels[i].setText(char)
        
        # 천지인 키패드 버튼 클릭 횟수 초기화
        self.cheonjiin_keypad_click_count = {key: 0 for key in ['ㅣ', '·', 'ㅡ', 'ㄱ ㅋ', 'ㄴ ㄹ', 'ㄷ ㅌ', 'ㅂ ㅍ', 'ㅅ ㅎ', 'ㅈ ㅊ', 'ㅇ ㅁ']}
        
        # 키패드 위젯을 멤버 변수로 저장
        self.keypad_widget = QWidget(self)
        self.keypad_layout = QGridLayout()
        self.keypad_widget.setLayout(self.keypad_layout)
        main_layout.addWidget(self.keypad_widget, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # 천지인 키패드와 숫자 키패드를 생성
        self.create_cheonjiin_keypad()
        self.create_number_keypad()

        # 자동 주차하기 버튼
        auto_park_button = QPushButton("자동 주차하기", self)
        auto_park_button.setFixedSize(200, 60)
        auto_park_button.setStyleSheet("""
            background-color: #FFB300; 
            color: white; 
            font-size: 20px; 
            border-radius: 5px;
        """)
        
        button_widget = QWidget(self)
        button_layout = QHBoxLayout()
        button_widget.setLayout(button_layout)
        button_layout.addWidget(auto_park_button, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(button_widget, alignment=Qt.AlignmentFlag.AlignCenter)  # 중앙에 배치
    
    def keypad_clicked(self):
        button = self.sender()
        key = button.text()
        print(f"Key pressed: {key}")

        # 지우기 클릭 시 번호판 칸 수정
        if key == '<-':
            self.car_number_labels[self.current_label_index].setText('')
        # 확인 클릭 시 액션 정의 필요
        elif key == '확인':
            pass
        elif key in self.cheonjiin_keypad_click_count:
            # 클릭 횟수에 따라 첫 번째 글자 또는 두 번째 글자로 변경
            self.cheonjiin_keypad_click_count[key] = (self.cheonjiin_keypad_click_count[key] + 1) % 2
            new_text = key.split()[self.cheonjiin_keypad_click_count[key]]
            self.car_number_labels[self.current_label_index].setText(new_text)
        # 숫자 키패드 버튼 클릭 시
        else:
            self.car_number_labels[self.current_label_index].setText(key)
        
    def create_cheonjiin_keypad(self):
        keys = ['ㅣ', '·', 'ㅡ', 'ㄱ ㅋ', 'ㄴ ㄹ', 'ㄷ ㅌ', 'ㅂ ㅍ', 'ㅅ ㅎ', 'ㅈ ㅊ', '<-', 'ㅇ ㅁ', '확인']
        positions = [(i, j) for i in range(4) for j in range(3)]
        for position, key in zip(positions, keys):
            button = QPushButton(key, self)
            button.setFixedSize(80, 60)
            button.setStyleSheet("""
                background-color: white; 
                font-size: 20px; 
                border-radius: 5px;
                color: black;
            """)
            button.clicked.connect(self.keypad_clicked)
            self.keypad_layout.addWidget(button, *position)
        self.keypad_layout.setSpacing(5)

    def create_number_keypad(self):
        keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '<-', '0', '확인']
        positions = [(i, j) for i in range(4) for j in range(3)]
        for position, key in zip(positions, keys):
            button = QPushButton(key, self)
            button.setFixedSize(80, 60)
            button.setStyleSheet("""
                background-color: white; 
                font-size: 20px; 
                border-radius: 5px;
                color: black;
            """)
            button.clicked.connect(self.keypad_clicked)
            self.keypad_layout.addWidget(button, *position)
        self.keypad_layout.setSpacing(5)
        
    def clear_keypad(self):
        for i in reversed(range(self.keypad_layout.count())):
            self.keypad_layout.itemAt(i).widget().setParent(None)

    def show_number_keyboard(self):
        self.clear_keypad()
        keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '<-', '0', '확인']
        positions = [(i, j) for i in range(4) for j in range(3)]
        for position, key in zip(positions, keys):
            button = QPushButton(key, self)
            button.setFixedSize(80, 60)
            button.setStyleSheet("""
                background-color: white; 
                font-size: 20px; 
                border-radius: 5px;
                color: black;
            """)
            button.clicked.connect(self.keypad_clicked)
            self.keypad_layout.addWidget(button, *position)
        self.keypad_layout.setSpacing(5)

    def show_cheonjiin_keyboard(self):
        self.clear_keypad()
        keys = ['ㅣ', '·', 'ㅡ', 'ㄱ ㅋ', 'ㄴ ㄹ', 'ㄷ ㅌ', 'ㅂ ㅍ', 'ㅅ ㅎ', 'ㅈ ㅊ', '<-', 'ㅇ ㅁ', '확인']
        positions = [(i, j) for i in range(4) for j in range(3)]
        for position, key in zip(positions, keys):
            button = QPushButton(key, self)
            button.setFixedSize(80, 60)
            button.setStyleSheet("""
                background-color: white; 
                font-size: 20px; 
                border-radius: 5px;
                color: black;
            """)
            button.clicked.connect(self.keypad_clicked)
            self.keypad_layout.addWidget(button, *position)
        self.keypad_layout.setSpacing(5)
        
    def label_clicked(self):
        # 레이블 클릭 시 키패드 변경
        label = self.sender()
        if label.text().isdigit():
            self.show_number_keyboard()
        else:
            self.show_cheonjiin_keyboard()
        
        self.current_label_index = self.car_number_labels.index(label)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())