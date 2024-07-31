import cv2
import os
import requests
import base64

# openapi url
url = 'https://apis.openapi.sk.com/sigmeta/lpr/v1'

# 웹캠 초기화 (0은 기본 웹캠을 의미합니다. 여러 개의 웹캠이 있을 경우 1, 2, 3 등을 사용)
cap = cv2.VideoCapture(0)

# 웹캠이 열렸는지 확인
if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

# 비디오 스트림 읽기
while True:
    ret, frame = cap.read()

    if not ret:
        print("프레임을 수신할 수 없습니다. 종료합니다...")
        break

    # 프레임을 창에 표시
    cv2.imshow('Camera', frame)

    # 'q' 키를 누르면 루프 종료 및 이미지 저장
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite('captured_img.jpg', frame)
        break

# 모든 리소스 해제
cap.release()
cv2.destroyAllWindows()

headers = {
    'accept': 'application/json',
    'appKey': 'l7xx846db5f3bc1e48d29b7275a745d501c8'
}

output_dir = './result/'
os.makedirs(output_dir,exist_ok=True)

def resize_image(image, max_width=1024, max_height=1024):
    height, width = image.shape[:2]
    if width > max_width or height > max_height:
        scailing_factor = min(max_width / width, max_height / height)
        new_size = (int(width * scailing_factor), int(height * scailing_factor))
        resized_image = cv2.resized(image, new_size, interpolation=cv2.INTER_AREA)
        return resized_image
    return image

image = cv2.imread('./captured_img.jpg')
resized_img = resize_image(image)

temp_file_path = './temp_image.jpg'
cv2.imwrite(temp_file_path, resized_img)

with open(temp_file_path,'rb') as image_file:
    files = {
        'File': ('captured_img.jpg', image_file, 'image/jpeg')
    }
    
    response = requests.post(url, headers=headers, files=files)
    
    response_json = response.json()
    if 'result' in response_json and 'objects' in response_json['result']:
        lp_string = response_json['result']['objects'][0]['lp_string']
        
        with open(temp_file_path, 'rb') as img_file:
            base64_encoded_img = base64.b64encode(img_file.read()).decode('utf-8')
        
os.remove(temp_file_path)
print(lp_string)
print(base64_encoded_img)

# 서버로 전송할 데이터 생성
# server_data = {
#     "lp_string": lp_string,
#     "image": base64_encoded_img
# }

# 서버로 데이터 전송
# server_url = 'http://your-server-endpoint.com/endpoint'  # 서버 엔드포인트 URL로 변경
# server_response = requests.post(server_url, json=server_data)