from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Frame, Label
import requests

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"D:\2024\python\Tkinter-Designer-master\Tkinter-Designer-master\myframesd\New folder\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# def show_text(text):
#     # Clear the content_frame
#     for widget in content_frame.winfo_children():
#         widget.destroy()
#
#     #service
#     if text=="Button 4 was clicked":
#         # Add new content (13 server names)
#         service=["ABB","KUKA","TECHNO","EMS"]
#         for i in service:
#             Label(content_frame, text=i, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF").pack(pady=5)
#     #log
#     elif text=="Button 2 was clicked":
#         # Add new content (13 server names)
#         for i in range(13):
#             server_name = f"Server {i + 1}"
#             Label(content_frame, text=server_name, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF").pack(pady=5)
#     #ems
#     elif text=="Button 3 was clicked":
#         # Add new content (13 server names)
#         for i in range(6):
#             server_name = f"ems {i + 1}"
#             Label(content_frame, text=server_name, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF").pack(pady=5)
#     elif text=="Button 1 was clicked":
#         # Add new content
#         service = ["SQL_exe", "infra", "reminder", "EMS"]
#         for i in service:
#             if i == "infra"or i =="SQL_exe":
#                 # code to show button
#                 Button(content_frame, text=i, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF", command=lambda: print("call api")).pack(pady=5)
#
#             else:
#                 Label(content_frame, text=i, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF").pack(pady=5)

# def show_text(text):
#     # Clear the content_frame
#     for widget in content_frame.winfo_children():
#         widget.destroy()
#
#     if text == "Button 1 was clicked":
#         response = requests.get('http://127.0.0.1:5000/button1')
#         services = response.json()
#         for service in services:
#             if service == "infra":
#                 Button(content_frame, text="Infra Button", font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF", command=lambda: print("Infra Button clicked")).pack(pady=5)
#
#             else:
#                 Label(content_frame, text=service, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF").pack(pady=5)
#     elif text == "Button 2 was clicked":
#         response = requests.get('http://127.0.0.1:5000/button2')
#         servers = response.json()
#         for server in servers:
#             Label(content_frame, text=server, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF").pack(pady=5)
#     elif text == "Button 3 was clicked":
#         response = requests.get('http://127.0.0.1:5000/button3')
#         ems_servers = response.json()
#         for server in ems_servers:
#             Label(content_frame, text=server, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF").pack(pady=5)
#     elif text == "Button 4 was clicked":
#         response = requests.get('http://127.0.0.1:5000/button4')
#         services = response.json()
#         for service in services:
#             Label(content_frame, text=service, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF").pack(pady=5)
#     elif text == "Button 5 was clicked":
#         response = requests.get('http://127.0.0.1:5000/button5')
#         message = response.json()["message"]
#         Label(content_frame, text=message, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF").pack(pady=5)
#     elif text == "Button 6 was clicked":
#         response = requests.get('http://127.0.0.1:5000/button6')
#         message = response.json()["message"]
#         Label(content_frame, text=message, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF").pack(pady=5)
def show_text(text):
    # Clear the content_frame
    for widget in content_frame.winfo_children():
        widget.destroy()

    if text == "Button 1":
        response = requests.get('http://127.0.0.1:5000/button1')
        services = response.json()
        for service in services:
            if service == "infra":
                Button(content_frame, text="Infra Button", font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF", command=lambda: print("Infra Button clicked")).pack(pady=5, anchor="w")
            else:
                Label(content_frame, text=service, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF").pack(pady=5, anchor="w")
    elif text == "Button 2":
        response = requests.get('http://127.0.0.1:5000/button2')
        servers = response.json()
        for server in servers:
            Label(content_frame, text=server, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF").pack(pady=5, anchor="w")
    elif text == "Button 3":
        response = requests.get('http://127.0.0.1:5000/button3')
        ems_servers = response.json()
        for server in ems_servers:
            Label(content_frame, text=server, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF").pack(pady=5, anchor="w")
    elif text == "Button 4":
        response = requests.get('http://127.0.0.1:5000/button4')
        services = response.json()
        for service in services:
            Label(content_frame, text=service, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF").pack(pady=5, anchor="w")
    elif text == "Button 5":
        response = requests.get('http://127.0.0.1:5000/button5')
        message = response.json()["message"]
        Label(content_frame, text=message, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF").pack(pady=5, anchor="w")
    elif text == "Button 6":
        response = requests.get('http://127.0.0.1:5000/button6')
        message = response.json()["message"]
        Label(content_frame, text=message, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF").pack(pady=5, anchor="w")

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


# button_image_1 = PhotoImage(file=relative_to_assets("button_1NOTEXT.png"))
# button_1 = Button(
#     image=button_image_1,
#     text="Button 1",  # Text to be displayed on the button
#     font=("SairaSemiCondensed SemiBold", 12),  # Font and size for the text
#     borderwidth=0,
#     highlightthickness=0,
#     activebackground="#AC7AEB",
#     activeforeground="#FFFFFF",
#     command=lambda: show_text("Button 1 was clicked"),
#     relief="flat",
#     compound="center"  # Display the text on top of the image
# )
# button_1.place(x=436.0, y=18.0, width=122.0, height=46.0)

# List of button configurations
buttons_config = [
    ("button_1NOTEXT.png", "Button 1", 436.0, 18.0),
    ("button_1NOTEXT.png", "Button 2", 793.0, 18.0),
    ("button_1NOTEXT.png", "Button 3", 671.0, 18.0),
    ("button_1NOTEXT.png", "Button 4", 558.0, 18.0),
    ("button_1NOTEXT.png", "Button 1", 436.0, 80.0),
    ("button_1NOTEXT.png", "Button 2", 558.0, 80.0),

]

# Create buttons using enumerate
for i, (image_path, text, x, y) in enumerate(buttons_config):
    button_image = PhotoImage(file=relative_to_assets(image_path))
    button = Button(
        image=button_image,
        text=text,
        font=("SairaSemiCondensed SemiBold", 12),
        borderwidth=0,
        highlightthickness=0,
        activebackground="#AC7AEB",
        activeforeground="#FFFFFF",
        command=lambda t=text: show_text(f"{t}"),
        relief="flat",
        compound="center"
    )
    button.image = button_image  # Keep a reference to the image
    button.place(x=x, y=y, width=122.0, height=46.0)

# button_image_2 = PhotoImage(
#     file=relative_to_assets("button_2.png"))
# button_2 = Button(
#     image=button_image_2,
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: show_text("Button 2 was clicked"),
#     relief="flat"
# )
# button_2.place(
#     x=793.0,
#     y=18.0,
#     width=122.0,
#     height=46.0
# )
#
# button_image_3 = PhotoImage(
#     file=relative_to_assets("button_3.png"))
# button_3 = Button(
#     text="hi",
#     image=button_image_3,
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: show_text("Button 3 was clicked"),
#     relief="flat"
# )
# button_3.place(
#     x=671.0,
#     y=18.0,
#     width=122.0,
#     height=46.0
# )
#
# button_image_4 = PhotoImage(
#     file=relative_to_assets("button_4.png"))
# button_4 = Button(
#     image=button_image_4,
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: show_text("Button 4 was clicked"),
#     relief="flat"
# )
# button_4.place(
#     x=558.0,
#     y=18.0,
#     width=122.0,
#     height=46.0
# )
#
# # Create a frame to hold the content that will change
content_frame = Frame(window, bg="#FFFFFF")
content_frame.place(x=0, y=140, width=1000, height=660)

# Add default text to the content_frame
default_text = "Welcome! Please click a button to display content."
Label(content_frame, text=default_text, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF").pack(pady=20)

window.resizable(False, False)
window.mainloop()
