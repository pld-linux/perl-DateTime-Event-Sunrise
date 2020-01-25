#
# Conditional build:
%bcond_without	tests		# perform "make test"
#
%define	pdir	DateTime
%define	pnam	Event-Sunrise
Summary:	DateTime::Event::Sunrise - Perl DateTime extension for computing the sunrise/sunset on a given day
Summary(pl.UTF-8):	DateTime::Event::Sunrise - moduł Perla do obliczania wschodów i zachodów Słońca
Name:		perl-DateTime-Event-Sunrise
Version:	0.0505
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9aa0c4e005d6b8c985f1e9ae8d04047c
URL:		http://search.cpan.org/dist/DateTime-Event-Sunrise/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module will computes the time of sunrise and sunset for a given
date and a given location. The computation uses Paul Schlyter's
algorithm.
Actually, the module creates a DateTime::Event::Sunrise object or
a DateTime::Set object, which are used to generate the sunrise or
the sunset times for a given location and for any date.

%description -l pl.UTF-8
Ten moduł oblicza momenty wschodów i zachodów Słońca dla
podanej daty i lokalizacji. Obliczenia wykorzystują algorytm Paula
Schlytera. Moduł tworzy obiekty typu DateTime::Event::Sunrise lub
DateTime::Set.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/DateTime/Event/Sunrise.pm
%{_mandir}/man3/DateTime::Event::Sunrise.*
