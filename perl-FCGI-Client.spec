#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	FCGI
%define		pnam	Client
Summary:	FCGI::Client - client library for fastcgi protocol
Name:		perl-FCGI-Client
Version:	0.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/FCGI/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d3e621b79a96ea1463331e33cf337524
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

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
        --destdir=$RPM_BUILD_ROOT \
        --installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%{perl_vendorlib}/FCGI/*.pm
%{perl_vendorlib}/FCGI/Client
%{_mandir}/man3/*
