# Riley Hall
# SDEV 220
# Exercise 9.3
# Creating a racecar using tkinter!

from tkinter import *

class raceCar:
    def __init__(self):
        window = Tk()
        window.title = "Race Car"
        self.canvas = Canvas(window, width=600, height=100, bg="white")
        self.canvas.pack()
        self.canvas.focus_set()
        # starting position
        self.x = 15
        self.y = 90

        # Movement speed
        self.dx = 6
        self.sleeptime = 100
        self.width = 600

        # Key Bindings
        self.canvas.bind("<Up>", self.faster)
        self.canvas.bind("<Down>", self.slower)

        # display car
        self.displayCar()

        # Car driving loop
        self.moveCar()
        self.canvas.mainloop()

    def displayCar(self):
        # Front tire
        self.canvas.create_oval(self.x + 10, self.y - 10, self.x + 20, self.y, fill="black", tags="car")
        # Back tire
        self.canvas.create_oval(self.x + 30, self.y - 10, self.x + 40, self.y, fill="black", tags="car")
        # Body
        self.canvas.create_rectangle(self.x, self.y - 20, self.x + 50, self.y - 10, fill="red", tags="car")
        # Roof
        self.canvas.create_rectangle(self.x + 10, self.y - 15, self.x + 40, self.y - 30, fill="white", tags="car")

    def moveCar(self):
        self.canvas.move("car", self.dx, 0)
        self.canvas.after(self.sleeptime, self.moveCar)
        # Loops  car back to left side
        if self.x < self.width:
            self.x += self.dx
        else:
            self.x = 5
            self.canvas.delete("car")
            self.displayCar()

    def faster(self, arg):
        if self.dx > 50:
            print("Cannot go any faster!")
        else:
            self.dx += 10
            print("Speeding up!")

    def slower(self, arg):
        if self.dx < 5:
            print("Cannot go any slower!")
        else:
            self.dx -= 5
            print("Slowing down!")




raceCar()