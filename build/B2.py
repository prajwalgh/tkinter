from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Frame, Label

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"D:\2024\python\Tkinter-Designer-master\Tkinter-Designer-master\myframesd\New folder\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Define the functions that replace the API calls
def get_button1_data():
    return ["SQL_exe", "infra", "reminder", "EMS"]

def get_button2_data():
    return [f"Server {i + 1}" for i in range(13)]

def get_button3_data():
    return [f"ems {i + 1}" for i in range(6)]

def get_button4_data():
    return ["ABB", "KUKA", "TECHNO", "EMS"]

def get_button5_data():
    return {"message": "Button 5 was clicked"}

def get_button6_data():
    return {"message": "Button 6 was clicked"}

def show_text(text):
    # Clear the content_frame
    for widget in content_frame.winfo_children():
        widget.destroy()

    if text == "Button 1":
        services = get_button1_data()
        for service in services:
            if service == "infra":
                Button(content_frame, text="Infra Button", font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF", command=lambda: print("Infra Button clicked")).pack(pady=5, anchor="w")
            else:
                Label(content_frame, text=service, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF").pack(pady=5, anchor="w")
    elif text == "Button 2":
        servers = get_button2_data()
        for server in servers:
            Label(content_frame, text=server, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF").pack(pady=5, anchor="w")
    elif text == "Button 3":
        ems_servers = get_button3_data()
        for server in ems_servers:
            Label(content_frame, text=server, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF").pack(pady=5, anchor="w")
    elif text == "Button 4":
        services = get_button4_data()
        for service in services:
            Label(content_frame, text=service, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF").pack(pady=5, anchor="w")
    elif text == "Button 5":
        message = get_button5_data()["message"]
        Label(content_frame, text=message, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF").pack(pady=5, anchor="w")
    elif text == "Button 6":
        message = get_button6_data()["message"]
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


# # Create a frame to hold the content that will change
content_frame = Frame(window, bg="#FFFFFF")
content_frame.place(x=0, y=140, width=1000, height=660)

# Add default text to the content_frame
default_text = "Welcome! Please click a button to display content."
Label(content_frame, text=default_text, font=("SairaSemiCondensed SemiBold", 24), bg="#FFFFFF").pack(pady=20)

window.resizable(False, False)
window.mainloop()
