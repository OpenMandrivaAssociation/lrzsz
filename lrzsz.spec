Summary:	The lrz and lsz modem communications programs
Name:		lrzsz
Version:	0.12.21
Release:	25
License:	GPLv2
Group:		Communications
Url:		http://www.ohse.de/uwe/software/lrzsz.html
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-0.12.21-automake-1.13.patch
Patch1:		%{name}-0.12.20-glibc21.patch

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
%apply_patches

# because of time skew between various generated files, autotools are
# forced to run. In the process, gettext-devel is required but new
# gettext-devel is not compatible with lrzsz, thus autotools will fail
find -type f -print0 | xargs -0 touch

%build
%configure2_5x \
	--disable-pubdir \
	--enable-syslog \
	--program-transform-name=s/l//
%make

%install
%makeinstall

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/*
%{_mandir}/man1/*

