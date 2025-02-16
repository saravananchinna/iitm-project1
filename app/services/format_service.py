from datetime import datetime
import subprocess

format_md_file_path = './data/format.md'
wednesday_count_file_input_path= './data/dates.txt'
wednesday_count_file_output_path='./data/dates-wednesdays.txt'




def read_file(file_name):
    with open(file_name, 'r') as file:
    # Read the content of the file
        content = file.read()
    return content

async def format_data():

    # Define the file path
    file_path = format_md_file_path

    # Run prettier with the --write flag to format the file in-place
    subprocess.run(['npm', 'install', 'prettier@3.4.2'], check=True)  # Install Prettier version 3.4.2
    subprocess.run(['npx', 'prettier', '--write', file_path], check=True)  # Format the file

    # Return the file path for further use
    print(file_path)

async def find_no_of_wednesday():
    date_strings=[]

    with open(wednesday_count_file_input_path, 'r') as file:
        lines = file.readlines()
    file.close
    lines = [line.strip() for line in lines]
    
    for line in lines:
        date_strings.append(line)
    

    # Initialize a counter for Wednesdays
    wednesday_count = 0

    # Iterate over each date string and check if it's a Wednesday
    for date_str in date_strings:
        try:
            # Try different date formats
           
            if '-' in date_str:
                date_obj = datetime.strptime(date_str, '%d-%b-%Y')
            elif ',' in date_str:
                date_obj = datetime.strptime(date_str, '%b %d, %Y')
            elif '/' in date_str:
                date_obj = datetime.strptime(date_str, '%Y/%m/%d %H:%M:%S')
            else:
                date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                
            # Check if the day of the week is Wednesday (2 is Wednesday in Python's datetime module)
            if date_obj.weekday() == 2:
                wednesday_count += 1
            
            
        except ValueError:
            continue  # Skip any date that cannot be parsed
    
    with open(wednesday_count_file_output_path,'w') as wfile:
        wfile.write(str(wednesday_count))
        wfile.close()

    return wednesday_count