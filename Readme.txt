Image Processing v2
This Python script captures images from two cameras and detects motion within specific regions of interest (ROIs) in the captured frames. It utilizes the OpenCV library for image processing and Firebase Realtime Database for storing motion detection alerts.

Description
The script captures images from two cameras at regular intervals and compares consecutive frames to detect motion. It defines regions of interest (ROIs) in each frame and computes the difference between consecutive frames within these regions. If motion is detected, it sends alerts to a Firebase Realtime Database.
Firebase Integration
Obtain the Firebase Admin SDK JSON file and save it as "xxx.json".
Initialize the Firebase Admin SDK in the script using the provided credentials and specify the database URL.
cred = credentials.Certificate("xxx.json")
firebase_admin.initialize_app(cred, {
   "databaseURL": "https://sistem-xxxx-default-rtdb.firebaseio.com/"
})
Dependencies
Python 3.x
OpenCV (cv2) library
Firebase Admin SDK
Pyrebase library
Installation
Ensure you have Python 3.x installed on your system.
Install the required libraries:
Copy code
pip install opencv-python
pip install firebase-admin
pip install pyrebase
Obtain the Firebase Admin SDK JSON file and place it in the project directory.
Usage
Run the script:
Copy code
python Image_Processing_v2.py
Enter the interval (in seconds) for capturing images when prompted.
The script will capture images from the connected cameras, detect motion, and send alerts to the Firebase Realtime Database when motion is detected.
Important Notes
Ensure that both cameras are properly connected and accessible by the script.
Adjust the ROIs and motion detection parameters as needed.
Modify the Firebase Realtime Database URL and paths according to your Firebase project setup.
The script continuously runs until the "ESC" key is pressed.
The motion detection alerts are sent to the Firebase Realtime Database.
Additional functionality, such as email notifications, can be integrated as needed.
License
This project is licensed under the MIT License.

Contribution
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.


Açıklama Türkçe: 
OpenCv ile pc veya harici kameradan belirli bir sürede aldığımız görüntüler arasında fark kontrolü yaparak izlediğimiz yerde hareket var veya hareket yok durumlarını belirliyoruz.
Belirlenen durumu sistemler arasında iletişim kurmak için FireBase' e veri olarak gönderiyoruz.
FireBase .json dosyasını cred = credentials.Certificate("xxx.json") dosyasına ekleyiniz.
FireBase admin için: 
firebase_admin.initialize_app(cred, {
   "databaseURL": "https://sistem-xxxx-default-rtdb.firebaseio.com/"})  yolunu ekleyiniz.
videom= cv2.VideoVapture() = default 0 verisi gelir. Harici almak için 1 veya 2 giriniz.
Süre belirlemek için:
sure=input("time") saniye olarak giriniz.