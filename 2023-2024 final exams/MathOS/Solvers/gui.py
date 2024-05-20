import tkinter as tk
import importlib
import sys
from screeninfo import get_monitors

monitors = get_monitors()
if len(monitors) == 1:
    x = monitors[0].width
    y = monitors[0].height
else: 
    print('multiple monitors')
    sys.exit()

def button_generator(lib: str, text: str):
    i = importlib.import_module(lib)
    i
    create_text_function_window(text)


def line_functions(function_name: str):
    with open(function_name + ".py", "r") as file:
        Text = file.read()
        line = ""
        lines = []
        for char in Text:
            line = line + char
            if char == "\n" and not line == "def launch():" and not line == "launch()":
                lines.append(line)
                line = ""
    return lines


def create_text_function_window(function_name: str):
    bg_color = "#328563"
    window = tk.Tk()
    window.title(function_name)
    window.geometry(f"{str(int(x / 2))}x{str(int(y / 3))}")
    window.resizable(False, True)
    title = tk.Label(
        window,
        width=int(x / 2),
        text=f"code from: {function_name}",
        font="Georgia 15",
        bg=bg_color,
        fg="white",
    )
    title.pack()
    scrollbar = tk.Scrollbar(window, bg=bg_color)
    scrollbar.pack(side="right", fill="y")
    text = tk.Listbox(
        window,
        yscrollcommand=scrollbar.set,
        width=int(x / 2 - 16),
        bg="#2e2e2e",
        fg="white",
        font="Arial 12",
    )
    lines = line_functions(function_name)
    for line in lines:
        text.insert("end", line)
    text.pack(side="left", fill="both")
    scrollbar.config(command=text.yview)
    window.mainloop()


button_info_list = [
    {"import": "bracketing", "text": "bracketing"},
    {"import": "dichotomy", "text": "dichotomy"},
    {"import": "regula_falsi", "text": "regula_falsi"},
]
"""
    {"import": "newton_raphson","text": "newton_rapshon"},
    {"import":"secant" ,"text": "secant"},
    {"import": "curve tracer","text": "curve_tracer"},
    """


def grid(width, height, square_count):
    def calculate_grid(axis, add):
        grid = []
        x = 0
        while not x >= axis + add:
            grid.append(x)
            x += add
        return grid

    grid_x = calculate_grid(width, height / square_count)
    grid_y = calculate_grid(height, height / square_count)
    return grid_x, grid_y


mainWindow = tk.Tk()
height = y - y / 10
width = x / 2 - x / 10
mainWindow.geometry(str(int(height)) + "x" + str(int(width)))
mainWindow.resizable(False, False)
mainWindow.title("function solvers")
canvas = tk.Canvas(mainWindow, width=width, height=height, bg="white")
canvas.pack()

grid_x, grid_y = grid(width, height, 30)
GRID = []
for i in range(len(grid_x)):
    GRID.append([grid_x[i], grid_y[i]])


def detect_movement(i):
    mouse_pos = (i.x, i.y)
    Pos = [None, None]
    for a in range(len(GRID) - 1):
        if mouse_pos[0] >= GRID[a][0] and mouse_pos[0] < GRID[a + 1][0]:
            Pos[0] = [GRID[a][0], GRID[a + 1][0]]
        if mouse_pos[1] >= GRID[a][1] and mouse_pos[1] < GRID[a + 1][1]:
            Pos[1] = [GRID[a][1], GRID[a + 1][1]]

        if Pos[0] is not None and Pos[1] is not None:
            canvas.create_rectangle(
                Pos[0][0],
                Pos[1][0],
                Pos[0][1],
                Pos[1][1],
                fill="#82AEA5",
                outline="#82AEA5",
            )
            break


mainWindow.bind("<Motion>", detect_movement)

top_bar = tk.Label(
    mainWindow,
    text="Please select method",
    font="Georgia 18",
    height=3,
    width=int(height / 9),
).place(in_=canvas, x=-180)

for button in button_info_list:
    _button = tk.Button(
        mainWindow,
        text=button["text"],
        font="Georgia 12",
        bg="b1AEA2",
        height=4,
        width=16,
        relief="groove",
        command=button_generator(button["import"], button["text"])
    )
    _button.place(in_=canvas, x = width *3/16, y=height *3/16+30)
mainWindow.mainloop