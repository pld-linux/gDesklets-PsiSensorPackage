%define		pname	PsiSensorPackage
Summary:	This package contains all Psi sensors
Summary(pl):	Ten pakiet zawiera wszystkie czujniki Psi
Name:		gDesklets-%{pname}
Version:	20031028
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	http://gdesklets.gnomedesktop.org/files/%{pname}-%{version}.tar.bz2
# Source0-md5:	24c891e1d0f66426040b4e4fb618f9f5
URL:		http://gdesklets.gnomedesktop.org/categories.php?func=gd_show_app&gd_app_id=38
BuildRequires:	python >= 1:2.3
BuildRequires:	python-pygtk-gtk >= 1.99.18
Requires:	gDesklets
%pyrequires_eq	python-libs
Provides:	gDesklets-sensor
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sensorsdir	%{_datadir}/gdesklets/Sensors

%description
This package contains all Psi sensors.

%description -l pl
Ten pakiet zawiera wszystkie czujniki Psi.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sensorsdir}

# Don't include FontSelector here - it's in gDesklets package
SENSORS="CPU Disk ExternalInterval IconButton Memo MemoOver Memory Network Ping popmail Theme VariableBorder"

for i in $SENSORS; do
	cd $i-*
	[ -f ChangeLog ] && mv ChangeLog ChangeLog-$i
	[ -f README ] && mv README README-$i
	
	./Install_${i}_Sensor.bin --nomsg \
		$RPM_BUILD_ROOT%{_sensorsdir}
		
	cd ..
done

rm -rf $RPM_BUILD_ROOT%{_sensorsdir}/*/{.order,ChangeLog,Makefile*}

%py_comp $RPM_BUILD_ROOT%{_sensorsdir}
%py_ocomp $RPM_BUILD_ROOT%{_sensorsdir}

rm -f $RPM_BUILD_ROOT%{_sensorsdir}/*/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc */ChangeLog-* */README-*
%{_sensorsdir}/*
