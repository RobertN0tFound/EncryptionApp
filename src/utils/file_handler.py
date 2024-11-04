import os

def read_file(filepath):
    with open(filepath, 'r') as f:
        return f.read()

def write_file(filepath, data):
    with open(filepath, 'w') as f:
        f.write(data)