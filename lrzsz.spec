Summary: The lrz and lsz modem communications programs
Name: lrzsz
Version: 0.12.21
Release: %mkrel 17
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
make -j1

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




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.12.21-15mdv2011.0
+ Revision: 666097
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.12.21-14mdv2011.0
+ Revision: 606421
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.12.21-13mdv2010.1
+ Revision: 519033
- rebuild

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.12.21-12mdv2010.0
+ Revision: 426007
- rebuild

* Sun Dec 21 2008 Oden Eriksson <oeriksson@mandriva.com> 0.12.21-11mdv2009.1
+ Revision: 317042
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.12.21-10mdv2009.0
+ Revision: 223128
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.12.21-9mdv2008.1
+ Revision: 152872
- rebuild
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Mar 07 2007 Oden Eriksson <oeriksson@mandriva.com> 0.12.21-7mdv2007.0
+ Revision: 134432
- Import lrzsz

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.12.21-7mdk
- Rebuild

* Tue Jun 07 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.12.21-6mdk
- Rebuild

* Sun May 23 2004 Abel Cheung <deaddog@deaddog.org> 0.12.21-5mdk 
- Avoid regeneration of auto* files which would fail
- Convert names into UTF-8

