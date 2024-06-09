# Library Management System Setup Guide

## Step 1: Download Required Software

1. **Python:**
   - Download and install Python from [Python Downloads](https://www.python.org/downloads/).

2. **PyCharm:**
   - Download and install PyCharm Edu from [PyCharm Downloads](https://www.jetbrains.com/edu-products/download/#section=pycharm-edu).

3. **MySQL:**
   - Download and install MySQL Workbench from [MySQL Workbench Downloads](https://dev.mysql.com/downloads/workbench/).
   - Download and install MySQL Installer from [MySQL Installer Downloads](https://dev.mysql.com/downloads/installer/).

4. **WinRAR:**
   - Download and install WinRAR from [WinRAR Downloads](https://www.win-rar.com/download.html?&L=0).

## Step 2: Setup MySQL Workbench

1. **Create Database:**
   - Open MySQL Workbench.
   - Create a new database with the name `userdata`.

2. **Import Data:**
   - Extract the provided `.rar` file using WinRAR.
   - In MySQL Workbench, go to `Server > Data Import`.
   - Import the following SQL files into the `userdata` database:
     - `userdata_book.sql`
     - `userdata_data.sql`
     - `userdata_kato.sql`
     - `userdata_student.sql`

## Step 3: Setup PyCharm and Run the Application

1. **Open PyCharm:**
   - Open PyCharm Edu.
   - Open the `Library-Management-System` folder.

2. **Install Requirements:**
   - Open the terminal within PyCharm.
   - Run the following command to install the required packages:
     ```sh
     pip install -r requirements.txt
     ```

3. **Run the Application:**
   - Open the `loing_page.py` file.
   - Run the file.

## Enjoy the Library Management System!

This setup guide should help you get the Library Management System up and running smoothly. If you encounter any issues, refer to the documentation or seek support from the relevant communities.
