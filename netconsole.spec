Summary:	An initscript to load netconsole.ko module
Summary(pl.UTF-8):	Skrypt inicjalizujący do wczytywania modułu netconsole.ko
Name:		netconsole
Version:	0.2
Release:	2
License:	GPL
Group:		Base
Source0:	%{name}.init
Source1:	%{name}.sysconfig
Source2:	http://glen.alkohol.ee/pld/netconsole.txt
# Source2-md5: 9bef22121ef926b789940b8a51092a3a
# Documentation/networking/netconsole.txt (2.6.25.17)
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An initscript to load netconsole kernel module.

%description -l pl.UTF-8
Skrypt inicjalizujący do wczytywania modułu jądra netconsole.

%prep
%setup -qcT
cp -a %{SOURCE2} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}

install %{SOURCE0} $RPM_BUILD_ROOT/etc/rc.d/init.d/netconsole
install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/netconsole

%clean
rm -rf "$RPM_BUILD_ROOT"

%post
/sbin/chkconfig --add netconsole
# nothing to restart - no rc-script stop

%preun
if [ "$1" = "0" ]; then
	# nothing to stop - no rc-script stop
	/sbin/chkconfig --del netconsole
fi

%files
%defattr(644,root,root,755)
%doc netconsole.txt
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/netconsole
%attr(754,root,root) /etc/rc.d/init.d/netconsole
