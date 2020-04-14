# Dumb ways to kill your system
Kill your (or not yours) system with style. Many ways on many languages to make your system be snapped by thanos itself.

# Bash

```
sudo chmod -R 777 /*; 
```
This will just make your entire system acessible using permissions.

```
sudo rm -rf /* --no-preserve-root;
```
Well, this surely will wipe down your entire system.


```
dd if=/dev/null of=/dev/sda; 
```
This will change every bite of your drive to 0's.

```
sudo mv /home/* /dev/null; 
```
This command will to move your entire users folder to the absolute void.

```
Mkfs.ext3 /dev/sda; 
```
This will format your drive entirely.

```
: () {: |: &} ;:
```
I's called fork bomb, and should make your system crashes, if you have one.

