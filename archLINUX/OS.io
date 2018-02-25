<html> By #BASHEL@GODARMYserver.I/O
	<head>
		<style>
			body{
			background-color:black;
				color:white;
				font-size:145%;
			} b {
			background-color:lightgrey;
				color:black;
			}
		</style>
	</head>

<body><pre> <h1>INSTALLATIONarchlinux i686 x32bit BIOS NOT UEFI</h1>
		
this page guides you to the full process of a default archlinux OS.
put usb or dvd then boot the system for a console then execute those shell codes:
============================================================================================
<b>loadkeys fr</b>
<b>ls /usr/share/kbd/consolefonts</b>
<b>setfont /usr/share/kbd/consolefonts/ter-132n</b>
OR seclect a 8x16 or 10x22 (depend on wat u hv on list)
=============================================================================================
0. PQRTITIONING USING cfdisk  
----------------------------
<b>cfdisk /dev/sda</b>
 /boot/sda1 (1GiB) : bootable,
 root/sda2 (70GiB) . primary all,
 swap/sda3 (4GiB) this way: go to type : 82 linux swap / so~
 click write
 u type yes on the write option confirmation before u hit enter
 =============================================================================================
1. partitioning using parted
---------------------------
<b>parted /dev/sda</b>
To then create a new MBR/msdos partition table for BIOS systems, use the following command:
(parted) <b>mklabel msdos</b>

In the final example, separate /boot/sda1 (1GiB), root/sda2 (70GiB), swap/sda3 (4GiB) this way:

(parted) <b>mkpart primary ext3 1MiB 1GiB</b>
(parted) <b>set 1 boot on</b>
(parted) <b>mkpart primary ext3 500MiB 70GiB</b>
(parted) <b>mkpart primary linux-swap 70GiB 100%</b>
================================================================================================
<b>reboot</b>
-----------------------------------------------------------------------------------------------
<b>mkfs.ext3 /dev/sda1</b>
<b>mkfs.ext4 /dev/sda2</b>

<b>mkswap /dev/sda3</b>
<b>swapon /dev/sda3</b>

<b>mkdir /mnt/boot</b>
<b>mount /dev/sda1 /mnt/boot</b>
<b>mount /dev/sda2 /mnt</b>

<b>pacstrap -i /mnt base base-devel</b>
<b>genfstab /mnt -U -p /mnt >> /mnt/etc/fstab</b>
<b>arch-chroot /mnt /bin/bash</b>

------------------------------------------------------------------------------------------
<b>nano /etc/locale.gen</b>
en.us utf8 REMOVE DIEZE
fr~utf8 REMOVE DIEZE
uk.gb~ REMOVE DIEZE
----------------------------------------------------------------------------------------
now save and exit nano then you push this shell code into console out of nano and press enter.

<b>locale-gen</b>
----------------------------------------------------------------------------------------
<b>echo LANG=en_US.UTF-8 > /etc/locale.conf</b>
<b>export LANG=en_US.UTF-8</b>
----------------------------------------------------------------------------------------
<b>nano /etc/vconsole.conf</b>
KEYMAP=fr-latin9
FONT=lat9w-16
----------------------------------------------------------------------------------------
push this shell code into console out of nano:
<b>ln -sf /usr/share/zoneinfo/Africa/Morocco /etc/localtime</b>
<b>hwclock --syntohc</b>
-----------------------------------------------------------------------------------------
<b>echo GODARMYserver > etc/hostname</b>

<b>nano etc/hosts</b>
127.0.0.1     localhost.localdomaine     GODARMYserver
-----------------------------------------------------------------------------------------
<b>linux-lts</b>
<b>mkinitcpio -p linux-lts</b>
<b>passwd</b>
<b>pacman -S grub</b>
<b>grub-install --recheck /dev/sda</b>
<b>grub-mkconfig -o /boot/grub/grub.cfg</b>
-----------------------------------------------------------------------------------------
<b>umount -R /mnt</b>
<b>exit</b>
<b>reboot</b>
===============================================================================
*****i skipped the useradd phase but u can do it*******

<b>useradd -m -g users -G wheel -s /bin/bash CHOOSEANDPUTAANAMEE</b>
<b>passwd ANDPUthAtNAMEE</b>

<b>EDITOR=nano visudo</b>
UNCOMMA REMOVE DIEZE FROM WHEEL LINE ALL ALL ANY COMMAND SAVE AND EXIT NANO

<b>exit</b>
------------
loginNONroot account
=============================================================================
<b>nano /etc/pacman.d/mirrorlist</b> ********no fr no volzvagn and only https**********
<b>pacman -Syu</b>
<b>pacman -S python xdg-user-dirs zip unzip unrar</b>
<b>pacman -S gst-plugins-good gst-plugins-bad gst-plugins-ugly gst-libav</b>

<b>pacman -S xorg xorg-server xorg-xinit xorg-apps </b>
<b>pacman -S xf86-video-intel xf86-input-mouse xf86-input-keyboard </b>

 <b>pacman -S lxdm</b>
 <b>sytemctl enable lxdm.service</b>
 <b>pacman -S xfce4 ntp git</b>

-------audio---------
<b>pacman -S alsa-utils pulseaudio-alsa pulseaudio pavucontrol</b>
<b>alsamixer</b>
<b>alsactl store</b>
 
<b>shutdown -h now</b>
==================================================
extra configuration settings in case of network lost
===============================================
--add a luncher /usr/bin/pavucontrolon GUI MODE
<b>systemctl enable dhcpcd</b>
or
<b>pacman -S neworkmanager</b>
<b>systemctl enable NetworkManager</b>
		</pre>
</body>
	CONGRATULATION YOU DID COMPLETE THE INSTALLATION SUCCESSFULLY NOW REMOVE THE F***dvd or usb then push REBOOT RAUGH BUTTON !!! yaayyy!!!!
	HAAAPPYYYYY BOOOOOTTTUUUUPPPP§§§§!!!!!! HIGH 5, BBYE.
</html>
