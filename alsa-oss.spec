Summary:	Advanced Linux Sound Architecture - OSS compatibility wrapper library & script
Summary(pl):	Advanced Linux Sound Architecture - biblioteka i skrypt kompatibilności z OSS
Name:		alsa-oss
Version:	1.0.1
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	ftp://ftp.alsa-project.org/pub/oss-lib/%{name}-%{version}.tar.bz2
# Source0-md5:	3d38c2702fa000cf01d78f690f0e14fc
URL:		http://www.alsa-project.org/
BuildRequires:	alsa-lib-devel >= 1.0.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the ALSA -> OSS compatibility library and simple
wrapper script which facilitates its use. This script just sets the
appropriate LD_PRELOAD path and then runs the command.

%description -l pl
Ten pakiet zawiera bibliotekę kompatybilności ALSA -> OSS oraz prosty
wrapper który ułatwia jej użycie, po prostu ustawiając odpowiednie
LD_PRELOAD i uruchamiając polecenie.

%prep
%setup -q

%build
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# useless (preloadable library)
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aoss
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/lib*.so
%{_mandir}/man1/aoss.1*
