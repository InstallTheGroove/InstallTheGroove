Name:		stepmania
Version:	5.0
Release:	1%{?dist}
Summary:	this is a game where you use your feet

Group:		Stepmania
License:	GPL2
URL:		http://www.stepmania.com
Source0:	stepmania-5.0.tgz
AutoReq:	0



BuildRequires: atk
BuildRequires: atk-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: bash
BuildRequires: binutils
BuildRequires: bzip2-devel
BuildRequires: bzip2-libs
BuildRequires: cairo
BuildRequires: cairo-devel
BuildRequires: coreutils
BuildRequires: cpio
BuildRequires: diffutils
BuildRequires: dwz
BuildRequires: elfutils
BuildRequires: file
BuildRequires: findutils
BuildRequires: fontconfig
BuildRequires: freetype
BuildRequires: gawk
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gdb
BuildRequires: gdk-pixbuf2
BuildRequires: gdk-pixbuf2-devel
BuildRequires: git
BuildRequires: glew-devel
BuildRequires: glib2
BuildRequires: glib2-devel
BuildRequires: glibc
BuildRequires: glibc-common
BuildRequires: glibc-devel
BuildRequires: glibc-headers
BuildRequires: grep
BuildRequires: gtk2
BuildRequires: gtk2-devel
BuildRequires: gzip
BuildRequires: hostname
BuildRequires: kernel-headers
BuildRequires: libGLEW
BuildRequires: libX11
BuildRequires: libX11-devel
BuildRequires: libXrandr
BuildRequires: libXrandr-devel
BuildRequires: libXrender-devel
BuildRequires: libgcc
BuildRequires: libjpeg-turbo
BuildRequires: libjpeg-turbo-devel
BuildRequires: libmad
BuildRequires: libmad-devel
BuildRequires: libogg
BuildRequires: libogg-devel
BuildRequires: libpng
BuildRequires: libpng-devel
BuildRequires: libstdc++
BuildRequires: libstdc++-devel
BuildRequires: libvorbis
BuildRequires: libvorbis-devel
BuildRequires: m4
BuildRequires: make
BuildRequires: mesa-libGL
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU
BuildRequires: mesa-libGLU-devel
BuildRequires: nasm
BuildRequires: pango
BuildRequires: pango-devel
BuildRequires: perl
BuildRequires: perl-podlators
BuildRequires: pkgconfig
BuildRequires: rsync
BuildRequires: sed
BuildRequires: tar
BuildRequires: xorg-x11-proto-devel

Requires: atk
Requires: autoconf
Requires: automake
Requires: bash
Requires: binutils
Requires: cairo
Requires: coreutils
Requires: cpio
Requires: diffutils
Requires: dwz
Requires: elfutils
Requires: file
Requires: findutils
Requires: fontconfig
Requires: freetype
Requires: gawk
Requires: gdk-pixbuf2
Requires: glib2
Requires: glibc
Requires: glibc-common
Requires: grep
Requires: gtk2
Requires: gzip
Requires: hostname
Requires: libGLEW
Requires: libX11
Requires: libXrandr
Requires: libgcc
Requires: libjpeg-turbo
Requires: libmad
Requires: libogg
Requires: libpng
Requires: libstdc++
Requires: libvorbis
Requires: m4
Requires: make
Requires: mesa-libGL
Requires: mesa-libGLU
Requires: nasm
Requires: pango
Requires: perl
Requires: perl-podlators
Requires: pkgconfig
Requires: rsync
Requires: sed
Requires: tar


%description
StepMania is a free dance and rhythm game for Windows, Mac, and Linux. It features 3D graphics, keyboard and "dance pad" support, and an editor for creating your own steps.

%prep
%setup -q


%build
./autogen.sh
./configure --with-minimaid
make


%install
make install DESTDIR=$RPM_BUILD_ROOT
%files
"/opt/*"
%doc
%changelog
