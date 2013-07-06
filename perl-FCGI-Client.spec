#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	FCGI
%define		pnam	Client
%include	/usr/lib/rpm/macros.perl
Summary:	FCGI::Client - client library for fastcgi protocol
#Summary(pl.UTF-8):	
Name:		perl-FCGI-Client
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/T/TO/TOKUHIROM/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f039f3c4a8e2bc370a20f24f1537afc1
# generic URL, check or change before uncommenting
URL:		http://search.cpan.org/dist/FCGI-Client/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Any-Moose >= 0.13
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FCGI::Client is client library for fastcgi protocol.



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/FCGI/*.pm
%{perl_vendorlib}/FCGI/Client
%{_mandir}/man3/*
