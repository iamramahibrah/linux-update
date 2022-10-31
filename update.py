import os
import time

def logo():
	print("==========================")
	print("   CYBER.IO LABS TOOLS")
	print("==========================")
logo()


def check_privileges():
	if not os.environ.get("SUDO_UID") and os.geteuid() != 0:
        raise PermissionError("You need to run this script with sudo or as root.")
check_privileges()

def update():
	print("updating....")
	time.sleep(2)
	# update & upgrade
	os.system('sudo apt update -y && sudo apt upgrade -y')

	# apt autoclean 
    os.system('sudo apt autoclean -y && sudo apt autoremove -y')

    # apt-get autoclean & autoremove
    os.system('sudo apt-get autoclean -y && sudo apt-get autoremove -y')

	# apt-get update & upgrade 
	os.system('sudo apt-get update -y && sudo apt-get upgrade -y')
	
update()

def distro_upgrade():
	print("distro upgrading....")
	time.sleep(2)
	os.system('autoclean -y')
	os.system('sudo apt-get dist-upgrade -y') 
distro_upgrade()
