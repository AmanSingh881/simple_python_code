import time

output_file = 'timestamps.txt'

while True:
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    with open(output_file, 'a') as file:
        file.write(current_time + '\n')
    time.sleep(1)
