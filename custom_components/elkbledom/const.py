from enum import Enum

DOMAIN = "illumi"
CONF_RESET = "reset"
CONF_DELAY = "delay"

class EFFECTS (Enum):
    flash = 0x01
    breath = 0x06
    colt = 0x07
    candle = 0x08
    ambulance = 0x09
    rgb_fade = 0x02
    rainbow_fade = 0x03
    rgb_jump = 0x04
    rainbow_jump = 0x05

EFFECTS_list = ['flash',
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
