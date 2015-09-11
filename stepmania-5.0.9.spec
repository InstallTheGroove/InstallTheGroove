Name:		stepmania
Version:	5.0.9
Release:	1%{?dist}
Summary:	this is a game where you use your feet

Group:		Stepmania
License:	GPL2
URL:		http://www.stepmania.com
Source0:	stepmania-5.0.9.tar.gz
AutoReq:	0


BuildRequires: alsa-lib-devel
BuildRequires: atk-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: bash
BuildRequires: binutils
BuildRequires: bzip2-devel
BuildRequires: bzip2-libs
BuildRequires: cairo-devel
BuildRequires: cmake
BuildRequires: coreutils
BuildRequires: cpio
BuildRequires: diffutils
BuildRequires: dwz
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gdk-pixbuf2-devel
BuildRequires: glew-devel
BuildRequires: glib2-devel
BuildRequires: glibc
BuildRequires: glibc-common
BuildRequires: glibc-devel
BuildRequires: glibc-headers
BuildRequires: gtk2-devel
BuildRequires: kernel-headers
BuildRequires: libX11-devel
BuildRequires: libXrandr-devel
BuildRequires: libXrender-devel
BuildRequires: libgcc
BuildRequires: libjpeg-turbo-devel
BuildRequires: libmad-devel
BuildRequires: libogg-devel
BuildRequires: libpng-devel
BuildRequires: libstdc++-devel
BuildRequires: libvorbis-devel
BuildRequires: m4
BuildRequires: make
BuildRequires: mesa-libEGL-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: nasm
BuildRequires: pango-devel
BuildRequires: pkgconfig
BuildRequires: pulseaudio-libs-devel
BuildRequires: xorg-x11-proto-devel
BuildRequires: yasm
BuildRequires: git
BuildRequires: chrpath

Requires: atk
Requires: coreutils
Requires: dwz
Requires: elfutils
Requires: freetype
Requires: gdk-pixbuf2
Requires: glib2
Requires: glibc
Requires: glibc-common
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
Requires: mesa-libGL
Requires: mesa-libGLU
Requires: pango
Requires: pulseaudio-libs
Requires: pkgconfig


%description
StepMania is a free dance and rhythm game for Windows, Mac, and Linux. It features 3D graphics, keyboard and "dance pad" support, and an editor for creating your own steps.

%prep
%setup -q


%build
./autogen.sh
./configure --with-minimaid
make


%install
#chrpath --delete %{buildroot}%{_bindir}/%{name}
#make install
make install DESTDIR=$RPM_BUILD_ROOT
%files
"/opt/*"
%doc
%changelog
