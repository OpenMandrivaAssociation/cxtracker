%define name cxtracker
%define version 0.9.5

Name: %{name}
Summary: Connection Tracker - is a passive network connection tracker
Version: %{version}
Release: %mkrel 1
License: GPLv3
Group: Monitoring
Source: https://github.com/gamelinux/%{name}/zipball/%{version}
URL:	https://github.com/gamelinux/cxtracker
Requires: perl-Net-Pcap perl-Getopt-Long-Descriptive perl-DateTime libpcap1 perl-NetPacket
BuildRequires: libpcap-devel
BuildRoot: %_tmppath/%{name}-%{version}-buildroot

%description
CxTracker (Connection Tracker) is a passive network connection tracker 
for profiling, history, auditing and network discovery. It can be used 
as an replacement for sancp in the sguil setup. It handles vlan (2 layers)
and IPv6 out of the box.

%prep
%setup -n gamelinux-cxtracker-3e03b90

%install
cd src/
%make 
mkdir -p %{buildroot}/usr/local/sbin/
install -m 755 cxtracker %{buildroot}/usr/local/sbin/
install -m 755 ../sbin/cxtracker.pl %{buildroot}/usr/local/sbin/

%files
%defattr(0755,root,root)
/usr/local/sbin/cxtracker
/usr/local/sbin/cxtracker.pl

%clean
rm -rf $RPM_BUILD_ROOT
