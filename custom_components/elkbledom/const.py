from enum import Enum

DOMAIN = "illumi"
CONF_RESET = "reset"
CONF_DELAY = "delay"

# https://api.lxillumi.com/v1/device/sceness/?language=en&model=DMRRBA-007
#{"code": 200, "msg": "success", "data": [{"id": 297, "name": "Auto", "instruction": "00"}, {"id": 298, "name": "Flash", "instruction": "01"}, {"id": 299, "name": "Breath", "instruction": "06"}, {"id": 300, "name": "Bolt", "instruction": "07"}, {"id": 301, "name": "Candle", "instruction": "08"}, {"id": 302, "name": "Ambulance", "instruction": "09"}, {"id": 303, "name": "RGB Fade", "instruction": "02"}, {"id": 304, "name": "Rainbow Fade", "instruction": "03"}, {"id": 305, "name": "RGB Jump", "instruction": "04"}, {"id": 306, "name": "Rainbow Jump", "instruction": "05"}]}

class EFFECTS (Enum):
    none = 0x00
    flash = 0x01
    breath = 0x06
    colt = 0x07
    candle = 0x08
    ambulance = 0x09
    rgb_fade = 0x02
    rainbow_fade = 0x03
    rgb_jump = 0x04
    rainbow_jump = 0x05

EFFECTS_list = ['none',
    'flash',
    'breath',
    'colt',
    'candle',
    'ambulance',
    'rgb_fade',
    'rainbow_fade',
    'rgb_jump',
    'rainbow_jump'
    ]

class WEEK_DAYS (Enum):
    monday = 0x01
    tuesday = 0x02
    wednesday = 0x04
    thursday = 0x08
    friday = 0x10
    saturday = 0x20
    sunday = 0x40
    all = (0x01 + 0x02 + 0x04 + 0x08 + 0x10 + 0x20 + 0x40)
    week_days = (0x01 + 0x02 + 0x04 + 0x08 + 0x10)
    weekend_days = (0x20 + 0x40)
    none = 0x00

#print(EFFECTS.blink_red.value)
