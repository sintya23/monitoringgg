import requests
import smtplib
from email.message import EmailMessage
import json

# Membaca daftar URL dari conf.json
with open('conf.json', 'r') as file:
    config_data = json.load(file)
    daftar_url = config_data.get('daftar_url', [])

# Melakukan looping untuk mengakses URL
for url in daftar_url:
    try:
        response = requests.get(url)
        # Periksa kode status HTTP untuk menentukan apakah permintaan berhasil
        if response.status_code == 200:
            print(f"Berhasil mengakses URL: {url}")
        else:
            print(f"Gagal mengakses URL: {url}, Kode Status: {response.status_code}")
    except Exception as e:
        print(f"Gagal mengakses URL: {url}, Error: {str(e)}")

# Lakukan permintaan HTTP untuk memeriksa status kode
response = requests.get(url)

if response.status_code < 200 and response.status_code > 299:
    pesan = f"Situs web {url} tidak dapat diakses. Status code: {response.status_code}"
    
    # Mengirim notifikasi email menggunakan SMTP
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)  # Server SMTP dan port
        server.starttls()  # Mengenkripsi koneksi
        server.login("email_address, email_password")  # Login ke email pengirim
        msg = f"Subject: Notifikasi Situs Web Tidak Dapat Diakses\n\n{pesan}"
        server.sendmail("email_address, recipient_address", msg)  # Mengirim pesan email
        server.quit()  # Keluar dari server
        print("Notifikasi email telah dikirim.")
    except Exception as e:
        print(f"Gagal mengirim email: {e}")
    else:
        print(f"Berhasil mengakses URL: {url}")