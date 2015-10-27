# InstallTheGroove
A custom installation of Fedora 21 geared towards arcade cabinets running Stepmania and its derivatives.

### What's in here?
- a simple kickstart file. It is VERY bare-bones, and is what i use for the pre-built ISO.

- spec files for the source tarball of stepmania 5.0, and simply love. dguzek ported the theme.

### How do I use this?

There are two pre-built ISOs I've generated: [a 64-bit ISO](http://bit.ly/2041TL7) for modern, home-built PCs, and [a 32-bit ISO](http://bit.ly/1MPUYve) which should work in an MK6 or a BoXoR. The 32-bit ISO can theoretically work on all hardware, but using the 64-bit flavor is recommended when possible.

# The install disc will automatically format your hard drive. This is by design. You have been warned.

### OK I have it installed, now what?

The system auto-logins to a fluxbox session.
The username is *itg* and the password is *changeme*

Right-click anywhere on the desktop to bring up the menu. *Lilyterm* is the terminal emulator, and *Leafpad* is a text editor. You can also launch OpenITG and Stepmania 5 directly from here. Firefox is included.

#### How do I install the PIUIO driver?
Open a `lilyterm` session and punch in the following:

```
cd utils
sudo ./piu.sh
```

it will ask for your password, which if not changed from the default, is `changeme`

#### How do I change the password?

I'm glad you asked! Just enter `passwd` on the command prompt and follow the instructions.

### How do I install just the games on my own Fedora 21 install?
stepmania5 can be installed with a single command:

`sudo yum -y install http://teknolust.org/static/stepmania-5.0.9-1.fc21.x86_64.rpm`

You'll need the `libmad` libraries, which can be obtained via the rpmfusion repos.

And since nobody wants to play on an arcade cabinet without (sighs heavily) Simply Love, I packaged that into an RPM also:

`sudo yum -y install http://teknolust.org/static/stepmania-simplylove-20150201-1.fc21.x86_64.rpm`

Linux philosophy is for packages to leave existing settings in place, so you'll have to pick the theme in-game after installing. This only needs to be done once.

Stepmania is installed in `/opt/stepmania-5.0`

OpenITG is available. As far as I can tell, it works "as designed" with all of its known buggy behaviour included. If you're on a 64-bit distro, you'll have to manually install a bunch of 32-bit libraries to get the game to run.

```
sudo yum -y install glibc.i686 libX11.i686 libXtst.i686 mesa-libGL.i686 mesa-libGLU.i686 libpng12.i686 libjpeg-turbo.i686 libusb.i686 libXrandr.i686 mesa-dri-drivers.i686 libvorbis.i686 libogg.i686 alsa-lib.i686
sudo yum -y install http://download1.rpmfusion.org/free/fedora/releases/21/Everything/i386/os/libmad-0.15.1b-17.fc21.i686.rpm
sudo yum -y install http://teknolust.org/static/openitg-b2-1.fc21.x86_64.rpm
```

Please be aware this is just a 32-bit build of OpenITG running cleanly on a 64-bit box. The game still runs into the 4GB memory limit.

On a 32-bit OS, it's much simpler:

```
sudo yum -y install http://download1.rpmfusion.org/free/fedora/releases/21/Everything/i386/os/libmad-0.15.1b-17.fc21.i686.rpm
sudo yum -y install http://teknolust.org/static/openitg-b2-1.fc21.i686.rpm
```

The game is installed in `/opt/openitg`.
