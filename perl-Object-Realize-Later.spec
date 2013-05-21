%define	upstream_name    Object-Realize-Later
%define	upstream_version 0.18

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	CPAN %{upstream_name} perl module
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/Object-Realize-Later/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MA/MARKOV/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module helps you implementing delay loading of object-data.  While
creating a stub-object, Object::Realize::Later simulates you got the
real data.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
make
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/Object/Realize


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.180.0-4mdv2012.0
+ Revision: 765541
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.180.0-3
+ Revision: 764064
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.180.0-2
+ Revision: 667283
- mass rebuild

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.180.0-1mdv2011.0
+ Revision: 401997
- rebuild using %%perl_convert_version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.18-2mdv2009.0
+ Revision: 223950
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.18-1mdv2008.1
+ Revision: 140694
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdv2008.0
+ Revision: 46656
- update to new version 0.18


* Mon Nov 20 2006 Oden Eriksson <oeriksson@mandriva.com> 0.15-2mdv2007.0
+ Revision: 85609
- use the mkrel macro
- Import perl-Object-Realize-Later

* Sat Jul 09 2005 Andreas Hasenack <andreas@mandriva.com> 0.15-1mdk
- packaged for Mandriva

