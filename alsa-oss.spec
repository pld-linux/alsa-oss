Summary:	Advanced Linux Sound Architecture - OSS compatibility wrapper library & script
Summary(pl):	Advanced Linux Sound Architecture - biblioteka i skrypt kompatybilno¶ci z OSS
Name:		alsa-oss
Version:	1.0.12
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	ftp://ftp.alsa-project.org/pub/oss-lib/%{name}-%{version}.tar.bz2
# Source0-md5:	d4d18bbf63a866d6e065b90e16acd676
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
Ten pakiet zawiera bibliotekê kompatybilno¶ci ALSA -> OSS oraz prosty
wrapper który u³atwia jej u¿ycie, po prostu ustawiaj±c odpowiednie
LD_PRELOAD i uruchamiaj±c polecenie.

%package devel
Summary:	ossredir header file and static library
Summary(pl):	Plik nag³ówkowy i biblioteka statyczka ossredir
Group:		Development/Libraries
# doesn't require base on build time (only at runtime...)

%description devel
The purpose of this little piece of code is to redirect OSS (Open
Sound System) calls to any shared library to avoid overhead caused
with the LD_PRELOAD wrapper. Especially, wrapping select() and poll()
functions cause big overhead.

%description devel -l pl
Celem tego ma³ego kawa³ka kodu jest przekierowanie wywo³añ OSS (Open
Sound System) do dowolnej biblioteki dzielonej, aby zapobiec narzutowi
wywo³anemu przez wrapper LD_PRELOAD. Szczególnie przechwytywanie
select() i poll() powoduje du¿y narzut.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# useless (preloadable libraries)
rm -f $RPM_BUILD_ROOT%{_libdir}/lib{alsatoss,aoss}.{la,a}

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

%files devel
%defattr(644,root,root,755)
%doc oss-redir/README
%{_libdir}/libossredir.a
%{_libdir}/libossredir.la
%{_includedir}/oss-redir.h
