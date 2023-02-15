from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Notebook


class Window:
    def __init__(self, width, heidth, title="suw", icon=None):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{heidth}+1000+200")
        # self.root.resizable(resizable[0], resizable[1])
        # self.root["background"] = "blue"
        if icon:
            self.root.iconbitmap(icon)

        self.tabs_control = Notebook(self.root, height=100, width=30)
        self.tab_1 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_1, text="Вычисление", underline=0)

        self.bir = IntVar()
        self.eki = IntVar()
        self.ush = IntVar()
        self.tort = IntVar()
        self.bes = IntVar()
        self.alti = IntVar()
        self.jeti = IntVar()
        self.segiz = IntVar()
        self.togiz = IntVar()

        self.lb1 = Label
        self.count = 0

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        self.draw_menu()
        self.tabs_control.pack(fill=BOTH, expand=1)

        Label(self.tab_1, anchor=W, padx=15, pady=5, text="Канша метрде суу бар?").grid(row=0, column=0, sticky=W)
        Label(self.tab_1, anchor=W, padx=15, pady=5, text="Суудын Минерализациясы?").grid(row=1, column=0, sticky=W)
        Label(self.tab_1, anchor=W, padx=15, pady=5, text="Суудын колумы?").grid(row=2, column=0, sticky=W)
        Label(self.tab_1, anchor=W, padx=15, pady=5, text="Жердын катламы?").grid(row=3, column=0, sticky=W)
        Label(self.tab_1, anchor=W, padx=15, pady=5, text="Суудын шорлыгы?").grid(row=4, column=0, sticky=W)
        Label(self.tab_1, anchor=W, padx=15, pady=5, text="Жердын шорлыгы?").grid(row=5, column=0, sticky=W)
        Label(self.tab_1, anchor=W, padx=15, pady=5, text="Дарья катламы?").grid(row=6, column=0, sticky=W)
        Label(self.tab_1, anchor=W, padx=15, pady=5, text="Еныне неше метр?").grid(row=7, column=0, sticky=W)
        Label(self.tab_1, anchor=W, padx=15, pady=5, text="Узынына неше метр?").grid(row=8, column=0, sticky=W)

        Entry(self.tab_1, width=7, textvariable=self.bir, justify=RIGHT).grid(row=0, column=2, sticky=E)
        Entry(self.tab_1, width=7, textvariable=self.eki, justify=RIGHT).grid(row=1, column=2, sticky=E)
        Entry(self.tab_1, width=7, textvariable=self.ush, justify=RIGHT).grid(row=2, column=2, sticky=E)
        Entry(self.tab_1, width=7, textvariable=self.tort, justify=RIGHT).grid(row=3, column=2, sticky=E)
        Entry(self.tab_1, width=7, textvariable=self.bes, justify=RIGHT).grid(row=4, column=2, sticky=E)
        Entry(self.tab_1, width=7, textvariable=self.alti, justify=RIGHT).grid(row=5, column=2, sticky=E)
        Entry(self.tab_1, width=7, textvariable=self.jeti, justify=RIGHT).grid(row=6, column=2, sticky=E)
        Entry(self.tab_1, width=7, textvariable=self.segiz, justify=RIGHT).grid(row=7, column=2, sticky=E)
        Entry(self.tab_1, width=7, textvariable=self.togiz, justify=RIGHT).grid(row=8, column=2, sticky=E)

        Button(self.tab_1, text="Старт", width=10, command=self.start).grid(row=8, column=3)

    def start(self):
        Button(self.tab_1, text="Выйти", width=10, command=self.root.destroy).grid(row=8, column=3)
        if self.bir and self.eki and self.ush and self.tort and self.bes and self.alti\
                and self.jeti and self.segiz and self.togiz == 0:
            mb.showerror("Qatelik!", "Belgilerdin ishi tolmagan!!!")
        elif self.bir and self.eki and self.ush and self.tort and self.bes and self.alti\
                and self.jeti and self.segiz and self.togiz:
            tab_2 = Frame(self.tabs_control, height=100, width=400)
            self.tabs_control.add(tab_2, text="Выделение", underline=0)
            self.tabs_control.select(tab_2)
            a = self.segiz.get()
            b = self.togiz.get()
            c = a/200 * b/200
            d = a/150 * b/150
            basseyn = int(c)
            skvojina = int(d)
            if a > 1500:
                inf = "kerek"
            elif b > 1500:
                inf = "kerek"
            else:
                inf = "kerek emes"
            vert = str(b)
            gorz = str(a)
            aa = self.ush.get()
            bb = aa - 20
            kun_suw = bb
            sagat_suw = (bb / 30) * 10
            minut_suw = sagat_suw / 360
            sekund_suw = minut_suw / 360
            rezelval = 1
            Label(tab_2, text=f"{str( skvojina )}-Skovina ketedi", padx=15, pady=5).grid(row=0, sticky=W, column=0)
            Label(tab_2, text=f"{str( basseyn )}-Basseyn ketedi", padx=15, pady=5).grid(row=1, sticky=W, column=0)
            Label(tab_2, text=f"informatcion kanal {inf}", padx=15, pady=5).grid(row=2, sticky=W, column=0)
            Label(tab_2, text=f"Vertikalina-{str(vert)} metr", padx=15, pady=5).grid(row=3, sticky=W, column=0)
            Label(tab_2, text=f"gorizontalina-{str(gorz)} metr", padx=15, pady=5).grid(row=4, sticky=W, column=0)
            Label(tab_2, text=f"Kunine-{str(kun_suw)} metr3", padx=15, pady=5).grid(row=5, sticky=W, column=0)
            Label(tab_2, text=f"Sagatina-{str( sagat_suw )} metr3", padx=15, pady=5).grid(row=6, sticky=W, column=0)
            Label(tab_2, text=f"Sekuntina-{str( sekund_suw )} metr3", padx=15, pady=5).grid(row=7, sticky=W, column=0)
            Label(tab_2, text=f"{str( rezelval )}-qoyladi", padx=15, pady=5).grid(row=8, sticky=W, column=0)
            self.gr(a, b, basseyn, skvojina, inf)
            if self.count > 1:
                self.tabs_control.forget(tab_2)
            else:
                self.count += 1

    def gr(self, wi, he, ba, sk, inf):
        tab_3 = Frame(self.tabs_control, height=he, width=wi)
        self.tabs_control.add(tab_3, text="Графикa", underline=0)
        canvas = Canvas(tab_3, height=he/4+200, width=wi/4)
        canvas.create_rectangle(0, 0, wi/4, he/4, fill="orange")
        if inf == "kerek":
            canvas.create_line(0, 0, wi/4, he/4, fill="cyan", width=3)
        b = 25
        d = int(round(wi/200))
        z = 0
        darmen = 1
        while darmen:
            a = 25
            for j in range(d):
                if z == ba:
                    darmen = 0
                    d = 0
                else:
                    canvas.create_rectangle(a, b, a+4, b+4, fill="blue", outline="blue")
                    z += 1
                    a += 50
            b += 50
            canvas.place(x=0, y=0)
        b1 = 18.75
        d1 = int(round(wi / 150))
        z1 = 0
        darmen1 = 1
        while darmen1:
            a1 = 18.75
            for j in range(d1):
                if z1 == sk:
                    darmen1 = 0
                    d1 = 0
                else:
                    canvas.create_rectangle(a1, b1, a1 + 3, b1 + 3, fill="black", outline="black")
                    z1 += 1
                    a1 += 37.5
            b1 += 37.5

            canvas.create_rectangle(10, he/4+10, 10+4, he/4+14, fill="blue", outline="blue")
            canvas.create_text(40, he/4+11, text="-Бассейн")

            canvas.create_rectangle(10, he/4+20, 10+4, he/4+24, fill="black", outline="black")
            canvas.create_text(40, he/4+21, text="-скожина")

            canvas.create_line(10, he/4+30, 30, he/4+30, fill="cyan", width=3)
            canvas.create_text(50, he/4+30, text="-канал")
            canvas.place(x=0, y=0)

    def draw_menu(self):
        menu_bar = Menu(self.root)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Выйти", command=self.exit)

        menu_bar.add_cascade(label="Файл", menu=file_menu)
        self.root.configure(menu=menu_bar)

    def exit(self):
        choice = mb.askokcancel("Quit?", "Do you to quit?")
        if choice:
            self.root.destroy()


if __name__ == "__main__":
    window = Window(320, 290, "PROEKT")
    window.run()
