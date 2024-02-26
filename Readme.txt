OpenCv ile pc veya harici kameradan belirli bir sürede aldığımız görüntüler arasında fark kontrolü yaparak izlediğimiz yerde hareket var veya hareket yok durumlarını belirliyoruz.
Belirlenen durumu sistemler arasında iletişim kurmak için FireBase' e veri olarak gönderiyoruz.
FireBase .json dosyasını cred = credentials.Certificate("xxx.json") dosyasına ekleyiniz.
FireBase admin için: 
firebase_admin.initialize_app(cred, {
   "databaseURL": "https://sistem-xxxx-default-rtdb.firebaseio.com/"})  yolunu ekleyiniz.
videom= cv2.VideoVapture() = default 0 verisi gelir. Harici almak için 1 veya 2 giriniz.
Süre belirlemek için:
sure=input("time") saniye olarak giriniz.