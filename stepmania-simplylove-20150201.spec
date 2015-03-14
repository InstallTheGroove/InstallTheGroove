Name:		stepmania-simplylove
Version:	20150201
Release:	1%{?dist}
Summary:	The Simply Love theme for Stepmania 5

Group:		Stepmania
License:	GPL2
URL:		https://github.com/dguzek/Simply-Love-SM5
Source0:	stepmania-simplylove-20150201.tgz
AutoReq:	0



Requires: stepmania

%description
A recreation of hurtpiggypig's Simply Love SM3.95 theme made to now run in StepMania 5

%prep
%setup -q
%build

%install
mkdir -p $RPM_BUILD_ROOT/opt/stepmania-5.0/Themes/SimplyLove
cp -pR . $RPM_BUILD_ROOT/opt/stepmania-5.0/Themes/SimplyLove/

%clean

%files
"/*"
%doc
%changelog
