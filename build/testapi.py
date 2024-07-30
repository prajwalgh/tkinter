import requests
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Frame, Label

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\2024\python\Tkinter-Designer-master\Tkinter-Designer-master\myframesd\New folder\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def show_text(text):
    # Clear the content_frame
    for widget in content_frame.winfo_children():
        widget.destroy()

    if text == "Button 1 was clicked":
        response = requests.get('http://127.0.0.1:5000/button1')
        services = response.json()
        for service in services:
            if service == "infra":
                Button(content_frame, text="Infra Button", font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF", command=lambda: print("Infra Button clicked")).pack(pady=5)
            else:
                Label(content_frame, text=service, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF").pack(pady=5)
    elif text == "Button 2 was clicked":
        response = requests.get('http://127.0.0.1:5000/button2')
        servers = response.json()
        for server in servers:
            Label(content_frame, text=server, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF").pack(pady=5)
    elif text == "Button 3 was clicked":
        response = requests.get('http://127.0.0.1:5000/button3')
        ems_servers = response.json()
        for server in ems_servers:
            Label(content_frame, text=server, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF").pack(pady=5)
    elif text == "Button 4 was clicked":
        response = requests.get('http://127.0.0.1:5000/button4')
        services = response.json()
        for service in services:
            Label(content_frame, text=service, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF").pack(pady=5)
    elif text == "Button 5 was clicked":
        response = requests.get('http://127.0.0.1:5000/button5')
        message = response.json()["message"]
        Label(content_frame, text=message, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF").pack(pady=5)
    elif text == "Button 6 was clicked":
        response = requests.get('http://127.0.0.1:5000/button6')
        message = response.json()["message"]
        Label(content_frame, text=message, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF").pack(pady=5)

window = Tk()
window.geometry("1000x800")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=800,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    0.0,
    1000.0,
    140.0,
    fill="#AC7AEB",
    outline="")

canvas.create_text(
    14.0,
    25.0,
    anchor="nw",
    text="Services Monitoring",
    fill="#FFFFFF",
    font=("SairaSemiCondensed SemiBold", 48 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_text("Button 1 was clicked"),
    relief="flat"
)
button_1.place(
    x=436.0,
    y=18.0,
    width=122.0,
    height=46.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_text("Button 2 was clicked"),
    relief="flat"
)
button_2.place(
    x=793.0,
    y=18.0,
    width=122.0,
    height=46.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_text("Button 3 was clicked"),
    relief="flat"
)
button_3.place(
    x=671.0,
    y=18.0,
    width=122.0,
    height=46.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_text("Button 4 was clicked"),
    relief="flat"
)
button_4.place(
    x=558.0,
    y=18.0,
    width=122.0,
    height=46.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_text("Button 5 was clicked"),
    relief="flat"
)
button_5.place(
    x=436.0,
    y=70.0,
    width=122.0,
    height=46.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_text("Button 6 was clicked"),
    relief="flat"
)
button_6.place(
    x=793.0,
    y=70.0,
    width=122.0,
    height=46.0
)

# Create a frame to hold the content that will change
content_frame = Frame(window, bg="#FFFFFF")
content_frame.place(x=0, y=140, width=1000, height=660)

window.resizable(False, False)
window.mainloop()
