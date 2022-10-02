import tkinter as tk
import csv
import threading
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)  # output to console

root = tk.Tk()
root.geometry('600x400')


# enable / disable button
def toggle_button_interactivity(btn: tk.Button):
    if btn['state'] == "normal":
        btn["state"] = "disable"
        btn["text"] = "Writing..."
    else:
        btn['state'] = "normal"
        btn["text"] = "write to file"


def save_file(btn):
    toggle_button_interactivity(btn)
    with open("mytextfile.csv", "w", newline="") as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL, delimiter=',')

        for i in range(10000000):
            wr.writerow("test")

        logger.info("Finished writing csv")  # info to console
        toggle_button_interactivity(btn)


def say_hi():
    print("Hi")


def write_file_in_thread(btn: tk.Button):
    t = threading.Thread(target=save_file, args=(btn,))
    t.start() # если ниже напишу t.join(), то будет ждать пока этот тред закончится, т.е. не будет интерактивности.
    print("writing...")


b1 = tk.Button(text="write to file", width=15, height=3)
b1.config(command=lambda: write_file_in_thread(b1))  # pass arguments via lambda
b1.pack()

b2 = tk.Button(text="Say Hi", width=15, height=3)
b2.config(command=say_hi)
b2.pack()

root.mainloop()
