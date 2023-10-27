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

# get test postal code
def get_postal_code(mode):
    # mode 1: randomly generating
    if mode == 0:
        loop = 0
        while True:
            random_postal_code = generate_random_postal_code()
            loop = loop + 1
            address = get_address(random_postal_code)
            if address:
                print(f"iteration times: {loop}")
                break
    elif mode == 1:
        costco = "V9B 6A2"
        downtown = "V8W 1H2"
        UVic = "V8P 5C2"
        sidney = "V8L 1X5"
        Durham_Region  = "L9L 1K2"
        UBC = "V6T 1Z4"
        Halifax = "B3K 6R8"
        random_postal_code = Halifax

    print(f"Postal code: {random_postal_code}")
    return random_postal_code

# create test file and store in test file folder
def create_test_file(postal_code,address,test_file_folder):
    # create a file for test
    file_name = postal_code + ".txt"
    # content is the address
    file_content = address
    # file path
    source_file_path = os.path.join(test_file_folder, file_name)
    # Open the file with write ('w') permission. If the file doesn't exist, Python will create it.
    with open(source_file_path, 'w') as file:
        # Write the content to the file
        file.write(file_content)

    return source_file_path,file_name

# find if the directory exist or not and create the folder if not exist
def ensure_path_exist(directory):
    flag = "True"
    # Check if the directory exists, if not create it
    if not os.path.exists(directory):
        flag = "False"
        os.mkdir(directory)
        print(f'Directory {directory} created.')
    else:
        print(f'Directory {directory} already exists.')
    # return the father path of the file, flag of path existance(T:exist, F:not)
    return directory, flag

# Get the directory according to the location
def get_path(address):
    # turn address str into str list
    add_lst = address.split(", ")
    # in country, province, postal code, city, town order
    add_lst.reverse()
    # just use province, city and town
    # remove postal code inside
    for names in add_lst:
        contains_number = any(char.isdigit() for char in names)
        if contains_number:
            add_lst.remove(names)
    # just need 3 levels
    add_level = add_lst[1:4]
    # replace space by _
    add_level = [x.replace(" ", "_") for x in add_level]
    # check whether "Backend test" folder exist or not
    # Get the current working directory
    current_directory = os.getcwd()
    # Now to get the father (parent) directory:
    father_directory = os.path.dirname(current_directory)
    test_repository = os.path.join(father_directory, "Backend test")
    # find it "test_repository" exist or not
    test_repository,test_repository_flag = ensure_path_exist(test_repository)
    # create a folder to store all the generated files
    test_file_folder = os.path.join(test_repository, "test file")
    # find it "test_file_folder" exist or not
    test_file_folder,test_file_folder_flag = ensure_path_exist(test_file_folder)
    flag = "True"
    add_path = test_repository
    for add_directory in add_level:
        # Construct the path to the next directory
        add_path = os.path.join(add_path, add_directory)
        # Check if the directory exists, if not create it
        add_path,add_flag = ensure_path_exist(add_path)

    return add_path,add_flag,test_repository_flag,test_file_folder

# copy the file to the given file path
def copy_file(source_file_path, file_father_path,file_name):
    # Specify the destination path
    destination_path = os.path.join(file_father_path,file_name)
    try:
        # Attempt to copy the file
        dest = shutil.copy2(source_file_path, destination_path)
        return f'Copy successful: {dest}'
    except FileNotFoundError as e:
        return f'File not found: {e}'
    except PermissionError as e:
        return f'Permission error: {e}'
    except Exception as e:
        # Catch any other exceptions
        return f'An error occurred: {e}'



if __name__ == "__main__":
    # get test postal code
    postal_code = get_postal_code(1)
    # get address according to the postal code
    address = get_address(postal_code)
    # get file path according to the address
    file_path, add_flag, test_repository_flag, test_file_folder = get_path(address)
    # create test file
    source_file_path, file_name = create_test_file(postal_code, address, test_file_folder)
    # move test file
    result = copy_file(source_file_path, file_path, file_name)
    print(result)
