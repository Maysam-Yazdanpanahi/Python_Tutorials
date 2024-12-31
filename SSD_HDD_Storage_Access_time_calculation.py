import os
import shutil
from time import time  
i=0
def measure_write_speed(drive, test_file='Deleteit', file_size_mb=100):  
    # Create a test file of specified size  
    global i
    i += 1
    file_size_bytes = file_size_mb * 1024 * 1024  # Convert MB to Bytes  
    path = os.path.join(drive, test_file+str(i)+'.tmp')  
    print('Writing into',path,end='\t')
    # Write speed test  
    Start = time()  
    with open(path, 'wb') as f:  
        f.write(os.urandom(file_size_bytes))
    Stop = time()
    write_time = Stop - Start  
    write_speed = file_size_bytes / (1024 * 1024) / write_time  # MB/s  
    return write_speed  

def measure_Read_speed(drive, test_file='Deleteit', file_size_mb=100):  
    # Create a test file of specified size  
    global i
    i += 1
    file_size_bytes = file_size_mb * 1024 * 1024  # Convert MB to Bytes  
    path = os.path.join(drive, test_file+str(i)+'.tmp')  
    print('Reading ',path,end='\t')
    # Read speed test  
    Start = time()  
    with open(path, 'rb') as f:  
        a = f.read()
    Stop = time()
    read_time = Stop - Start  
    read_speed = file_size_bytes / (1024 * 1024) / read_time  # MB/s  

    # Clean up the test file
    Clean = input('Clean temporary file?')
    if Clean != '' and Clean[0].upper == 'Y':
        os.remove(path) 
    return read_speed

def measure_Copy_speed(drive, test_file='Deleteit', file_size_mb=100):  
    # Create a test file of specified size  
    global i
    i += 1
    file_size_bytes = file_size_mb * 1024 * 1024  # Convert MB to Bytes  
    path = os.path.join(drive, test_file+str(i)+'.tmp')  

    # Read speed test
    Directory = input('Enter a new folder to copy data: ')
    if Directory == '':
        Directory='testing'
    if not os.path.exists(os.path.join(drive,Directory)):
        os.makedirs(os.path.join(drive,Directory))
    Newpath = os.path.join(drive,Directory,test_file+str(i))
    print(f'Copying from {path} to {Newpath}',end='\t')
    Start = time()      
    shutil.copy2(path,Newpath)
    Stop = time()
    Copy_time = Stop - Start  
    Copy_speed = file_size_bytes / (1024 * 1024) / Copy_time  # MB/s  

    # Clean up the test file

    return Copy_speed

if __name__ == "__main__":
    try:
        file_size_mb = int(input('Enter the size of file in MebiByte: '))
    except ValueError:
        print('Enter a valid value!')
    else:     
        ssd_drive = 'C:'  # Adjust if needed  
        hdd_drives = ['D:', 'E:','F:']  # List your HDD drives here
        Removable_drive = 'O:'
        # Measure SSD speed
        function = input('Writing test or reading test or copying test: ')
        if function[0].upper() == 'W':
            ssd_write_speed = measure_write_speed(ssd_drive,'Delete_me', file_size_mb)  
            print(f"SSD (Drive {ssd_drive}): Write Speed: {ssd_write_speed:.2f} MB/s")  
            # Measure each HDD speed  
            for hdd in hdd_drives:  
                hdd_write_speed = measure_write_speed(hdd,'Delete_me', file_size_mb)  
                print(f"HDD (Drive {hdd}): Write Speed: {hdd_write_speed:.2f} MB/s")  
            try:
                Pendrive_write_speed = measure_write_speed(Removable_drive,'Delete_me', file_size_mb)
            except FileNotFoundError as ERR:
                print(f'Insert a penDrive(Flash Drive){ERR}')
            else:
                print(f"Removable (Drive {Removable_drive}): Write Speed: {Pendrive_write_speed:.2f} MB/s")
        
        elif function[0].upper() == 'R':
            ssd_read_speed = measure_Read_speed(ssd_drive,'Delete_me', file_size_mb)  
            print(f"SSD (Drive {ssd_drive}): Read Speed: {ssd_read_speed:.2f} MB/s")  
            # Measure each HDD speed  
            for hdd in hdd_drives:  
                hdd_read_speed = measure_Read_speed(hdd,'Delete_me', file_size_mb)  
                print(f"HDD (Drive {hdd}): Read Speed: {hdd_read_speed:.2f} MB/s")  

            Pendrive_read_speed = measure_Read_speed(Removable_drive,'Delete_me', file_size_mb)  
            print(f"Removable (Drive {Removable_drive}): Read Speed: {Pendrive_read_speed:.2f} MB/s")
            
        elif function[0].upper() == 'C':
            ssd_Copy_speed = measure_Copy_speed(ssd_drive,'Delete_me', file_size_mb)  
            print(f"SSD (Drive {ssd_drive}): Copy Speed: {ssd_Copy_speed:.2f} MB/s")  
            # Measure each HDD speed  
            for hdd in hdd_drives:  
                hdd_Copy_speed = measure_Copy_speed(hdd,'Delete_me', file_size_mb)  
                print(f"HDD (Drive {hdd}): Copy Speed: {hdd_Copy_speed:.2f} MB/s")  

            Pendrive_Copy_speed = measure_Copy_speed(Removable_drive,'Delete_me', file_size_mb)  
            print(f"Removable (Drive {Removable_drive}): Copy Speed: {Pendrive_Copy_speed:.2f} MB/s")