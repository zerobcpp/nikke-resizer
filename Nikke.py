import sys
import pygetwindow as gw


def resize(size=(2560, 1000)):
    print(size[0], size[1])
    app = [i for i in gw.getWindowsWithTitle('NIKKE') if i.title == 'NIKKE'][0]
    app.resizeTo(size[0], size[1])
    app.activate()


if __name__ == "__main__":
    args = sys.argv
    default_size = (2560, 1000)
    size = default_size
    if len(args) == 3:
        size = (int(args[1]), int(args[2]))
        print(f'Resizing to {size[0]} x {size[1]}')
        resize(size=size)
    elif len(args) == 1:
        print(f'using default size')
        resize(size=default_size)

