%define	upstream_name    Object-Realize-Later
%define	upstream_version 0.18

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 2

Summary:	CPAN %{upstream_name} perl module
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/Object-Realize-Later/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MA/MARKOV/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module helps you implementing delay loading of object-data.  While
creating a stub-object, Object::Realize::Later simulates you got the
real data.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/Object/Realize
