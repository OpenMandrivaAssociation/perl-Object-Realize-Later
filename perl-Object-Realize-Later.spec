%define	real_name Object-Realize-Later

Summary:	CPAN %{real_name} perl module
Name:		perl-%{real_name}
Version:	0.15
Release:	%mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/M/MA/MARKOV/%{real_name}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/Object-Realize-Later/
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
This module helps you implementing delay loading of object-data.  While
creating a stub-object, Object::Realize::Later simulates you got the
real data.

%prep
%setup -q -n %{real_name}-%{version}

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


