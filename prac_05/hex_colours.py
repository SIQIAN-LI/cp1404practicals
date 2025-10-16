COLOR_TO_CODE = {
    'absolutezero': '#0048ba',
    'acidgreen': '#b0bf1a',
    'aliceblue': '#f0f8ff',
    'aqua': '#00ffff',
    'ashgrey': '#b2beb5',
    'blueviolet': '#8a2be2',
    'brightube': '#d19fe8',
    'brilliantrose': '#ff55a3',
    'smokyblack': '#100c08',
    'crimson': '#dc143c'
}
print(COLOR_TO_CODE)
max_color_width = max(len(color) for color in COLOR_TO_CODE.keys())

color = input("Color: ").lower()
while color != '':
    try:
        print(f"{color:{max_color_width}} code is {COLOR_TO_CODE[color]}")
    except KeyError:
        print("Invalid input or unrecorded color")
    color = input("Color: ").lower()
