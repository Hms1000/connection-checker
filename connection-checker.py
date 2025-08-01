from pathlib import Path
import subprocess
import argparse
import logging
import json

# i decided to setup logging so that i can not miss important infomation
log_file = Path(__file__).with_name('connection-checker.log')
logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s-%(levelname)s-%(message)s'
)

# this is the function i am using to check the connection
def check_connection(packet, target):
    try:
        # i ran a ping request, i only decided to capture a few packets because i was just testing connection
        subprocess.run(['ping', '-c', str(packet), target], stdout=subprocess.DEVNULL, check=True)
        print('Internet is up.')
        logging.info('Internet is up')
        result = {'status': 'connected', 'target': target}
        return result
        # i used error handling methods to capture any errors
    except subprocess.CalledProcessError:
        print('No internet connection')
        logging.error('No internet connection')
        result = {'status': 'disconnected', 'target': target}
        return result

# i am trying to save the output as json data
def save_json_output(filename, result):
    try:
        with open(filename, 'w') as f:
            json.dump(result, f, indent=4, sort_keys=True)
            logging.info(f'Output saved to {filename}')
    except FileNotFoundError:
        print(f'File Not Found')
        logging.error(f'File Not Found')

# i put everything together using a main function 
def main():
    parser = argparse.ArgumentParser(description='internet connectivity checker')
    parser.add_argument('--target', type=str, default='8.8.8.8', help='target ip address or url')
    parser.add_argument('--packet', type=int, default=4, help='number of ping packets')
    parser.add_argument('--output', default='status.json', help='Output JSON filename')
    args = parser.parse_args()

    result = check_connection(args.packet, args.target)

    save_json_output(args.output, result)

if __name__ == '__main__':
    main()
