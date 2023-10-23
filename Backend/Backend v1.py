import random
import string
from geopy.geocoders import Nominatim
import os
import shutil

# generate random postal code as an input for finding random address
def generate_random_postal_code():
    # Characters allowed in different positions of the postal code
    alphabet = string.ascii_uppercase
    digits = string.digits

    # Generate each part of the postal code
    first_alpha = random.choice(alphabet)
    first_digit = random.choice(digits)
    second_alpha = random.choice(alphabet)

    third_digit = random.choice(digits)
    fourth_alpha = random.choice(alphabet)
    fifth_digit = random.choice(digits)

    # Combine all parts into the standard format
    postal_code = f"{first_alpha}{first_digit}{second_alpha} {third_digit}{fourth_alpha}{fifth_digit}"

    return postal_code

# find the address according to the postal code
def get_address(postal_code):
    geolocator = Nominatim(user_agent="location_based_smart_drive")
    location = geolocator.geocode(postal_code, country_codes="CA")
    if location:
        return location.address
    else:
        return None

# find if the path exist or not



# Get the directory according to the location
def get_path(address):
    # turn address str into str list
    add_lst = address.split(", ")
    # in country, province, postal code, city, town order
    add_lst.reverse()
    # just use province, city and town
    add_level = add_lst[1:2] + add_lst[3:5]
    # replace space by _
    add_level = [x.replace(" ", "_") for x in add_level]
    #


    file_father_path, exist_flag = ensure_directories_exist(add_level, test_repository)


    # Get the current working directory
    current_directory = os.getcwd()
    # Now to get the father (parent) directory:
    father_directory = os.path.dirname(current_directory)
    test_repository = os.path.join(father_directory, "Backend test")



if __name__ == "__main__":
    # Generate and print a random Canadian postal code
    print(generate_random_postal_code())
