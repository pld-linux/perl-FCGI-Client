#
# Conditional build:
%bcond_without	tests		# unit tests

%define		pdir	FCGI
%define		pnam	Client
Summary:	FCGI::Client - client library for FastCGI protocol
Summary(pl.UTF-8):	FCGI::Client - biblioteka kliencka do protokołu FastCGI
Name:		perl-FCGI-Client
Version:	0.09
Release:	1
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/FCGI/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d3e621b79a96ea1463331e33cf337524
URL:		https://metacpan.org/dist/FCGI-Client
BuildRequires:	perl-Module-Build-Tiny >= 0.035
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Moo >= 2
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Type-Tiny
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FCGI::Client is client library for FastCGI protocol.

%description -l pl.UTF-8
FCGU::Client to biblioteka kliencka do protokołu FastCGI.

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
%{perl_vendorlib}/FCGI/Client.pm
%{perl_vendorlib}/FCGI/Client
%{_mandir}/man3/FCGI::Client*.3*
