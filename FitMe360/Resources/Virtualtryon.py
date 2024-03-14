import os
import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from cvzone.PoseModule import PoseDetector
import cvzone

# Function to start camera feed with selected shirt images based on gender selection
def start_camera(gender):
    root.withdraw()
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    detector = PoseDetector()
    shirtFolderPath = r"drive:\path\.." # give path of t-shirts folder
    # Determine which shirt images to overlay based on gender selection
    if gender == "Male":
        selected_shirts = [0, 1]  # Indices of male shirt images
    else:
        selected_shirts = [2, 3]  # Indices of female shirt images
    listShirts = os.listdir(shirtFolderPath)
    fixedRatio = 262/190  # widthOfShirt/widthOfPoints lm11 and lm12
    shirtRatioHeightWidth = 581/440
    imageNumber = 0
    counterRight = 0
    counterLeft = 0
    selectionSpeed = 10

    def stop_camera():
        cap.release()  # Release the camera
        cv2.destroyAllWindows()
        root.deiconify()

    while True:
        success, img = cap.read()
        if not success:
            break
        img = detector.findPose(img)
        lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)
        if lmList:
            lm11 = lmList[11][1:3]
            lm12 = lmList[12][1:3]
            imgShirt = cv2.imread(os.path.join(shirtFolderPath, listShirts[selected_shirts[imageNumber]]), cv2.IMREAD_UNCHANGED)
            widthOfShirt = int((lm11[0]-lm12[0]*fixedRatio))
            currentScale = (lm11[0]-lm12[0])/190
            offset = int(44*currentScale), int(48*currentScale)
            try:
                img = cvzone.overlayPNG(img, imgShirt, (lm12[0] - offset[0], lm12[1] - offset[1]))
            except:
                pass

            if lmList[16][1] < 100:
                counterRight += 1
                cv2.ellipse(img, (139, 360), (66, 66), 0, 0,
                            counterRight * selectionSpeed, (0, 255, 0), 20)
                if counterRight * selectionSpeed > 360:
                    counterRight = 0
                    if imageNumber < len(selected_shirts) - 1:
                        imageNumber += 1
            elif lmList[15][1] > 1000:
                counterLeft += 1
                cv2.ellipse(img, (1138, 360), (66, 66), 0, 0,
                            counterLeft * selectionSpeed, (0, 255, 0), 20)
                if counterLeft * selectionSpeed > 360:
                    counterLeft = 0
                    if imageNumber > 0:
                        imageNumber -= 1
            else:
                counterRight = 0
                counterLeft = 0

        cv2.imshow("FitMe360", img)
        key = cv2.waitKey(1)
        if key == ord('q'):
            stop_camera()  # Stop camera if 'q' is pressed



# Create GUI window
root = tk.Tk()
root.title("FitMe360")
root.geometry("600x400")
root.configure(bg="#000000")

# Function to handle gender selection
def select_gender():
    gender = gender_var.get()
    start_camera(gender)

# Website name banner
label_banner = ttk.Label(root, text="FitMe360", background="#000000", foreground="white", font=("Now", 24, "bold"))
label_banner.pack(side="top", pady=10)  # Align the banner to the top center

# Label and combobox for gender selection
label_gender = ttk.Label(root, text="Select your gender:", background="#000000", foreground="white", font=("Helvetica", 14))
label_gender.pack(pady=(20, 5), padx=10)  # Adjust padding
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(root, textvariable=gender_var, values=["Male", "Female"], font=("Helvetica", 12))
gender_combobox.pack(pady=5, padx=10)  # Adjust padding

# Button to start the application
start_button = ttk.Button(root, text="Start", command=select_gender, style="StartButton.TButton")
start_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Align the button to the center

style = ttk.Style(root)
style.configure("StartButton.TButton", background="black", foreground="black", font=("Helvetica", 12), padding=10)


root.mainloop()
