class Colorizer:
    colors_id = {"grey": 90, "red": 91, "green": 92, "yellow": 93, "blue": 94, "pink": 95, "turquoise": 96}

    def __init__(self, color: str):
        self._color = color
        self._color_id = Colorizer.colors_id.get(self._color.lower(), 0)

    def __enter__(self):
        if self._color.lower() in Colorizer.colors_id:
            print(f"\033[{self._color_id}m", end="")

    def __exit__(self, type, value, traceback):
        print(f"\033[0m", end="")


# Tests:
# with Colorizer('blue'):
#     print('printed in red')
# print('printed in default color')
