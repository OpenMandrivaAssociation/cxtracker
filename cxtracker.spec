%define name cxtracker
%define version 0.9.8

Name: %{name}
Summary: Connection Tracker - is a passive network connection tracker
Version: %{version}
Release: 1
License: GPLv3
Group: Monitoring
Source: https://github.com/gamelinux/cxtracker/archive/%{version}.tar.gz
URL:	https://github.com/gamelinux/cxtracker
Requires: perl-Net-Pcap perl-Getopt-Long-Descriptive perl-DateTime perl-NetPacket
BuildRequires: libpcap-devel

%description
CxTracker (Connection Tracker) is a passive network connection tracker 
for profiling, history, auditing and network discovery. It can be used 
as an replacement for sancp in the sguil setup. It handles vlan (2 layers)
and IPv6 out of the box.

%prep
%setup -n 

%install
cd src/
%make 
mkdir -p %{buildroot}%{_bindir}
install -m 755 cxtracker %{buildroot}%{_bindir}
install -m 755 ../sbin/cxtracker.pl %{buildroot}%{_bindir}

%files
%defattr(0755,root,root)
%{_bindir}/cxtracker
%{_bindir}/cxtracker.pl
