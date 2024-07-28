import os
import requests
import shutil
import random
import string
import platform
import psutil
from datetime import datetime
from PIL import Image
import subprocess

API_KEY = 'add your weather API then it will work'  

def backup_files(source_dir, backup_dir):
    try:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = os.path.join(backup_dir, f"backup_{timestamp}")
        shutil.copytree(source_dir, backup_path)
        print(f"\nBackup created at {backup_path}\n")
    except Exception as e:
        print(f"\nError during backup: {e}\n")

def scrape_weather(city):
    try:
        url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
        response = requests.get(url)
        data = response.json()
        if "error" in data:
            print(f"\nError: {data['error']['message']}\n")
        else:
            temperature = data["current"]["temp_c"]
            weather_description = data["current"]["condition"]["text"]
            humidity = data["current"]["humidity"]
            wind_speed = data["current"]["wind_kph"]
            feels_like = data["current"]["feelslike_c"]
            print(f"\nCurrent temperature in {city}: {temperature}°C\n")
            print(f"Weather description: {weather_description}\n")
            print(f"Humidity: {humidity}%\n")
            print(f"Wind speed: {wind_speed} kph\n")
            print(f"Feels like: {feels_like}°C\n")
    except Exception as e:
        print(f"\nError fetching weather data: {e}\n")

def resize_images():
    try:
        directory = input("Enter image directory: ")
        image_name = input("Enter image name (leave blank to resize all images in the directory): ")
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))
        size = (width, height)
        
        if image_name:
            # Resize a specific image
            img_path = os.path.join(directory, image_name)
            if os.path.isfile(img_path):
                img = Image.open(img_path)
                img = img.resize(size,  Image.Resampling.LANCZOS)
                img.save(os.path.join(directory, f"resized_{image_name}"))
                print(f"Resized {image_name}")
            else:
                print(f"Image {image_name} not found in {directory}")
        else:
            # Resize all images in the directory
            print(f"\nResizing all images in {directory} to {size[0]}x{size[1]}:\n")
            for filename in os.listdir(directory):
                if filename.endswith(".jpg") or filename.endswith(".png"):
                    img = Image.open(os.path.join(directory, filename))
                    img = img.resize(size, Image.LANCZOS)
                    img.save(os.path.join(directory, f"resized_{filename}"))
                    print(f"Resized {filename}")
            print("\nImage resizing completed.\n")
    except Exception as e:
        print(f"\nError: {e}\n")

def generate_password(length=12):
    try:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        print(f"\nGenerated password: {password}\n")
    except Exception as e:
        print(f"\nError generating password: {e}\n")

def delete_files(directory, file_name, file_extension):
    try:
        print(f"\nDeleting files in {directory} with name containing '{file_name}' and extension '{file_extension}':\n")
        for filename in os.listdir(directory):
            if filename.endswith(file_extension) and file_name in filename:
                os.remove(os.path.join(directory, filename))
                print(f"Deleted {filename}")
        print("\nFile deletion completed.\n")
    except Exception as e:
        print(f"\nError deleting files: {e}\n")

def count_files(directory):
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        print(f"\nNumber of files in {directory}: {len(files)}\n")
    except FileNotFoundError:
        print(f"\nError: The directory {directory} does not exist.\n")
    except Exception as e:
        print(f"\nError counting files: {e}\n")

def list_files(directory):
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        print(f"\nFiles in {directory}:\n")
        for file in files:
            print(file)
        print()
    except FileNotFoundError:
        print(f"\nError: The directory {directory} does not exist.\n")
    except Exception as e:
        print(f"\nError listing files: {e}\n")

def check_disk_usage(directory):
    try:
        total, used, free = shutil.disk_usage(directory)
        print(f"\nDisk usage for {directory}:\n")
        print(f"Total: {total // (2**30)} GiB\n")
        print(f"Used: {used // (2**30)} GiB\n")
        print(f"Free: {free // (2**30)} GiB\n")
    except Exception as e:
        print(f"\nError checking disk usage: {e}\n")

def disk_cleaner():
    try:
        temp_dirs = [
            os.path.join(os.getenv('TEMP', '/tmp')),
            '/var/tmp',
            '/tmp'
        ]
        for temp_dir in temp_dirs:
            try:
                for root, dirs, files in os.walk(temp_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        os.remove(file_path)
                        print(f"Deleted {file_path}")
            except Exception as e:
                print(f"Error cleaning {temp_dir}: {e}")
        print("\nDisk cleaning completed.\n")
    except Exception as e:
        print(f"\nError during disk cleaning: {e}\n")

def system_maintenance():
    try:
        system = platform.system()
        if system == 'Windows':
            print("\nPerforming Windows system maintenance...\n")
            subprocess.run(["cleanmgr", "/sagerun:1"], check=True)
            print("\nWindows maintenance completed.\n")
        elif system == 'Linux':
            print("\nPerforming Linux system maintenance...\n")
            subprocess.run(["sudo", "apt-get", "autoremove", "-y"], check=True)
            subprocess.run(["sudo", "apt-get", "clean"], check=True)
            print("\nLinux maintenance completed.\n")
        elif system == 'Darwin':
            print("\nPerforming macOS system maintenance...\n")
            subprocess.run(["brew", "cleanup"], check=True)
            print("\nmacOS maintenance completed.\n")
        else:
            print("\nUnsupported OS for system maintenance.\n")
    except Exception as e:
        print(f"\nError during system maintenance: {e}\n")

def system_report():
    try:
        print("\nSystem Report:\n")
        print(f"Operating System: {platform.system()} {platform.version()}\n")
        print(f"Processor: {platform.processor()}\n")
        print(f"CPU Cores: {psutil.cpu_count(logical=True)}\n")
        print(f"CPU Frequency: {psutil.cpu_freq().current} MHz\n")
        print(f"Memory: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB Total\n")
        print(f"Memory Usage: {psutil.virtual_memory().percent}%\n")
        print(f"Disk Usage: {psutil.disk_usage('/').percent}%\n")
    except Exception as e:
        print(f"\nError generating system report: {e}\n")

def menu():
    print("\nPlease choose a task to perform:\n")
    print("Enter 1. Backup Files")
    print("Enter 2. Scrape Weather Information")
    print("Enter 3. Resize Images")
    print("Enter 4. Generate a Random Password")
    print("Enter 5. Delete Files")
    print("Enter 6. Count Files in Directory")
    print("Enter 7. List Files in Directory")
    print("Enter 8. Check Disk Usage")
    print("Enter 9. Disk Cleaner")
    print("Enter 10. System Maintenance")
    print("Enter 11. System Report")
    print("Enter 0. Exit\n")

while True:
    menu()
    choice = input("Enter your choice: ")
    
    if choice == '1':
        source_dir = input("\nEnter source directory: ")
        backup_dir = input("Enter backup directory: ")
        if os.path.exists(source_dir) and os.path.exists(backup_dir):
            backup_files(source_dir, backup_dir)
        else:
            print("\nInvalid directory path, please try again.\n")
    elif choice == '2':
        city = input("\nEnter city name: ")
        scrape_weather(city)
    elif choice == '3':
        resize_images()
    elif choice == '4':
        try:
            length = int(input("\nEnter password length: "))
            generate_password(length)
        except ValueError:
            print("\nInvalid input, please enter a numeric value for password length.\n")
    elif choice == '5':
        directory = input("\nEnter directory: ")
        file_name = input("Enter part of the file name to delete: ")
        file_extension = input("Enter file extension to delete (e.g., .mp3, .mp4, .txt, .pdf, .docx): ")
        if os.path.exists(directory):
            delete_files(directory, file_name, file_extension)
        else:
            print("\nInvalid directory path, please try again.\n")
    elif choice == '6':
        directory = input("\nEnter directory: ")
        if os.path.exists(directory):
            count_files(directory)
        else:
            print("\nInvalid directory path, please try again.\n")
    elif choice == '7':
        directory = input("\nEnter directory: ")
        if os.path.exists(directory):
            list_files(directory)
        else:
            print("\nInvalid directory path, please try again.\n")
    elif choice == '8':
        directory = input("\nEnter directory: ")
        if os.path.exists(directory):
            check_disk_usage(directory)
        else:
            print("\nInvalid directory path, please try again.\n")
    elif choice == '9':
        disk_cleaner()
    elif choice == '10':
        system_maintenance()
    elif choice == '11':
        system_report()
    elif choice == '0':
        print("\nExiting the program.\n")
        break
    else:
        print("\nInvalid choice, please try again.\n")
