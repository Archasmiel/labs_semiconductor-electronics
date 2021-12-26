import tkinter as tk
from tkscrolledframe import ScrolledFrame


def make_window(title, size, labels):
    root = tk.Tk()
    root.title(title)
    root.geometry(size)

    frame_top = tk.Frame(root, width=int(size.split('x')[0]), height=int(size.split('x')[1]))
    frame_top.pack(side="top", expand=1, fill="both")

    sf = ScrolledFrame(frame_top, width=380, height=240)
    sf.pack(side="top", expand=1, fill="both")

    sf.bind_arrow_keys(frame_top)
    sf.bind_scroll_wheel(frame_top)
    frame = sf.display_widget(tk.Frame)

    for i in labels:
        w = tk.Text(frame, height=1, borderwidth=0)
        w.tag_configure("center", justify='center')
        w.insert(1.0, i)
        w.tag_add("center", "1.0", "end")
        w.pack()

    root.mainloop()
