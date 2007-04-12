%define name lrzsz
%define version 0.12.21
%define release %mkrel 7

Summary: The lrz and lsz modem communications programs
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Communications
URL: http://www.ohse.de/uwe/software/lrzsz.html
Source: %{name}-%{version}.tar.bz2
Patch1: %{name}-0.12.20-glibc21.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Lrzsz (consisting of lrz and lsz) is a cosmetically modified
zmodem/ymodem/xmodem package built from the public-domain version of the
rzsz package.  Lrzsz was created to provide a working GNU copylefted
Zmodem solution for Linux systems.  

You should install lrzsz if you're also installing a Zmodem communications
program that uses lrzsz.  If you're installing minicom, you need to install
lrzsz.

%prep
%setup -q
%patch1 -p1 -b .glibc21

# because of time skew between various generated files, autotools are
# forced to run. In the process, gettext-devel is required but new
# gettext-devel is not compatible with lrzsz, thus autotools will fail
find -type f -print0 | xargs -0 touch

%build
%configure	--disable-pubdir \
		--enable-syslog \
		--program-transform-name=s/l//
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*


