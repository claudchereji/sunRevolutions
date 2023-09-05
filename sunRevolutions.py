import tkinter as tk
from tkinter import ttk
import datetime


def calculate_sun_revolutions():
    year = int(year_entry.get())
    month = int(month_entry.get())
    day = int(day_entry.get())
    date1 = datetime.date(year, month, day)
    current_date = datetime.date.today()
    time_difference = current_date - date1
    days_difference = time_difference.days
    result_label.config(text=f"So according to my calculations, \nyou've lived through {days_difference} sun revolutions!")


root = tk.Tk()
root.title('Sun Revolutions Calculator')

frame = ttk.Frame(root)
frame.pack(pady=20, padx=20, expand=True)

name_label = ttk.Label(frame, text="What's your name?")
name_label.grid(row=0, column=0, columnspan=3, pady=10)

name_entry = ttk.Entry(frame)
name_entry.grid(row=1, column=0, columnspan=3, pady=10)

dob_label = ttk.Label(frame, text="Enter your date of birth:")
dob_label.grid(row=2, column=0, columnspan=3, pady=10)

year_label = ttk.Label(frame, text="Year")
year_label.grid(row=3, column=0)
year_entry = ttk.Entry(frame, width=5)
year_entry.grid(row=4, column=0, pady=10, padx=5)

month_label = ttk.Label(frame, text="Month")
month_label.grid(row=3, column=1)
month_entry = ttk.Entry(frame, width=3)
month_entry.grid(row=4, column=1, pady=10, padx=5)

day_label = ttk.Label(frame, text="Day")
day_label.grid(row=3, column=2)
day_entry = ttk.Entry(frame, width=3)
day_entry.grid(row=4, column=2, pady=10, padx=5)

calculate_button = ttk.Button(frame, text="Calculate", command=calculate_sun_revolutions)
calculate_button.grid(row=5, column=0, columnspan=3, pady=20)

result_label = ttk.Label(frame, text="")
result_label.grid(row=6, column=0, columnspan=3, pady=20)

root.mainloop()