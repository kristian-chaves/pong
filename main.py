from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector

class PongBall(Widget):

    #velocity of ball on x y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # referencelist property - lets us ball.velocity as shorthand
    velocity = ReferenceListProperty(velocity_x,velocity_y)

    # move the ball one step
    # called in equal intervals to animate ball
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class PongGame(Widget):
    
    pass

class PongApp(App):
    def build(self):
        return PongGame()

if __name__ == '__main__':
    PongApp().run()