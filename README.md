### `README.md`

# 주차장 키오스크 시스템

## 개요
PyQT6를 활용한 주차장 키오스크 프론트 화면입니다. (PyQT6 실습을 통해 제작했습니다.)

## 프로젝트 구조

```
parking_kiosk/
├── main.py
├── components/
│   ├── __init__.py
│   ├── clickable_label.py
│   ├── gif_widget.py
│   ├── keypad.py
│   ├── park_button.py
│   ├── top_label.py
│   ├── enter_number_plate.py
├── pages/
│   ├── __init__.py
│   ├── main_window.py
│   ├── entry_page.py
│   ├── exit_page.py
│   ├── settlement_page.py
│   ├── vehicle_selection_page.py
│   ├── main_button.py
│   ├── vehicle_list_item.py
└── res/
└── README.md
```

## 파일 설명

### main.py
애플리케이션의 진입점으로, `MainWindow` 클래스를 초기화하고 실행합니다.

### components/
- **clickable_label.py**: 클릭 가능한 라벨 컴포넌트.
- **gif_widget.py**: GIF 위젯 컴포넌트.
- **keypad.py**: 천지인 키패드와 숫자 키패드를 관리하는 컴포넌트.
- **park_button.py**: 주차 버튼 컴포넌트.
- **top_label.py**: 상단 라벨 컴포넌트.
- **enter_number_plate.py**: 번호판 입력 컴포넌트.

### pages/
- **main_window.py**: 메인 윈도우를 정의하는 파일. 페이지 전환과 메인 UI 구성 요소를 관리합니다.
- **entry_page.py**: 입차 페이지를 정의하는 파일.
- **exit_page.py**: 출차 페이지를 정의하는 파일.
- **settlement_page.py**: 정산 페이지를 정의하는 파일.
- **vehicle_selection_page.py**: 출차 시 차량을 선택하는 페이지를 정의하는 파일.
- **main_button.py**: 메인 화면의 입차 및 출차 버튼을 정의하는 파일.
- **vehicle_list_item.py**: 차량 리스트의 각 아이템을 정의하는 파일.

### res/
이미지와 같은 리소스 파일을 포함하는 폴더입니다.

## 주요 기능

### 입차 기능
1. **MainWindow**:
    - 메인 윈도우를 초기화하고, 중앙 위젯으로 `QStackedWidget`을 설정합니다.
    - 입차 페이지와 출차 페이지를 추가하고, 페이지 전환 기능을 제공합니다.
2. **EntryPage**:
    - 상단 라벨, 번호판 입력, 키패드, 자동주차 버튼으로 구성됩니다.
    - `ParkButton` 클릭 시 `MainWindow`의 `show_gif_widget` 메서드를 호출하여 GIF를 표시합니다.
3. **Keypad**:
    - 천지인 키패드와 숫자 키패드를 제공합니다.
    - 키패드 입력을 통해 번호판 입력란을 수정할 수 있습니다.
    - `확인` 버튼 클릭 시 `MainWindow`의 `show_gif_widget` 또는 `show_vehicle_selection_page` 메서드를 호출합니다.

### 출차 기능
1. **ExitPage**:
    - 출차 시 차량을 선택할 수 있는 페이지입니다.
2. **VehicleSelectionPage**:
    - 출차 시 차량 리스트를 보여주고, 선택된 차량의 정보를 바탕으로 정산 페이지로 이동합니다.
3. **SettlementPage**:
    - 선택된 차량의 정보를 바탕으로 정산 정보를 보여줍니다.

## 실행 방법
1. 이 저장소를 클론합니다:
   ```bash
   git clone <repository-url>
   ```
2. 필요한 패키지를 설치합니다:
   ```bash
   pip install -r requirements.txt
   ```
3. 애플리케이션을 실행합니다:
   ```bash
   python main.py
   ```

## 향후 작업
- 사용자 인터페이스 개선
- 추가 기능 구현
- 백엔드 기능 통합
```

### 주요 변경 사항 요약

1. **폴더 구조 개선**:
   - `components` 폴더와 `pages` 폴더로 나누어 컴포넌트와 페이지를 분리하였습니다.
   - 각 파일의 역할을 명확히 정의하여 모듈화하였습니다.

2. **기능 구현**:
   - 입차 및 출차 기능 구현.
   - 정산 페이지를 통해 요금을 확인하고 결제할 수 있는 기능 추가.

3. **사용자 인터페이스**:
   - 사용자 인터페이스의 각 요소를 컴포넌트화하여 재사용 가능하게 구성하였습니다.

