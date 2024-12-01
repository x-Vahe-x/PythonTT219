import os
import random
import string
import time
import threading
import multiprocessing
from collections import Counter

current_directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(current_directory, 'large_text.txt')

def create_large_text_file(filename, num_words=1000000):
    with open(filename, 'w') as f:
        for _ in range(num_words):
            sentence = ' '.join(random.choices(string.ascii_lowercase + ' ', k=random.randint(5, 15)))
            f.write(sentence + '\n')

def count_words_sequential(filename):
    word_counter = Counter()
    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            word_counter.update(words)
    return word_counter

def count_words_chunk(chunk):
    word_counter = Counter()
    for line in chunk:
        words = line.split()
        word_counter.update(words)
    return word_counter

def count_words_multithreaded(filename, num_threads=4):
    with open(filename, 'r') as f:
        lines = f.readlines()
        
    chunk_size = len(lines) // num_threads
    threads = []
    results = []

    def worker(chunk_start, chunk_end):
        chunk = lines[chunk_start:chunk_end]
        result = count_words_chunk(chunk)
        results.append(result)

    for i in range(num_threads):
        chunk_start = i * chunk_size
        chunk_end = (i + 1) * chunk_size if i < num_threads - 1 else len(lines)
        thread = threading.Thread(target=worker, args=(chunk_start, chunk_end))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    final_counter = Counter()
    for result in results:
        final_counter.update(result)

    return final_counter

def count_words_multiprocessing(filename, num_processes=4):
    with open(filename, 'r') as f:
        lines = f.readlines()

    chunk_size = len(lines) // num_processes
    chunks = [lines[i * chunk_size:(i + 1) * chunk_size] for i in range(num_processes)]

    with multiprocessing.Pool(num_processes) as pool:
        results = pool.map(count_words_chunk, chunks)

    final_counter = Counter()
    for result in results:
        final_counter.update(result)

    return final_counter

if __name__ == "__main__":
    create_large_text_file(filename, num_words=1000000)
    print(f"Large text file '{filename}' created.")

    start_time = time.time()
    sequential_result = count_words_sequential(filename)
    sequential_time = time.time() - start_time
    print(f"Sequential execution time: {sequential_time:.2f} seconds")

    start_time = time.time()
    multithreaded_result = count_words_multithreaded(filename, num_threads=4)
    multithreaded_time = time.time() - start_time
    print(f"Multithreaded execution time: {multithreaded_time:.2f} seconds")

    start_time = time.time()
    multiprocessing_result = count_words_multiprocessing(filename, num_processes=4)
    multiprocessing_time = time.time() - start_time
    print(f"Multiprocessing execution time: {multiprocessing_time:.2f} seconds")

    print("\nExecution Time Comparison:")
    print(f"Sequential Time: {sequential_time:.2f} seconds")
    print(f"Multithreaded Time: {multithreaded_time:.2f} seconds (Speedup: {sequential_time/multithreaded_time:.2f}x)")
    print(f"Multiprocessing Time: {multiprocessing_time:.2f} seconds (Speedup: {sequential_time/multiprocessing_time:.2f}x)")
