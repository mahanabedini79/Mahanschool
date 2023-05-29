from tkinter import *
from khayyam import JalaliDate

def convert_date():
    # get the input values from the user
    jalali_year = int(year_entry.get())
    jalali_month = int(month_entry.get())
    jalali_day = int(day_entry.get())
    
    # create a JalaliDate object
    jalali_date = JalaliDate(jalali_year, jalali_month, jalali_day)
    
    # convert the JalaliDate object to a GregorianDate object
    gregorian_date = jalali_date.to_gregorian()
    
    # display the output to the user
    output_label.config(text=f"{gregorian_date.year}/{gregorian_date.month}/{gregorian_date.day}")

# create the main window
window = Tk()
window.title("Jalali to Gregorian Date Converter")

# create the input fields
year_label = Label(window, text="Jalali Year:")
year_label.grid(row=0, column=0, padx=10, pady=10)
year_entry = Entry(window)
year_entry.grid(row=0, column=1)

month_label = Label(window, text="Jalali Month:")
month_label.grid(row=1, column=0, padx=10, pady=10)
month_entry = Entry(window)
month_entry.grid(row=1, column=1)

day_label = Label(window, text="Jalali Day:")
day_label.grid(row=2, column=0, padx=10, pady=10)
day_entry = Entry(window)
day_entry.grid(row=2, column=1)

# create the convert button
convert_button = Button(window, text="Convert", command=convert_date)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# create the output label
output_label = Label(window, text="")
output_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# start the main loop
window.mainloop()
