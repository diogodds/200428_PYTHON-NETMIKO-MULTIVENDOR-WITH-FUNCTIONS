This Python script will define three functions.

The functions rely on netmiko, and will have diferent attributes and activos for devices of three different vendors (HPE, HP Aruba and COMNET).

Te main script will extract atttributes from a text file, and based on the OS information provided on the file, will call one of the three functions to SSH to the devices.
