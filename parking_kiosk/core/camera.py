import os
import requests
import base64
import cv2

image_path = "parking_kiosk/gui/res/test.jpg"

# TODO: 사진 찍어서 경로 전달
def get_vehicle_image():
    # 테스트 코드
    return image_path

def capture_image():
    file_path = 'captured_img,jpg'
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if not ret:
        raise Exception("웹캠에서 이미지를 가져올 수 없습니다.")

    cap.release()
    cv2.imwrite(file_path, frame)
    
    print(f"이미지 저장완료 : {file_path}")

def encode_image_to_base64(image_buffer):
    image_base64 = base64.b64encode(image_buffer).decode('utf-8')
    return image_base64

def ocr_reader(image_base64):
    url = 'https://apis.openapi.sk.com/sigmeta/lpr/v1'
    headers = {
        'accept': 'application/json',
        'appKey': 'l7xx846db5f3bc1e48d29b7275a745d501c8'
    }

    output_dir = './result/'
    os.makedirs(output_dir,exist_ok=True)

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

def resize_image(image, max_width=1024, max_height=1024):
    height, width = image.shape[:2]
    if width > max_width or height > max_height:
        scailing_factor = min(max_width / width, max_height / height)
        new_size = (int(width * scailing_factor), int(height * scailing_factor))
        resized_image = cv2.resized(image, new_size, interpolation=cv2.INTER_AREA)
        return resized_image
    return image

print(get_vehicle_image())
capture_image()
ocr_reader()