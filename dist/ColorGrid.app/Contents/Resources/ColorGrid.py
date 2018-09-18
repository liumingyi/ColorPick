# encoding=utf-8
"""
Create by Mingyi on 2018/9/6 4:32 PM
"""

from tkinter import *

from Config import color_list_file


def selectColor(event):
    cell = canvas.find_closest(event.x, event.y)[0]
    cell_color = canvas.gettags(cell)[0]
    # print(">> {} <<".format(cell_color))
    root.clipboard_clear()
    root.clipboard_append(cell_color)


def drawColorGrid(size, count):
    for i in range(count):
        color = colors[i]
        column = i % 14
        row = i // 14
        item = canvas.create_rectangle(size * column, size * row, size * (column + 1), size * (row + 1), fill=color,
                                       tag=color)
        canvas.tag_bind(item, "<Button-1>", selectColor)


# print("Started!")

root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.title("点击颜色即可复制代码")

canvas = Canvas(root, width=280, height=380)
canvas.pack(fill='both', expand=True)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))

cell_size = 20
# colors = ['red', 'yellow', 'blue', 'white', 'black', 'red', 'yellow', 'blue', 'white', 'black', ]


with open(color_list_file, 'r', encoding='utf-8') as f:
    colorstr = f.read()
    colors = colorstr.split(",")

total = len(colors)

# 绘制颜色表格
drawColorGrid(cell_size, total)

root.mainloop()
