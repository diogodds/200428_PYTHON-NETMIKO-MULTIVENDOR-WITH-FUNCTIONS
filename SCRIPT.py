#/usr/bin/env python

from netmiko import ConnectHandler 
from datetime import datetime
#import time
import sys
import getpass
import re

import warnings
warnings.filterwarnings(action='ignore',module='.*paramiko.*')

###########################################################################
# The three functions bellow will take specific action based on the device
###########################################################################

def COMNET():
    net_connect = ConnectHandler(device_type='cisco_ios', ip=dictionary['IP'], username=username, password=password, global_delay_factor=2.0)
      
    print('Connected to ' + dictionary['HOSTNAME'] + ' that runs COMNET software.')
        
    net_connect.send_command('\n')
    output = net_connect.send_command('show version', expect_string=r'#')
    print(output)

def ARUBA():
    net_connect = ConnectHandler(device_type='hp_procurve', ip=dictionary['IP'], username=username, password=password, global_delay_factor=3.0)
  
    print('Connected to ' + dictionary['HOSTNAME'] + ' that runs ARUBA software.')
    
    net_connect.send_command('\n')
    output = net_connect.send_command('Getmib sysDescr.0 ', expect_string=r'#')
    print(output)

def COMWARE():  
    net_connect = ConnectHandler(device_type='hp_comware', ip=dictionary['IP'], username=username, password=password, global_delay_factor=2.0)
  
    print('Connected to ' + dictionary['HOSTNAME'] + ' that runs COMWARE software.')
    
    net_connect.send_command('\n')
    net_connect.send_command('screen-length disable', expect_string=r'>')
    output = net_connect.send_command('display version', expect_string=r'>')
    print(output)
    

##############################################################################

username = 'dsantos'
password = getpass.getpass()

##############################################################################
# The code bellow will retrieve information about devices (IP, PASS, SW)
# and based on the SW running, will call one of the three functions defined
# previously, that will use NETMIKO to SSH to the devices and run some
# commands.
##############################################################################    

with open('DEVICE-ATTRIBUTES.txt') as file: # This opens the text file with the BGP parameters in csv format
    parameters = file.read().splitlines() # The file is loaded into the "parameters" variable and splited into lines
    
for line in parameters:
    attribute_per_device = line.split(',') # This is to split each element of a line on the csv files to objects on a list

    # A dictionary will be created based on the objects of each line of the list (for loop will be in charge of looping
    # through all lines in the csv / txt file
    dictionary = {'HOSTNAME':attribute_per_device[0],
                  'IP':attribute_per_device[1],
                  'SECRET':attribute_per_device[2],
                  'MANUFACTURER':attribute_per_device[3],   
                 }            
    
    print('#' * 60 + '\n' + 'Establishing connection to ' + dictionary['HOSTNAME'] + '.')    
    start_time = datetime.now()
    print(str(start_time.strftime("%Y-%m-%d %H:%M:%S")))
    
    if dictionary['MANUFACTURER'] == 'aruba':
       ARUBA()

    elif dictionary['MANUFACTURER'] == 'comware':
       COMWARE()

    else:
       COMNET()

    end_time = datetime.now()
    
    print('\nTotal time: {}'.format(end_time - start_time) +'\n' + '#' * 60)