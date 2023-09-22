from pynput.mouse import Listener, Button
import pyautogui
import time


class Draw:
    def __init__(self):
        self.shape = 'SQUARE'
        self.start = None
        self.end = None
        self.valid_shapes = ['SQUARE', 'CIRCLE']
        self.did_receive_point_recently = False

    def set_shape(self):
        while self.shape is None:
            shape = input("Enter the shape you want to draw (circle, square) ").strip().upper()
            if shape in self.valid_shapes:
                self.shape = shape


    def set_point(self, x, y):
        if self.start is None:
            self.start = (x, y)
        elif self.end is None:
            if(self.start[0] == x and self.start[1] == y):
                print('swallowing set point')
                return
            self.end = (x, y)
            self.draw()
        else:
            print('swallowing set point')

    def draw(self):
        print('drawing shape, do not move your mouse')
        time.sleep(1)

        if self.shape == "CIRCLE":
            self.draw_circle()
        elif self.shape == "SQUARE":
            self.draw_rectangle()
        else:
            print("Invalid shape")

        exit(0)

    def draw_rectangle(self):
        x1, y1 = self.start
        x2, y2 = self.end

        pyautogui.moveTo(x1, y1)
        pyautogui.dragTo(x2, y1, duration=0.25, button="left")
        time.sleep(0.1)
        pyautogui.dragTo(x2, y2, duration=0.25, button="left")
        time.sleep(0.1)
        pyautogui.dragTo(x1, y2, duration=0.25, button="left")
        time.sleep(0.1)
        pyautogui.dragTo(x1, y1, duration=0.25, button="left")
        time.sleep(0.1)

    def draw_circle(self):
        x1, y1 = self.start
        x2, y2 = self.end

        # Calculate the center and radius based on the provided corners
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2
        radius = min(abs(x2 - x1), abs(y2 - y1)) // 2

        pyautogui.moveTo(center_x, center_y)
        pyautogui.dragTo(
            center_x + radius, center_y, duration=0.25, button="left"
        )  # Draw a circle using a horizontal line
        pyautogui.moveTo(center_x, center_y)
        pyautogui.dragTo(
            center_x, center_y + radius, duration=0.25, button="left"
        )  # Draw a circle using a vertical line

    def on_click(self, x, y, button, pressed):
        if button == Button.left:
            print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
            self.set_point(x, y)
            time.sleep(0.5)




draw = Draw()


draw.set_shape()

# listener = mouse.Listener(on_click=draw.on_click)
# listener.join()

with Listener(on_click=draw.on_click) as listener:
    listener.join()