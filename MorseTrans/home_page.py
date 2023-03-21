import customtkinter
from customtkinter import *
import tkinter.font as font
import os
import speech_recognition as sr
import pyttsx3
from PIL import Image
import ctypes
import encryption as cipher




ctypes.windll.shcore.SetProcessDpiAwareness(1)
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Morse Code Translator App")
        width_of_window = 650
        height_of_window = 490
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_coordinate = (screen_width/2)-(width_of_window/2)
        y_coordinate = (screen_height/2)-(height_of_window/2)
        self.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
        self.resizable(0, 0)

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "morse_dr.png")),
            dark_image=Image.open(os.path.join(image_path, "morse_li.png")),size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "morse_li.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
            dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "morse_dr.png")),
            dark_image=Image.open(os.path.join(image_path, "morse_li.png")), size=(20, 20))
        self.valider_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "valider_dr.png")),
            dark_image=Image.open(os.path.join(image_path, "valider_li.png")), size=(10, 10))


        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Morse Code Trans", image=self.logo_image,
            compound="left", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
            image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Real Time",
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
            image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Morse Code",
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
            image=self.chat_image,anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")


        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark"], command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        #message for finger morse
        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="• Write here your message you want to encrypt",
        compound="left",font=customtkinter.CTkFont(size=16, weight="bold"))
        self.home_frame_large_image_label.grid(row=1, column=0, padx=0, pady=5)

        #entry field & Display code finger
        self.entry_finger_morse = customtkinter.CTkEntry(self.home_frame,placeholder_text="enter your message here",width=380,height=170,border_width=2,corner_radius=10)
        self.entry_finger_morse.place(relx=0.1, rely=0.42)
        
        #Button get fingers code
        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame,corner_radius=1, height=9, border_width=1,border_spacing=7, text="Get Code", image=self.valider_image,
                   font=("Calibri (Body)", 16), fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),anchor="w", command=self.get_code_finger)
        self.home_frame_button_1.grid(row=2, column=0, padx=20, pady=180)

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        #button to launch real time capture
        self.home_frame_button_1 = customtkinter.CTkButton(self.second_frame,corner_radius=2, height=30, border_width=2,border_spacing=20, text="Launch Real Time Capture", image=self.valider_image,
                  font=("Arial", 17),  fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),anchor="w", command=self.get_launch_real_time)
        self.home_frame_button_1.grid(row=0, column=0, padx=110, pady=180)


        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        # message for finger morse 1 
        self.home_frame_large_image_label1 = customtkinter.CTkLabel(self.third_frame, text="• 1 Code Fingers",
        compound="left",font=customtkinter.CTkFont(size=13))
        self.home_frame_large_image_label1.grid(row=1, column=0, padx=50, pady=20)

        #entry field & Display code finger 1 
        self.entry_finger_morse1 = customtkinter.CTkEntry(self.third_frame,placeholder_text="☺☺☺☺☺☺",width=270,height=90,border_width=1.5,corner_radius=10)
        self.entry_finger_morse1.place(relx=0.2, rely=0.12)

        # message for finger morse code 2
        self.home_frame_large_image_label2 = customtkinter.CTkLabel(self.third_frame, text="• 2 Morse Code",
        compound="left",font=customtkinter.CTkFont(size=13))
        self.home_frame_large_image_label2.grid(row=2, column=0, padx=100, pady=100)

        # #entry field & Display morse code 2
        self.entry_finger_morse2 = customtkinter.CTkEntry(self.third_frame,placeholder_text="☺☺☺☺☺☺",width=270,height=90,border_width=1.5,corner_radius=10)
        self.entry_finger_morse2.place(relx=0.2, rely=0.42)

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "Real Time" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "Real Time":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("Real Time")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")


    #----------- get_code_finger method -----------------#
    def get_code_finger(self):
        print("get_code_finger")
        message = str(self.entry_finger_morse.get())
        if message != "" and not message.isdigit():
            from get_code_number_fingers import get_code_fingerN as myGet
            chiffred = myGet(message)
            # print(chiffred)
            self.entry_finger_morse.delete(0, END)
            self.entry_finger_morse.insert(0, chiffred)
            self.entry_finger_morse1.insert(0, chiffred)
            text_morse_code = cipher.encryptor(message.upper())
            self.entry_finger_morse2.insert(0, text_morse_code)

        else:
            self.entry_finger_morse.delete(0, END)
            print("Write Something !!")


    #----------- get_launch_real_time method -----------------#
    def get_launch_real_time(self):
        self.destroy()
        import FingerCounter
        # os.system("python 5-Traitement_Code\FingerCounter.py")


    #----------- get_message_heard method -----------------#
    def get_message_heard(self):
        from FingerCounter import send_message_sound
        sound_message = send_message_sound()
        if sound_message !="":
            x=sound_message
            engine = pyttsx3.init()
            engine.setProperty("rate", 130) ## 2nd parameter sets speed
            engine.say("Your Message is "+x)
            engine.runAndWait()
            print("get message heard")
        else:
            engine = pyttsx3.init()
            engine.setProperty("rate", 130) ## 2nd parameter sets speed
            engine.say("Nothing to say right now")
            engine.runAndWait()
            print("Nothing to say")

    #----------------get all data third frame---------------#
    def get_all_data(self):
        pass



    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


appp = App()
appp.mainloop()
