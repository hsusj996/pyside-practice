# config/config.py
# 외부 공용 브로커 사용 중
# 로컬 브로커로 변경해야함
MQTT_PORT = 1883
MQTT_BROKER_IP = "192.168.30.151"
MQTT_TOPIC_COMMAND = "parking/command"
MQTT_BROKER_PATH = "C:\\Program Files\\mosquitto\\mosquitto.exe"
MQTT_CONF_PATH = "C:\\Program Files\\mosquitto\\mosquitto.conf"