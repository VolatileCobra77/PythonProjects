import math
import PySimpleGUI as sg

print("Starting!")
# Define the GUI layout
layout = [[sg.Text("Select a shape to calculate:")],
          [
                  sg.Radio("Triangular Prism(Base,Legnth and Height ONLY)",
                           "SHAPE",
                           key="-TRIANGULAR_PRISM-",
                           default=True)
          ],
          [
                  sg.Radio("Rectangular Prism(Base, Legnth and Height ONLY)",
                           "SHAPE",
                           key="-RECTANGULAR_PRISM-")
          ],
          [
                  sg.Radio("Cylinder(Radius and Height ONLY)",
                           "SHAPE",
                           key="-CYLINDER-")
          ], [sg.Text("Enter the dimensions:")],
          [sg.Text("Base:"), sg.InputText(key="-BASE-")],
          [sg.Text("Height:"),
           sg.InputText(key="-HEIGHT-")],
          [sg.Text("Length:"),
           sg.InputText(key="-LENGTH-")],
          [sg.Text("Radius:"),
           sg.InputText(key="-RADIUS-")],
          [
                  sg.Radio("Surface Area",
                           "CALCULATION",
                           key="-SURFACE_AREA-",
                           default=True)
          ], [sg.Radio("Volume", "CALCULATION", key="-VOLUME-")],
          [sg.Button("Calculate"),
           sg.Button("Clear"),
           sg.Button("Exit")],
          [sg.Text("Result:"),
           sg.Text(size=(100, 1), key="-OUTPUT-")]]

# Create the GUI window
window = sg.Window("Shape Calculator", layout)


# Define the functions for calculating surface areas and volumes
def surface_area_triangular_prism(base, height, length):
        return base * height + length * math.sqrt(base**2 +
                                                  height**2) + length * base


def volume_triangular_prism(base, height, length):
        return (base * height * length) / 2


def surface_area_rectangular_prism(base, height, length):
        return 2 * (base * height + base * length + height * length)


def volume_rectangular_prism(base, height, length):
        return base * height * length


def surface_area_cylinder(radius, height):
        return 2 * math.pi * radius * height + 2 * math.pi * radius**2


def volume_cylinder(radius, height):
        return math.pi * radius**2 * height


print("running main loop")
# Main event loop
while True:
        
        event, values = window.read()
        print(event)
        if event == "Exit" or event == sg.WIN_CLOSED:
                break

        if event == "Clear":
                window["-BASE-"].update("")
                window["-HEIGHT-"].update("")
                window["-LENGTH-"].update("")
                window["-RADIUS-"].update("")
                window["-OUTPUT-"].update("")

        if event == "Calculate":
                print("calculate clicked!")
                if values["-TRIANGULAR_PRISM-"]:
                        base = float(values["-BASE-"])
                        height = float(values["-HEIGHT-"])
                        length = float(values["-LENGTH-"])
                        if values["-SURFACE_AREA-"]:
                                print("surface area selected")
                                result = surface_area_triangular_prism(
                                        base, height, length)
                        else:
                                print("volume selected")
                                result = volume_triangular_prism(
                                        base, height, length)
                        window["-OUTPUT-"].update(result)

                elif values["-RECTANGULAR_PRISM-"]:

                        base = float(values["-BASE-"])
                        height = float(values["-HEIGHT-"])
                        length = float(values["-LENGTH-"])
                        if values["-SURFACE_AREA-"]:
                                result = surface_area_rectangular_prism(
                                        base, height, length)
                        else:
                                result = volume_rectangular_prism(
                                        base, height, length)
                        window["-OUTPUT-"].update(result)

                elif values["-CYLINDER-"]:
                        radius = float(values["-RADIUS-"])
                        height = float(values["-HEIGHT-"])
                        if values["-SURFACE_AREA-"]:
                                result = surface_area_cylinder(radius, height)
                        else:
                                result = volume_cylinder(radius, height)

                        window["-OUTPUT-"].update(result)
      
        print(event)
window.close()
