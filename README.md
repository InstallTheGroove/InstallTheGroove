# InstallTheGroove
A custom installation of Fedora 21 geared towards arcade cabinets running Stepmania and its derivatives.

### What's in here?
Right now, just a simple kickstart file. It is VERY bare-bones, and designed to be used with a minimal F21 bootable ISO and a single *mkisofs* command. This requires a network connection for installing packages. As the project progresses, the base packages will all be on the livecd, negating the need for internet. The process will also be documented here.

You can download a pre-built iso here: `http://teknolust.org/static/InstallTheGroove.iso`

### How do I use this?

You'll want some sort of a Linux environment. It doesn't need to be Fedora 21, these directions are distro-agnostic. It involves downloading the Fedora 21 Server bootable ISO, and the "stage2" squashfs.

```
mkdir ~/bootcd
mkdir ~/installthegroove
wget http://dl.fedoraproject.org/pub/fedora/linux/releases/21/Server/x86_64/os/images/boot.iso
sudo mount -o loop boot.iso ~/bootcd
cp -pR ~/bootcd/isolinux ~/installthegroove
cd ~/installthegroove
wget https://raw.githubusercontent.com/sherl0k/InstallTheGroove/master/ks.cfg
mkdir image
cd image
wget http://dl.fedoraproject.org/pub/fedora/linux/releases/21/Server/x86_64/os/LiveOS/squashfs.img
cd ..
sudo mkisofs -r -T -J -V "InstallTheGroove" -b isolinux.bin -c boot.cat -no-emul-boot -boot-load-size 4 -boot-info-table -v -o linuxboot.iso .
```

# The install disc will automatically format your hard drive. This is by design. You have been warned.

### OK I have it installed, now what?

If you are unsure how to log in, The username is *fedora* and the password is *Asdfqwerty*

Future releases will have a something more sane, and will auto-login (and auto-launch the game).

stepmania5 can be installed with a single command:

`yum -y install http://teknolust.org/static/stepmania-5.0-1.fc21.x86_64.rpm`

And since nobody wants to play on an arcade cabinet without (sighs heavily) Simply Love, I packaged that into an RPM also:

`yum -y install http://teknolust.org/static/stepmania-simplylove-20150201-1.fc21.x86_64.rpm`

Linux philosophy is for packages to leave existing settings in place, so you'll have to pick the theme in-game after installing. This only needs to be done once.

Stepmania is installed in `/opt/stepmania-5.0`
