import csv
import os

# Specify the file path
# file_path = "csv_file.csv"

header = ["timestamp", "traffic_type", "mode", "ip", "port"]

def generate_csv(file_path, timestamp=None, traffic_type=None, mode=None, ip=None, port=None):
    # Check if the file exists
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    file_path += f"/traffic_generator_{traffic_type}_{mode}_{timestamp}.csv"
    print(file_path)
     
    if os.path.exists(file_path):

        # Open the file in write mode
        with open(file_path, mode='a', newline='') as f:
            writer = csv.writer(f)

            # Write the data rows            
            writer.writerow([timestamp, traffic_type, mode, ip, port])

        print("CSV file appended successfully!")

    else:
        with open(file_path, mode='w', newline='') as f:
            writer = csv.writer(f)

            # Write the column headers
            writer.writerow(header)

            writer.writerow([timestamp, traffic_type, mode, ip, port])
        
        print("CSV file created successfully!")

if __name__ == '__main__':
    generate_csv()