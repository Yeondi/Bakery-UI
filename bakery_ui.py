import tkinter
from tkinter import *


class BakeryView:
    def __init__(self, window):
        self.__init_window(window)

    def __init_window(self, window):
        window.title("빵집")
        window.geometry('400x200')
        label = Label(window, text='주문내역')
        label.pack()
        self.orderText = Text(window)
        self.orderText.pack()

    def add_order(self, orders):
        self.orderText.insert(0.0, orders + "\n")


class CustomerView:
    def __init__(self, name, window, bakery_view):
        self.name = name
        self.__init_window(window)
        self.bakeryView = bakery_view

    def __init_window(self, window):
        window.title("고객: " + self.name)
        self.sandwich = Label(window,text="샌드위치 (5000원)")
        self.sandwich.grid(column = 0,row=0)
        self.input_entry = Entry(window,width=10)
        self.input_entry.grid(column=1,row=0)
        self.cake = Label(window, text='케이크 (20000원)')
        self.cake.grid(column = 0,row=1)
        self.input_entry2 = Entry(window,width=10)
        self.input_entry2.grid(column=1,row=1)

        self.btn = Button(window,text="주문하기",command=self.send_order)
        self.btn.grid(column=0,row=2)

        self.btn.bind("<Return>",self.send_order)

        window.geometry('350x200')

    def send_order(self):
        order_text = ""
        try:#문자가 아니면서 0보다 큰 int
            if int(self.input_entry.get()) > 0 or int(self.input_entry2.get()) > 0:
                order_text += self.name
            if int(self.input_entry.get()) > 0 : #숫자가 아닐경우
                order_text+= ": " + self.sandwich.cget("text") + " " + self.input_entry.get() + "개"
                if int(self.input_entry2.get()) > 0:
                    order_text+=", "
            if int(self.input_entry2.get()) > 0:
                order_text += ": " + self.cake.cget("text")+ " " + self.input_entry2.get()+"개"
        except:
            try:
                if int(self.input_entry2.get()) > 0:
                    order_text = self.name
                if int(self.input_entry2.get()) > 0:
                    order_text += ": " + self.cake.cget("text")+ " " + self.input_entry2.get()+"개"
            except:
                order_text += ""


        self.bakeryView.add_order(order_text)


if __name__ == '__main__':
    app = Tk()
    bakery = BakeryView(app)
    CustomerView('고객A', Toplevel(app), bakery)
    CustomerView('고객B', Toplevel(app), bakery)
    app.mainloop()
