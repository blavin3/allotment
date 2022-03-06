from tkinter import *

class PumpGUI():
    def __init__(self, pump_frame, pump_id):
        self.duration = 10
        self.pump_id = pump_id
        btn_column = Button(pump_frame, text=f"Pump {pump_id}", 
        height=5, width=20, font = ('Arial' , 35))
        btn_column.grid(column=pump_id, row=0)

        lbfrm_column = LabelFrame(pump_frame, text=f'P{pump_id} Duration (mins)',
            font = ('Arial' , 20), padx=2, pady=22)
        lbfrm_column.grid(column=pump_id, row=1)

        self.lb_lbfrm = Label(lbfrm_column, text=f'{self.duration}',
            font = ('Arial' , 15), height=2, width=10)
        self.lb_lbfrm.grid(column=0, row=0)

        btn_lbfrm = Button(lbfrm_column, text="up", 
            height=2, width=10, font = ('Arial' , 15),
            command=self.up_press)
        btn_lbfrm.grid(column=1, row=0)

        btn_lbfrm = Button(lbfrm_column, text="down", 
            height=2, width=10,font = ('Arial' , 15),
            command=self.down_press)
        btn_lbfrm.grid(column=1, row=1)

    def up_press(self):
        self.duration += 1
        if self.duration == 60:
            self.duration = 0
        self.lb_lbfrm.configure(text=f'{self.duration}')

    def down_press(self):
        self.duration -= 1
        if self.duration == -1:
            self.duration = 59
        self.lb_lbfrm.configure(text=f'{self.duration}')

def main():
    root = Tk()
    width, height = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry('%dx%d+0+0' % (width,height))

    pump_frame = LabelFrame(root, text="Manual Pump Control",
        font = ('Arial' , 35), padx=20, pady=20)
    
    PumpGUI(pump_frame, 0)
    PumpGUI(pump_frame, 1)
    PumpGUI(pump_frame, 2)

    pump_frame.pack()

    root.mainloop()

if __name__ == "__main__":
    main()