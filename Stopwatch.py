import tkinter as ui

class Stopwatch:
    def __init__(self, master):
        self.master = master
        master.title("Stopwatch")

        self.running = False
        self.time_elapsed = 0 

        self.label = ui.Label(master, text="00:00:00", font=('Arial', 48))
        self.label.pack()

        self.start_button = ui.Button(master, text="Start", command=self.start)
        self.start_button.pack(side=ui.LEFT)

        self.stop_button = ui.Button(master, text="Stop", command=self.stop)
        self.stop_button.pack(side=ui.LEFT)

        self.reset_button = ui.Button(master, text="Reset", command=self.reset)
        self.reset_button.pack(side=ui.LEFT)

        self.update_clock()

    def update_clock(self):
        if self.running:
            self.time_elapsed += 1
            hours, remainder = divmod(self.time_elapsed, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        self.master.after(1000, self.update_clock)

    def start(self):
        if not self.running:
            self.running = True

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        self.running = False
        self.time_elapsed = 0
        self.label.config(text="00:00:00")

if __name__ == "__main__":
    root = ui.Tk()
    stopwatch = Stopwatch(root)
    root.mainloop()
