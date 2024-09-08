import hashlib
import os
import logging
import argparse


file_path = "./hash_db/hashes.txt"
directory_path = "./hash_db/"


def read_hash_db(file_path):
    hash_list = []
    with open(file_path, 'r') as file:
        for line in file:
            hash_list.append(line.strip())
    return hash_list



def calculate_file_hash(file_path):
    with open(file_path, 'rb') as f:
        sha256_hash = hashlib.sha256()

        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)

    return sha256_hash.hexdigest()



def scan_directory(directory_path, hash_list):
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            file_hash = calculate_file_hash(file_path)

            print(f"\nDosya: {file_path}, Hesaplanan Hash: {file_hash}")

            if file_hash in hash_list:
                print(f"\nZararlı yazılım tespit edildi: {file_path}")
                log_results(file_path, True)
            else:
                print(f"\nTemiz dosya: {file_path}")
                log_results(file_path, False)



logging.basicConfig(filename='scan_results.log', level=logging.INFO)

def log_results(file_path, is_malware):
    if is_malware:
        logging.info(f"\nZararlı yazılım bulundu: {file_path}")
    else:
        logging.info(f"\nTemiz dosya: {file_path}")



def main():
    parser = argparse.ArgumentParser(description="BeyzInfectify")
    parser.add_argument('--directory', type=str, help="Taranacak dizin", required=True)
    
    args = parser.parse_args()
    
    hash_list = read_hash_db(file_path)
    
    scan_directory(args.directory, hash_list)



if __name__ == '__main__':
    main()

