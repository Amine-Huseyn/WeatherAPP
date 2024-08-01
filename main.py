from tkinter import *
from tkinter import messagebox
from bs4 import BeautifulSoup
import requests

window = Tk()
window.title("Weather APP")
window.geometry("500x700")
window.config(bg="#6dc9f3")

img = PhotoImage(file="cloud.png")
img_label = Label(image=img, bg="#6dc9f3")
img_label.place(x=-10, y=-80)

question_label = Label(text="Enter City", fg="white", font=('Arial', 15, 'bold'), bg="black")
question_label.place(x=210, y=200)

question_entry = Entry(width=30, font=('Helvetica', 10, 'bold'))
question_entry.focus()
question_entry.place(x=155, y=240)

search_icon = PhotoImage(file="search.png")
temp_icon = PhotoImage(file="temp.png")
sky_icon = PhotoImage(file="skyicon.png")
time_icon = PhotoImage(file="timeicon.png")

def fetch_weather():
    city = question_entry.get()
    url = f"https://www.google.com/search?q=weather{city}"

    if question_entry.get() == "":
        messagebox.showerror(title="Error", message="Please enter a city name !")
    else:
        try:
            html = requests.get(url).content
            soup = BeautifulSoup(html, 'html.parser')
            temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
            std = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
            data = std.split('\n')
            time = data[0]
            sky = data[1]

            temp_output_label = Label(text=f"Temperature: {temp}", font=('Helvetica', 15, 'bold'), bg="#6dc9f3")
            temp_output_label.place(x=200, y=450)

            temp_icon_label = Label(image=temp_icon, bg="#6dc9f3")
            temp_icon_label.place(x=95, y=420)

            time_output_label = Label(text=f"Time: {time}", font=('Helvetica', 15, 'bold'), bg="#6dc9f3")
            time_output_label.place(x=200, y=530)

            time_icon_label = Label(image=time_icon, bg="#6dc9f3")
            time_icon_label.place(x=115, y=523)

            sky_output_label = Label(text=f"Sky: {sky}", font=('Helvetica', 15, 'bold'), bg="#6dc9f3")
            sky_output_label.place(x=200, y=610)

            sky_icon_label = Label(image=sky_icon, bg="#6dc9f3")
            sky_icon_label.place(x=102, y=590)

        except Exception as e:
            messagebox.showerror("Error", "Unable to fetch weather data !")


info_button = Button(image=search_icon, width=105, command=fetch_weather)
exit_button = Button(text="Exit", width=10, command=lambda: window.destroy(), font=('Helvetica', 13, 'bold'))
exit_button.place(x=205, y=370)
info_button.place(x=205, y=300)

window.mainloop()