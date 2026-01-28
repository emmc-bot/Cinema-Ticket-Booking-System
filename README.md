# 🎬 Cinema Ticket Booking System

A simple command-line movie ticket booking system built with Python.

## 📋 Features
- View available movies with showtimes and studio details
- Interactive seat selection with visual layout
- Automatic seat availability tracking
- Receipt generation with pricing
- Data persistence through text files

## 📁 Project Structure
```
project/
├── main.py              # Main program file
├── movies.txt           # Movie database (code|title|status)
├── studios.txt          # Studio database (code|name|rows|cols|status)
└── README.md            # This file
```

## 🚀 How to Run
1. Ensure Python 3.x is installed on your system
2. Place all files in the same directory
3. Update file paths in `readFile()` function if needed
4. Run the program:
```bash
python main.py
```

## 📝 Data Files Format

### movies.txt
```
TLT|The Last Travel|A
TMR|The Midnight Run|A
TGM|The Great Mission|A
LSP|Lost Planet|A
```

### studios.txt
```
S1|Studio 1|10|15|A
S2|Studio 2|12|18|A
S3|Studio 3|8|12|A
MX|IMAX|15|20|A
```

## 🎯 Usage Guide

### 1. View Available Movies
- The program starts by displaying all active movies
- Shows movie title, code, showtimes, and studio details

### 2. Select a Movie
- Enter the movie code (e.g., `TLT`)
- Only active movies (status `A`) can be selected

### 3. Choose Showtime
- View available time slots for the selected movie
- Enter your preferred time (e.g., `13.30`)

### 4. Select Seats
- A visual seating layout will appear showing available `[ ]` and taken `[x]` seats
- Enter seat using letter+number format (e.g., `A1`, `B12`)
- You can book multiple seats in one transaction

### 5. Complete Booking
- Review your receipt with movie details, seats, and total price
- The program automatically updates seat availability

## 💰 Pricing
- Each ticket costs **Rp. 50,000**
- Total price = number of tickets × Rp. 50,000

## ⚠️ Notes
- Only movies with status `A` (Active) are available
- Seats are shown as:
  - `[ ]` = Available
  - `[x]` = Taken
- Seat format: Letter (row) + Number (column), e.g., `A1`, `C12`
- Maximum seat columns are 2 digits (up to 99 seats per row)

## 🔧 Customization
- Modify `movies.txt` and `studios.txt` to add/remove movies and studios
- Change ticket price in the `createReciept()` function (line 98)
- Update showtime schedules in the `playD` dictionary

## 📊 Sample Output
```
THE LAST TRAVEL : TLT
13.30 Studio 1 ( 10 x 15 )
15.00 Studio 4 ( 12 x 18 )

Enter movie code: TLT
Movie Title: The Last Travel
['13.30', '15.00', '19.30']
Choose playing time: 13.30
...
```

## 🛠️ Requirements
- Python 3.x
- No external libraries required

---
