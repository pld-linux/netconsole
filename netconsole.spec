Summary:	An initscript to load netconsole.ko module
Summary(pl.UTF-8):	Skrypt inicjalizujący do wczytywania modułu netconsole.ko
Name:		netconsole
Version:	0.3
Release:	1
License:	GPL
Group:		Base
Source0:	%{name}.init
Source1:	%{name}.sysconfig
Source2:	http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=blob_plain;f=Documentation/networking/%{name}.txt
# Source2-md5:	98712ca5ba15aaf6df29e0eea0acd753
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An initscript to load netconsole kernel module.

For NetConsole Daemon, you can look at cancd package or use plain
syslog daemon.

%description -l pl.UTF-8
Skrypt inicjalizujący do wczytywania modułu jądra netconsole.

Demona NetConsole można znaleźć w pakiecie cancd.

%prep
%setup -qcT
cp -a %{SOURCE2} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}
install -p %{SOURCE0} $RPM_BUILD_ROOT/etc/rc.d/init.d/netconsole
cp -a %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/netconsole

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
