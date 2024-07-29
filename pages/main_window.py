from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QStackedWidget
from components.main_button import MainButton
from components.top_label import TopLabel
from components.enter_number_plate import EnterNumberPlate
from components.keypad import Keypad
from components.park_button import ParkButton
from pages.settlement_page import SettlementPage
from PyQt6.QtCore import Qt, QTimer
from pages.exit_page import ExitPage
from pages.entry_page import EntryPage
from components.gif_widget import GifWidget
from pages.vehicle_selection_page import VehicleSelectionPage

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("주차장 키오스크")
        self.setGeometry(100, 100, 400, 600)
        self.setStyleSheet("background-color: #2E3348;")

        # 중앙 위젯 설정
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # 스택 위젯 설정
        self.stacked_widget = QStackedWidget(self)
        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        central_widget.setLayout(layout)

        # 메인 버튼 페이지
        self.main_button = MainButton(self)
        self.main_button.entry_button.clicked.connect(self.show_entry_page)
        self.main_button.exit_button.clicked.connect(self.show_exit_page)
        self.stacked_widget.addWidget(self.main_button)

        # # 입차 페이지
        self.entry_page = EntryPage(self)
        self.stacked_widget.addWidget(self.entry_page)
        
        # 출차 페이지
        self.exit_page = ExitPage(self)
        self.stacked_widget.addWidget(self.exit_page)

    def show_entry_page(self):
        self.stacked_widget.setCurrentWidget(self.entry_page)

    def show_exit_page(self):
        self.stacked_widget.setCurrentWidget(self.exit_page)
    
    def show_settlement_page(self, vehicle_info):
        settlement_page = SettlementPage(vehicle_info, self)
        self.stacked_widget.addWidget(settlement_page)
        self.stacked_widget.setCurrentWidget(settlement_page)
        
    def show_gif_widget(self):
        gif_widget = GifWidget("res/test.gif", duration=3000, parent=self)
        gif_widget.move(self.rect().center() - gif_widget.rect().center())
        gif_widget.start()
        QTimer.singleShot(3000, self.return_to_main)

    def show_vehicle_selection_page(self):
        vehicles = [
            {
                'image_path': 'res/car1.png',
                'plate_number': '19오 7777',
                'duration': '43분'
            },
            {
                'image_path': 'res/car2.png',
                'plate_number': '77소 7777',
                'duration': '1시간 7분'
            },
            # 다른 차량 정보를 추가하세요.
        ]
        vehicle_selection_page = VehicleSelectionPage(vehicles, self)
        self.stacked_widget.addWidget(vehicle_selection_page)
        self.stacked_widget.setCurrentWidget(vehicle_selection_page)
    
    def return_to_main(self):
        self.stacked_widget.setCurrentWidget(self.main_button)