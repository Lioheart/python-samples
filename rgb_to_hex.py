"""
Przekształca listę trzech liczb na hex i odwrotnie
"""

def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))

print(hex_to_rgb("FF65BA"))

print(rgb(0,2,0))
print(rgb(255,255,255))
print(rgb(-20,275,125))