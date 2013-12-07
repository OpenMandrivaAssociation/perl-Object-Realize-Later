%define	modname	Object-Realize-Later
%define	modver	0.18

Summary:	CPAN %{modname} perl module
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	10
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/Object-Realize-Later/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MA/MARKOV/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel

%description
This module helps you implementing delay loading of object-data.  While
creating a stub-object, Object::Realize::Later simulates you got the
real data.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Object/Realize
%{_mandir}/man3/*

