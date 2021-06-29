"""Contants for Hitachi Smart App integration"""

from homeassistant.components.climate.const import (
    HVAC_MODE_OFF,
    HVAC_MODE_COOL,
    HVAC_MODE_DRY,
    HVAC_MODE_HEAT,
    HVAC_MODE_AUTO,
    HVAC_MODE_FAN_ONLY,
)

DOMAIN = "Hitachi_smart_app"
PLATFORMS = ["humidifier", "sensor", "number", "binary_sensor", "climate"]
MANUFACTURER = "Hitachi"
DEFAULT_NAME = "Hitachi Smart Application"

DEVICE_TYPE_AC = 0x01
DEVICE_TYPE_DEHUMIDIFIER = 0x04

DATA_CLIENT = "client"
DATA_COORDINATOR = "coordinator"

UPDATE_INTERVAL = 60

DEHUMIDIFIER_MAX_HUMD = 70
DEHUMIDIFIER_MIN_HUMD = 40
DEHUMIDIFIER_AVAILABLE_HUMIDITY = {0: 40, 1: 45, 2: 50, 3: 55, 4: 60, 5: 65, 6: 70}
DEHUMIDIFIER_ON_TIMER_MIN = 0
DEHUMIDIFIER_ON_TIMER_MAX = 12
DEHUMIDIFIER_OFF_TIMER_MIN = 0
DEHUMIDIFIER_OFF_TIMER_MAX = 12

CLIMATE_AVAILABLE_MODE = [
    {"key": HVAC_MODE_OFF, "mappingCode": -1},
    {"key": HVAC_MODE_COOL, "mappingCode": 0},
    {"key": HVAC_MODE_DRY, "mappingCode": 1},
    {"key": HVAC_MODE_FAN_ONLY, "mappingCode": 2},
    {"key": HVAC_MODE_AUTO, "mappingCode": 3},
    {"key": HVAC_MODE_HEAT, "mappingCode": 4},
]
CLIMATE_AVAILABLE_PRESET = {0: "普通模式", 1: "節能模式", 2: "快速模式"}
CLIMATE_AVAILABLE_SWING_MODE = {
    0: "自動",
    1: "右45°",
    2: "右90°",
    3: "左右90°",
    4: "左90°",
    5: "左45°",
}
CLIMATE_AVAILABLE_FAN_MODE = {
    0: "自動",
    1: "靜音",
    2: "微風",
    3: "弱風",
    4: "強風",
}
CLIMATE_MINIMUM_TEMPERATURE = 16
CLIMATE_MAXIMUM_TEMPERATURE = 30
CLIMATE_TEMPERATURE_STEP = 1.0
CLIMATE_ON_TIMER_MIN = 0
CLIMATE_ON_TIMER_MAX = 1440
CLIMATE_OFF_TIMER_MIN = 0
CLIMATE_OFF_TIMER_MAX = 1440

ICON_TANK = "mdi:cup-water"
ICON_HUMIDITY = "mdi:water-percent"
ICON_ON_TIMER = "mdi:alarm"
ICON_OFF_TIMER = "mdi:alarm-snooze"
ICON_THERMOMETER = "mdi:thermometer"
ICON_PM25 = "mdi:dots-hexagon"


LABEL_DEHUMIDIFIER = ""
LABEL_CLIMATE = ""
LABEL_TANK = "水箱滿水"
LABEL_HUMIDITY = "環境溼度"
LABEL_DEHUMIDIFIER_ON_TIMER = "定時開機(時)"
LABEL_DEHUMIDIFIER_OFF_TIMER = "定時關機(時)"
LABEL_CLIMATE_ON_TIMER = "定時開機(分)"
LABEL_CLIMATE_OFF_TIMER = "定時關機(分)"
LABEL_OUTDOOR_TEMPERATURE = "室外溫度"
LABEL_PM25 = "PM2.5"
