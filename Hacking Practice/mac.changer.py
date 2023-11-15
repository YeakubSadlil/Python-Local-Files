#! usr/bin/python3 env

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options,arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify a new MAC address, use --help for more info")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", options.interface, "down"])
    subprocess.call(["ifconfig", options.interface, "hw", "ether", options.new_mac])
    subprocess.call(["ifconfig", options.interface, "up"])
    
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
    mac_address_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result)) # \w is a word character, \w\w is two word characters
    
    if mac_address_result:
        return mac_address_result.group(0)
    else:
        print("[-] There is no MAC address in this interface", options.interface)    

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC address is = " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface) # get the updated current mac address after changing it
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " + str(current_mac))