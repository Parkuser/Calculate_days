from datetime import date

print("Calculate how many days have passed from an earlier date to today\nor how many days it is to a date in the future")
input_date = input("Input date e.g. 2022-03-13 ")
input_date_split = input_date.split("-")

now = date.today()
try:
    new_date = date(int(input_date_split[0]), int(input_date_split[1]), int(input_date_split[2]))
    delta = new_date - now
    if delta.days < 0:
        print(f"{input_date} was for {abs(delta.days)} days ago")
    else:
        print(f'It is {delta.days} days to {input_date} ')
except ValueError:
    print("Wrong date format, month must be in 1..12 or day is out of range for month")
except IndexError:
    print("Date should be in format 2022-02-18")
