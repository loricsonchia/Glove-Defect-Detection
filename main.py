import os
import tkinter as tk
from customtkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

#image upload Handler
def open_image():
    global photo
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg; *.jpeg; *.png; *.bmp; *.heic")])
    if file_path:
        image = Image.open(file_path)
        max_size = (300, 300)
        image.thumbnail(max_size, Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo

app = CTk()
app.geometry("1200x600")
app.title("Glove Defect Detector GDD System")
app.resizable(0,0)

#image frame
frame0 = CTkFrame(master=app, width=350, height=600)
frame0.grid(row=0, column=0)
side_img_data = Image.open("main1.jpeg")
side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(350, 600))
CTkLabel(master=frame0, text="", image=side_img).pack(expand=True, side="left")


# Header frame (adjusted to span entire top row)
frame1 = CTkFrame(master=app, fg_color="#ffffff")
frame1.grid(row=0, column=1, columnspan=2, padx=(1,1), pady=(5,450), sticky="ns")  # Spans columns 1 and 2
CTkLabel(master=frame1, text="Glove Defect Detector", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 50)).pack(anchor="w", pady=(35, 40), padx=(160, 151))


#input frame
frame2 = CTkFrame(master=app, fg_color="#ffffff", border_color="#000000", border_width=2)
frame2.grid(row=0, column=1, padx=(1, 1), pady=(150, 1), sticky="ns")
CTkLabel(master=frame2, text="Input your image", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 20)).pack(anchor="w", pady=(5, 30), padx=(135, 135))

# Label to display the input image
input_image_label = tk.Label(frame2)
input_image_label.pack(pady=(5, 20))  # Adjust the padding as needed


# Frame for buttons
buttons_frame = CTkFrame(master=frame2,fg_color="#ffffff")
buttons_frame.pack(side='bottom', pady=(10, 10))  # This frame is packed at the bottom of frame2

# Buttons for "Upload Image" and "Detect"
button_upload = CTkButton(master=buttons_frame, text="Upload Image", command=open_image)
button_upload.pack(side='left', padx=(10, 20), pady=(5, 5))  # These buttons are side by side
button_detect = CTkButton(master=buttons_frame, text="Detect")
button_detect.pack(side='left', padx=(20, 10), pady=(5, 5))

#output frame
frame3 = CTkFrame(master=app, fg_color="#ffffff", border_color="#000000", border_width=2)
frame3.grid(row=0, column=2, padx=(1, 1), pady=(150, 1), sticky="ns")
CTkLabel(master=frame3, text="Output", text_color="#7E7E7E", anchor="w", justify="center", font=("Arial Bold", 20)).pack(anchor="w", pady=(10, 5), padx=(172, 172))

label = tk.Label(app)
label.grid()

app.mainloop()