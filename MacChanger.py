import subprocess
import optparse
import re
def getInput():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="interface to change")
    parse_object.add_option("-m","--mac",dest="mac",help="new mac address")

    return parse_object.parse_args()

def changeMac(user_interface,user_mac):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac])
    subprocess.call(["ifconfig",user_interface,"up"])

def check(interface):
    ifconfig = subprocess.check_output(["ifconfig",inputs.interface]).decode("utf-8")
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig)

    if new_mac: 
        return new_mac.group(0)

(inputs,arguments) = getInput()
changeMac(inputs.interface,inputs.mac)
final_mac = check(inputs.interface)
if final_mac == inputs.mac :
    print("Mac Address Change Successfully")
