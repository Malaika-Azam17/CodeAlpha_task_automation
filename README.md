Project Title: Python Task Automation Script

Description

This Python script is designed to automate various system tasks, including file backup, weather data scraping, image resizing, password generation, file deletion, file counting, listing files in a directory, checking disk usage, disk cleaning, performing system maintenance, and generating a system report. The script provides a menu-driven interface for easy task selection and execution.

Features

Backup Files: Creates a backup of a specified directory.

Scrape Weather Information: Retrieves and displays current weather information for a specified city.

Resize Images: Resizes a specific image or all images in a directory to specified dimensions.

Generate a Random Password: Generates a random password of specified length.

Delete Files: Deletes files in a directory that match a specified name pattern and file extension.

Count Files in Directory: Counts the number of files in a specified directory.

List Files in Directory: Lists all files in a specified directory.

Check Disk Usage: Displays the total, used, and free disk space for a specified directory.

Disk Cleaner: Cleans temporary files from system directories.

System Maintenance: Performs system maintenance tasks based on the operating system.

System Report: Generates a report of system information including OS details, CPU, memory, and disk usage.

Detailed Function Descriptions

backup_files(source_dir, backup_dir)
Creates a backup of the specified source directory into the specified backup directory, with a timestamp to distinguish multiple backups.

scrape_weather(city)
Fetches current weather information for the specified city using the WeatherAPI and displays temperature, weather description, humidity, wind speed, and feels-like temperature.

resize_images()
Prompts the user to enter an image directory, image name (optional), width, and height. Resizes the specified image or all images in the directory to the given dimensions.

generate_password(length=12)
Generates a random password of the specified length using a combination of letters, digits, and punctuation characters.

delete_files(directory, file_name, file_extension)
Deletes files in the specified directory that match the provided name pattern and file extension.

count_files(directory)
Counts and displays the number of files in the specified directory.

list_files(directory)
Lists and displays all files in the specified directory.

check_disk_usage(directory)
Displays the total, used, and free disk space for the specified directory.

disk_cleaner()
Cleans temporary files from common system temporary directories.

system_maintenance()
Performs system maintenance tasks based on the operating system:

Windows: Runs Disk Cleanup.
Linux: Runs apt-get autoremove and apt-get clean.
macOS: Runs brew cleanup.
system_report()
Generates and displays a report of system information including OS details, CPU, memory, and disk usage.

menu()
Displays the main menu with options for each task and handles user input to execute the corresponding function.
