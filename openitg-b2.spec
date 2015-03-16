%define debug_package %{nil}

Name:		openitg
Version:	b2
Release:	1%{?dist}
Summary:	OpenITG Beta 2

Group:		OpenITG
License:	GPL2
URL:		https://github.com/openitg/openitg
Source0:	openitg-b2.tgz
AutoReq:	0

Requires: glibc.i686
Requires: libX11.i686
Requires: libXtst.i686
Requires: mesa-libGL.i686
Requires: mesa-libGLU.i686
Requires: libpng12.i686
Requires: libjpeg-turbo.i686
Requires: libusb.i686
Requires: libXrandr.i686
Requires: mesa-dri-drivers.i686

%description
An open-source rhythm dancing game based on StepMania 3.95

%prep
%setup -q
%build

%install
mkdir -p $RPM_BUILD_ROOT/opt/openitg/
cp -pR . $RPM_BUILD_ROOT/opt/openitg/

%clean

%files
"/*"
%doc
%changelog
