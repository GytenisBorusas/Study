import re
from datetime import datetime

month_names = {
    "january": ["january", "1"],
    "february": ["february", "2"],
    "march": ["march", "3"],
    "april": ["april", "4"],
    "may": ["may", "5"],
    "june": ["june", "6"],
    "july": ["july", "7"],
    "august": ["august", "8"],
    "september": ["september", "9"],
    "october": ["october", "10"],
    "november": ["november", "11"],
    "december": ["december", "12"]
}

def get_month_number(month_name):
    for key, values in month_names.items():
        if month_name.lower() in values:
            return values[1]
    return None

def identify_format(prompt):
    date_str = input(prompt).strip()  # strip spaces
    
    # Check for the "9/8/1636" format
    if re.match(r"^\d{1,2}/\d{1,2}/\d{4}$", date_str):
        month, day, year = date_str.split('/')
        if int(month) >= 13 or int(day) >= 32:
            return "Invalid date"
        return day, month, year
    
    # Check for the "September 8, 1636" format
    try:
        datetime.strptime(date_str, '%B %d, %Y')
        date_part, year = date_str.split(', ')
        month_name, day = date_part.split(' ')
        month = get_month_number(month_name)
        if not month:
            raise ValueError
        return day, month, year
    
    except ValueError:
        return "Unknown format"

def main():
    while True:
        result = identify_format("Date: ")
        
        if isinstance(result, str) and result in ["Invalid date", "Unknown format"]:
            print("Invalid input. Please try again.")
            continue
        
        day, month, year = result
        print(f"{year}-{month.zfill(2)}-{day.zfill(2)}")
        break

main()
