import os
import random
import time

current_directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(current_directory, 'random_numbers.txt')

def create_file(filename):
    with open(filename, 'w') as file:
        for _ in range(100):
            line = ' '.join(str(random.randint(1, 100)) for _ in range(20))
            file.write(line + '\n')

def read_file_and_convert_to_int(filename):
    with open(filename, 'r') as file:
        return [list(map(int, line.split())) for line in file]

def filter_numbers(data):
    return [[num for num in line if num > 40] for line in data]

def write_filtered_data_to_file(filename, filtered_data):
    with open(filename, 'w') as file:
        for line in filtered_data:
            file.write(' '.join(map(str, line)) + '\n')

def read_file_generator(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield list(map(int, line.split()))

def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.2f} seconds")
        return result
    return wrapper

if __name__ == "__main__":

    create_file(filename)
    data = read_file_and_convert_to_int(filename)
    filtered_data = filter_numbers(data)
    write_filtered_data_to_file(filename, filtered_data)

    print("Reading the file using generator:")
    for i, line in enumerate(read_file_generator(filename)):
        if i < 5:  
            print(line)

    @execution_time_decorator
    def process_file(filename):
        data = read_file_and_convert_to_int(filename)
        filtered_data = filter_numbers(data)
        write_filtered_data_to_file(filename, filtered_data)

    process_file(filename)