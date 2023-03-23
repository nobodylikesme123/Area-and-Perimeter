'''
Zavier Philpot
Area and Perimeter

'''

import tkinter as tk

def on_shape_selected(shape):
    print(f"You selected the {shape} shape")

root = tk.Tk()
root.title("Select a shape")

circle_btn = tk.Button(root, text="Circle", command=lambda: on_shape_selected("circle"))
circle_btn.pack()

triangle_btn = tk.Button(root, text="Triangle", command=lambda: on_shape_selected("triangle"))
triangle_btn.pack()

square_btn = tk.Button(root, text="Square", command=lambda: on_shape_selected("square"))
square_btn.pack()

rectangle_btn = tk.Button(root, text="Rectangle", command=lambda: on_shape_selected("rectangle"))
rectangle_btn.pack()

root.mainloop()
