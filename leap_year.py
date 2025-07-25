def is_leap_year(year):
    """
    Determines if a given year is a leap year.
    
    Rules:
    - A year is a leap year if it is divisible by 4
    - Except years divisible by 100, unless they are also divisible by 400
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def main():
    try:
        year = int(input("Enter a year to check if it's a leap year: "))
        if year < 0:
            print("Please enter a valid positive year.")
        elif is_leap_year(year):
            print(f"✅ {year} is a leap year.")
        else:
            print(f"❌ {year} is not a leap year.")
    except ValueError:
        print("⚠️ Invalid input. Please enter a valid numeric year.")

if __name__ == "__main__":
    main()
