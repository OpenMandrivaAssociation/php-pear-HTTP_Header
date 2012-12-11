%define		_class		HTTP
%define		_subclass	Header
%define		upstream_name	%{_class}_%{_subclass}

%define		_requires_exceptions pear(PHPUnit.php)

Name:		php-pear-%{upstream_name}
Version:	1.2.1
Release:	%mkrel 3
Summary:	OO-Interface to modify HTTP-Headers easily
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTTP_Header/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires(post): php-pear
Requires(preun): php-pear-HTTP >= 1.2
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This class provides methods to set/modify HTTP-Headers. To abstract
common things, like caching etc. some sub classes are provided that
handle special cases (i.e. HTTP_Header_Cache).

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{upstream_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-3mdv2012.0
+ Revision: 742009
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-2
+ Revision: 679360
- mass rebuild

* Sat Oct 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.1-1mdv2011.0
+ Revision: 587643
- update to new version 1.2.1

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.0-6mdv2010.1
+ Revision: 477895
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.2.0-5mdv2010.0
+ Revision: 441185
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-4mdv2009.1
+ Revision: 322127
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-3mdv2009.0
+ Revision: 236886
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-2mdv2008.0
+ Revision: 15467
- rule out the PHPUnit.php dep


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-1mdv2007.0
+ Revision: 81782
- Import php-pear-HTTP_Header

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-1mdk
- 1.2.0
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-4mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-3mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-2mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-1mdk
- 1.1.2

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-1mdk
- initial Mandriva package (PLD import)

