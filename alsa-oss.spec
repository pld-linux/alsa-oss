Summary:	Advanced Linux Sound Architecture (ALSA) OSS compatibility wrapper library & script
Summary(pl):	Advanced Linux Sound Architecture (ALSA) - biblioteka i skrypt  kompatibilno¶ci z OSS
Name:		alsa-oss
%define		_pre	rc2
Version:	1.0.0
Release:	0.%{_pre}.2
License:	GPL
Group:		Applications/Sound
Source0:	ftp://ftp.alsa-project.org/pub/oss-lib/%{name}-%{version}%{_pre}.tar.bz2
# Source0-md5:	50cc9bd5c36149aacd0ca2d0bcb55d0b
URL:		http://www.alsa-project.org/
BuildRequires:	alsa-lib-devel >= 1.0.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OSS compatibility library and simple wrapper script which facilitates
it's use. It just sets the appropriate LD_PRELOAD path and then runs
the command.


%description -l pl
Bibliteka kompatybilno¶ci z OSS i prosty wrapper który u³atwia jej
u¿ycie, który po prostu ustawia odpowiednie LD_PRELOAD po czym
uruchamia komendê.



%prep
%setup -q -n %{name}-%{version}%{_pre}
%configure

%build

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aoss

%{_mandir}/man1/aoss.1*
%{_libdir}/*.la
%{_libdir}/*.so.*
