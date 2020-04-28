This Python script will define three functions.

The functions rely on netmiko, and will have diferent attributes and actioms for devices of three different vendors (HPE, HP Aruba and COMNET).

The main script will extract devices atttributes from a text file, and based on the OS information provided on the file, will call one of the three functions to SSH to the devices and run some basic commands.
