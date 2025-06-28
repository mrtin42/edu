import re
from datetime import datetime

#-- 1 -----------------------
def calculate_average_speed(time1, time2):
    time_format = "%H:%M:%S"
    time1 = datetime.strptime(time1, time_format)
    time2 = datetime.strptime(time2, time_format)
    time_diff = (time2 - time1).total_seconds() / 3600  # convert seconds to hours
    distance = 1  # distance between cameras in miles
    average_speed = distance / time_diff
    return average_speed

def is_valid_number_plate(number_plate):
    pattern = r"^[A-Z]{2}\d{2}\s\d{3}[A-Z]{3}$"
    return bool(re.match(pattern, number_plate))

def process_speed_data(file_path, speed_limit=70):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        number_plate, time1, time2 = line.strip().split(',')
        if not is_valid_number_plate(number_plate):
            print(f"Invalid number plate: {number_plate}")
            continue
        
        average_speed = calculate_average_speed(time1, time2)
        if average_speed > speed_limit:
            print(f"Speeding: {number_plate} at {average_speed:.2f} mph")

if __name__ == "__main__":
    
    # Example usage
    time1 = "08:00:00"
    time2 = "08:01:00"
    print(f"Average speed: {calculate_average_speed(time1, time2):.2f} mph")
    
    number_plate = "XX77 787"
    print(f"Number plate {number_plate} is valid: {is_valid_number_plate(number_plate)}")
    
    # Process speed data from a file
    process_speed_data('/path/to/speed_data.txt')