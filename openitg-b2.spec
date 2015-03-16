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
