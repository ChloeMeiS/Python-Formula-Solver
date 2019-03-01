# Import the modules
import sys
import math
import tkinter as tk
from cgitb import text

class FormulaCalculator(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tkMain = tk.Frame(self)

        self.geometry("300x275")
        self.title('Python Project 1')

        tkMain.pack(side="top", fill="both", expand=True)

        tkMain.grid_rowconfigure(0, weight=1)
        tkMain.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainMenu, AreaMenu, VolumeMenu, PerimeterMenu, CalculusMenu,
                  AreaSquare, AreaRectangle, AreaCircle, AreaTrapezoid, AreaSphere, AreaTriangle,
                  PerimeterSquare, PerimeterRectangle, PerimeterTriangle, PerimeterCircle,
                  VolumeCube, VolumeRectangle, VolumeSqrPyr, VolumeCylinder, VolumeCone, VolumeSphere,
                  Quadratic, Distance, Slope):
            frame = F(tkMain, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuText = tk.Label(self, text='What type of formula would you like to use?').pack()

        button1 = tk.Button(self, text="Areas", command=lambda: controller.show_frame(AreaMenu)).pack()
        button2 = tk.Button(self, text="Perimeters", command=lambda: controller.show_frame(PerimeterMenu)).pack()
        button3 = tk.Button(self, text="Volumes", command=lambda: controller.show_frame(VolumeMenu)).pack()
        button4 = tk.Button(self, text="Calculus", command=lambda: controller.show_frame(CalculusMenu)).pack()
        button5 = tk.Button(self, text="Exit", command=controller.destroy).pack()


class AreaMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuText = tk.Label(self, text='Which area formula do you want to use?').pack()

        button1 = tk.Button(self, text="Square", command=lambda: controller.show_frame(AreaSquare)).pack()
        button2 = tk.Button(self, text="Rectangle", command=lambda: controller.show_frame(AreaRectangle)).pack()
        button3 = tk.Button(self, text="Circle", command=lambda: controller.show_frame(AreaCircle)).pack()
        button4 = tk.Button(self, text="Trapezoid", command=lambda: controller.show_frame(AreaTrapezoid)).pack()
        button5 = tk.Button(self, text="Sphere", command=lambda: controller.show_frame(AreaSphere)).pack()
        button6 = tk.Button(self, text="Triangle", command=lambda: controller.show_frame(AreaTriangle)).pack()
        button7 = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(MainMenu)).pack()


class PerimeterMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuText = tk.Label(self, text='Which perimeter formula do you want to use?').pack()

        button1 = tk.Button(self, text="Square", command=lambda: controller.show_frame(PerimeterSquare)).pack()
        button2 = tk.Button(self, text="Rectangle", command=lambda: controller.show_frame(PerimeterRectangle)).pack()
        button3 = tk.Button(self, text="Circle", command=lambda: controller.show_frame(PerimeterCircle)).pack()
        button4 = tk.Button(self, text="Triangle", command=lambda: controller.show_frame(PerimeterTriangle)).pack()
        button5 = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(MainMenu)).pack()


class VolumeMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuText = tk.Label(self, text='Which volume formula do you want to use?').pack()

        button1 = tk.Button(self, text="Cube", command=lambda: controller.show_frame(VolumeCube)).pack()
        button2 = tk.Button(self, text="Rectangular Prism",
                            command=lambda: controller.show_frame(VolumeRectangle)).pack()
        button3 = tk.Button(self, text="Square Pyramid", command=lambda: controller.show_frame(VolumeSqrPyr)).pack()
        button4 = tk.Button(self, text="Cylinder", command=lambda: controller.show_frame(VolumeCylinder)).pack()
        button5 = tk.Button(self, text="Cone", command=lambda: controller.show_frame(VolumeCone)).pack()
        button6 = tk.Button(self, text="Sphere", command=lambda: controller.show_frame(VolumeSphere)).pack()
        button7 = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(MainMenu)).pack()


class CalculusMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuText = tk.Label(self, text='Which calculus formula do you want to use?').pack()

        button1 = tk.Button(self, text="Quadratic", command=lambda: controller.show_frame(Quadratic)).pack()
        button2 = tk.Button(self, text="Distance", command=lambda: controller.show_frame(Distance)).pack()
        button3 = tk.Button(self, text="Slope", command=lambda: controller.show_frame(Slope)).pack()
        button4 = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(MainMenu)).pack()


class AreaSquare(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuText = tk.Label(self, text='Enter length of the side for the square').pack(side="top")

        def squareArea():
            side = float(entry.get())
            label.set('area = ' + str(side * side))

        lengthText = tk.Label(self, text="Side").pack()
        entry = tk.Entry(self, width=40)
        entry.pack()

        label = tk.StringVar()
        ansBox = tk.Label(self, textvariable=label).pack()

        enterButton = tk.Button(self, text="Enter", command=squareArea).pack()
        exitButton = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(AreaMenu)).pack()


class AreaRectangle(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuText = tk.Label(self, text='Enter the length and width of the rectangle').pack()

        def recArea():
            length = float(entryL.get())
            width = float(entryW.get())
            label.set('area = ' + str(length * width))

        lengthText = tk.Label(self, text="Length").pack()
        entryL = tk.Entry(self, width=40)
        entryL.pack()

        lengthText = tk.Label(self, text="Width").pack()
        entryW = tk.Entry(self, width=40)
        entryW.pack()

        label = tk.StringVar()
        ansBox = tk.Label(self, textvariable=label).pack()

        enterButton = tk.Button(self, text="Enter", command=recArea).pack()
        exitButton = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(AreaMenu)).pack()


class AreaCircle(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuText = tk.Label(self, text='Enter the radius of the circle').pack()

        def circArea():
            radius = float(entry.get())
            label.set('area = ' + str(math.pi * (radius ** 2)))

        lengthText = tk.Label(self, text="Radius").pack()
        entry = tk.Entry(self, width=40)
        entry.pack()

        label = tk.StringVar()
        ansBox = tk.Label(self, textvariable=label).pack()

        enterButton = tk.Button(self, text="Enter", command=circArea).pack()
        exitButton = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(AreaMenu)).pack()


class AreaTrapezoid(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuText = tk.Label(self, text='Enter the length of base 1, base 2, and the height').pack()

        def trapArea():
            base1 = float(entryB1.get())
            base2 = float(entryB2.get())
            height = float(entryH.get())
            label.set('area = ' + str(0.5 * (base1 + base2) * height))

        lengthText = tk.Label(self, text="Base 1").pack()
        entryB1 = tk.Entry(self, width=40)
        entryB1.pack()

        lengthText = tk.Label(self, text="Base 2").pack()
        entryB2 = tk.Entry(self, width=40)
        entryB2.pack()

        lengthText = tk.Label(self, text="Height").pack()
        entryH = tk.Entry(self, width=40)
        entryH.pack()

        label = tk.StringVar()
        ansBox = tk.Label(self, textvariable=label).pack()

        enterButton = tk.Button(self, text="Enter", command=trapArea).pack()
        exitButton = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(AreaMenu)).pack()


class AreaSphere(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuText = tk.Label(self, text='Enter the radius of the sphere').pack()

        def sphereArea():
            radius = float(entry.get())
            label.set('area = ' + str(4 * math.pi * (radius ** 2)))

        lengthText = tk.Label(self, text="Radius").pack()
        entry = tk.Entry(self, width=40)
        entry.pack()

        label = tk.StringVar()
        ansBox = tk.Label(self, textvariable=label).pack()

        enterButton = tk.Button(self, text="Enter", command=sphereArea).pack()
        exitButton = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(AreaMenu)).pack()


class AreaTriangle(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuText = tk.Label(self, text='Enter the base and height of the triangle').pack()

        def triArea():
            base = float(entryB.get())
            height = float(entryH.get())
            label.set('area = ' + str(0.5 * base * height))

        lengthText = tk.Label(self, text="Base").pack()
        entryB = tk.Entry(self, width=40)
        entryB.pack()

        lengthText = tk.Label(self, text="Height").pack()
        entryH = tk.Entry(self, width=40)
        entryH.pack()

        label = tk.StringVar()
        ansBox = tk.Label(self, textvariable=label).pack()

        enterButton = tk.Button(self, text="Enter", command=triArea).pack()
        exitButton = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(AreaMenu)).pack()


class PerimeterSquare(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuText = tk.Label(self, text='Enter the side of the square').pack()

        def squarePeri():
            side = float(entry.get())
            label.set('perimeter = ' + str(4 * side))

        lengthText = tk.Label(self, text="Side").pack()
        entry = tk.Entry(self, width=40)
        entry.pack()

        label = tk.StringVar()
        ansBox = tk.Label(self, textvariable=label).pack()

        enterButton = tk.Button(self, text="Enter", command=squarePeri).pack()
        exitButton = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(PerimeterMenu)).pack()


class PerimeterRectangle(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuText = tk.Label(self, text='Enter the length and width of the rectangle').pack()

        def recPeri():
            length = float(entryL.get())
            width = float(entryW.get())
            label.set('perimeter = ' + str((2 * length) + (2 * width)))

        lengthText = tk.Label(self, text="Length").pack()
        entryL = tk.Entry(self, width=40)
        entryL.pack()

        lengthText = tk.Label(self, text="Width").pack()
        entryW = tk.Entry(self, width=40)
        entryW.pack()

        label = tk.StringVar()
        ansBox = tk.Label(self, textvariable=label).pack()

        enterButton = tk.Button(self, text="Enter", command=recPeri).pack()
        exitButton = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(PerimeterMenu)).pack()


class PerimeterCircle(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuText = tk.Label(self, text='Enter the diameter of the circle').pack()

        def circPeri():
            diameter = float(entry.get())
            label.set('perimeter = ' + str(math.pi * diameter))

        lengthText = tk.Label(self, text="Diameter").pack()
        entry = tk.Entry(self, width=40)
        entry.pack()

        label = tk.StringVar()
        ansBox = tk.Label(self, textvariable=label).pack()

        enterButton = tk.Button(self, text="Enter", command=circPeri).pack()
        exitButton = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(PerimeterMenu)).pack()


class PerimeterTriangle(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuText = tk.Label(self, text='Enter the three sides of the triangle').pack()

        def triPeri():
            side1 = float(entry1.get())
            side2 = float(entry2.get())
            side3 = float(entry3.get())
            label.set('perimeter = ' + str(side1 + side2 + side3))

        lengthText = tk.Label(self, text="Side 1").pack()
        entry1 = tk.Entry(self, width=40)
        entry1.pack()

        lengthText = tk.Label(self, text="Side 2").pack()
        entry2 = tk.Entry(self, width=40)
        entry2.pack()

        lengthText = tk.Label(self, text="Side 3").pack()
        entry3 = tk.Entry(self, width=40)
        entry3.pack()

        label = tk.StringVar()
        ansBox = tk.Label(self, textvariable=label).pack()

        enterButton = tk.Button(self, text="Enter", command=triPeri).pack()
        exitButton = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(PerimeterMenu)).pack()


class VolumeCube(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuText = tk.Label(self, text='Enter the side length of the cube').pack()

        def cubeVol():
            side = float(entry.get())
            label.set('volume = ' + str(side * side * side))

        lengthText = tk.Label(self, text="Side").pack()
        entry = tk.Entry(self, width=40)
        entry.pack()

        label = tk.StringVar()
        ansBox = tk.Label(self, textvariable=label).pack()

        enterButton = tk.Button(self, text="Enter", command=cubeVol).pack()
        exitButton = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(VolumeMenu)).pack()


class VolumeRectangle(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuText = tk.Label(self, text='Enter the length, width, and height of the rectangular prism').pack()

        def recPrisVol():
            side1 = float(entry1.get())
            side2 = float(entry2.get())
            side3 = float(entry3.get())
            label.set('volume = ' + str(side1 * side2 * side3))

        lengthText = tk.Label(self, text="Length").pack()
        entry1 = tk.Entry(self, width=40)
        entry1.pack()

        lengthText = tk.Label(self, text="Width").pack()
        entry2 = tk.Entry(self, width=40)
        entry2.pack()

        lengthText = tk.Label(self, text="Height").pack()
        entry3 = tk.Entry(self, width=40)
        entry3.pack()

        label = tk.StringVar()
        ansBox = tk.Label(self, textvariable=label).pack()

        enterButton = tk.Button(self, text="Enter", command=recPrisVol).pack()
        exitButton = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(VolumeMenu)).pack()


class VolumeSqrPyr(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuText = tk.Label(self, text='Enter the base and height of the square pyramid').pack()

        def sqrPyrVol():
            base = float(entryB.get())
            height = float(entryH.get())
            label.set('volume = ' + str((1 / 3) * (base ** 2) * height))

        lengthText = tk.Label(self, text="Base").pack()
        entryB = tk.Entry(self, width=40)
        entryB.pack()

        lengthText = tk.Label(self, text="Height").pack()
        entryH = tk.Entry(self, width=40)
        entryH.pack()

        label = tk.StringVar()
        ansBox = tk.Label(self, textvariable=label).pack()

        enterButton = tk.Button(self, text="Enter", command=sqrPyrVol).pack()
        exitButton = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(VolumeMenu)).pack()


class VolumeCylinder(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuText = tk.Label(self, text='Enter the radius and height of the cylinder').pack()

        def cylVol():
            radius = float(entryR.get())
            height = float(entryH.get())
            label.set('volume = ' + str(math.pi * (radius * radius) * height))

        lengthText = tk.Label(self, text="Radius").pack()
        entryR = tk.Entry(self, width=40)
        entryR.pack()

        lengthText = tk.Label(self, text="Height").pack()
        entryH = tk.Entry(self, width=40)
        entryH.pack()

        label = tk.StringVar()
        ansBox = tk.Label(self, textvariable=label).pack()

        enterButton = tk.Button(self, text="Enter", command=cylVol).pack()
        exitButton = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(VolumeMenu)).pack()


class VolumeCone(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuText = tk.Label(self, text='Enter the radius and height to the cone').pack()

        def coneVol():
            radius = float(entryR.get())
            height = float(entryH.get())
            label.set('volume = ' + str((1 / 3) * math.pi * (radius * radius) * height))

        lengthText = tk.Label(self, text="Radius").pack()
        entryR = tk.Entry(self, width=40)
        entryR.pack()

        lengthText = tk.Label(self, text="Height").pack()
        entryH = tk.Entry(self, width=40)
        entryH.pack()

        label = tk.StringVar()
        ansBox = tk.Label(self, textvariable=label).pack()

        enterButton = tk.Button(self, text="Enter", command=coneVol).pack()
        exitButton = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(VolumeMenu)).pack()


class VolumeSphere(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuText = tk.Label(self, text='Enter the radius for the sphere').pack()

        def sphereVol():
            radius = float(entry.get())
            label.set('volume = ' + str((4 / 3) * math.pi * (radius * radius * radius)))

        lengthText = tk.Label(self, text="Radius").pack()
        entry = tk.Entry(self, width=40)
        entry.pack()

        label = tk.StringVar()
        ansBox = tk.Label(self, textvariable=label).pack()

        enterButton = tk.Button(self, text="Enter", command=sphereVol).pack()
        exitButton = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(VolumeMenu)).pack()


class Quadratic(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuText = tk.Label(self, text='Enter the values for a, b, and c').pack()

        def quad():
            a = float(entry1.get())
            b = float(entry2.get())
            c = float(entry3.get())

            if ((2 * a) == 0):
                label.set("Division by 0!")
            elif ((b * b) - (4 * a * c) < 0):
                label.set("Negative under the square root!")
            else:
                xPos = ((-1 * b) + math.sqrt((b * b) - (4 * a * c))) / (2 * a)
                xNeg = ((-1 * b) - math.sqrt((b * b) - (4 * a * c))) / (2 * a)
                if (xPos == xNeg):
                    label.set('x = ' + str(xPos))
                else:
                    ans = 'x = ' + str(xPos) + ' or x = ' + str(xNeg)
                    label.set(ans)

        lengthText = tk.Label(self, text="a").pack()
        entry1 = tk.Entry(self, width=40)
        entry1.pack()

        lengthText = tk.Label(self, text="b").pack()
        entry2 = tk.Entry(self, width=40)
        entry2.pack()

        lengthText = tk.Label(self, text="c").pack()
        entry3 = tk.Entry(self, width=40)
        entry3.pack()

        label = tk.StringVar()
        ansBox = tk.Label(self, textvariable=label).pack()

        enterButton = tk.Button(self, text="Enter", command=quad).pack()
        exitButton = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(CalculusMenu)).pack()


class Distance(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuText = tk.Label(self, text='Enter the values for (x0, y0) and (x1, y1)').pack()

        def distance():
            x0 = float(entry1.get())
            y0 = float(entry2.get())
            x1 = float(entry3.get())
            y1 = float(entry4.get())
            label.set('distance = ' + str(math.sqrt(((x1 - x0) * (x1 - x0)) + ((y1 - y0) * (y1 - y0)))))

        lengthText = tk.Label(self, text="x0").pack()
        entry1 = tk.Entry(self, width=40)
        entry1.pack()

        lengthText = tk.Label(self, text="y0").pack()
        entry2 = tk.Entry(self, width=40)
        entry2.pack()

        lengthText = tk.Label(self, text="x1").pack()
        entry3 = tk.Entry(self, width=40)
        entry3.pack()

        lengthText = tk.Label(self, text="y1").pack()
        entry4 = tk.Entry(self, width=40)
        entry4.pack()

        label = tk.StringVar()
        ansBox = tk.Label(self, textvariable=label).pack()

        enterButton = tk.Button(self, text="Enter", command=distance).pack()
        exitButton = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(CalculusMenu)).pack()


class Slope(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        menuText = tk.Label(self, text='Enter the values for (x0, y0) and (x1, y1)').pack()

        def slope():
            x0 = float(entry1.get())
            y0 = float(entry2.get())
            x1 = float(entry3.get())
            y1 = float(entry4.get())

            if ((x1 - x0) == 0):
                label.set("Division by 0!")
            else:
                label.set('slope = ' + str((y1 - y0) / (x1 - x0)))

        lengthText = tk.Label(self, text="x0").pack()
        entry1 = tk.Entry(self, width=40)
        entry1.pack()

        lengthText = tk.Label(self, text="y0").pack()
        entry2 = tk.Entry(self, width=40)
        entry2.pack()

        lengthText = tk.Label(self, text="x1").pack()
        entry3 = tk.Entry(self, width=40)
        entry3.pack()

        lengthText = tk.Label(self, text="y1").pack()
        entry4 = tk.Entry(self, width=40)
        entry4.pack()

        label = tk.StringVar()
        ansBox = tk.Label(self, textvariable=label).pack()

        enterButton = tk.Button(self, text="Enter", command=slope).pack()
        exitButton = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(CalculusMenu)).pack()


app = FormulaCalculator()
app.mainloop()
