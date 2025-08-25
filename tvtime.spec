# TODO:
# - figure out why configure scripts checks for wrong gcc path (while priting another) and drop CC/CXX forcing in the spec
Summary:	A high quality TV viewer
Summary(pl.UTF-8):	Program do oglądania TV w wysokiej jakości
Name:		tvtime
Version:	1.0.11
Release:	3
License:	GPL v2+
Group:		Applications/Multimedia
Source0:	https://linuxtv.org/downloads/tvtime/%{name}-%{version}.tar.gz
# Source0-md5:	f4adba831376a8baad92dbda49056138
Patch0:		%{name}-opt.patch
Patch1:		%{name}-autodetect_textured_overlay.patch
Patch2:		%{name}-x32.patch
Patch3:		build.patch
URL:		http://tvtime.sourceforge.net/
BuildRequires:	alsa-lib-devel >= 1.0.9
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6
BuildRequires:	freetype-devel >= 2
BuildRequires:	gcc >= 5:3.2
BuildRequires:	gettext-tools
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	zlib-devel
Requires:	alsa-lib >= 1.0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fomit-frame-pointer

%description
tvtime is a high quality television application for use with video
capture cards. tvtime processes the input from a capture card and
displays it on a computer monitor or projector. Unlike other
television applications, tvtime focuses on high visual quality making
it ideal for videophiles.

%description -l pl.UTF-8
tvtime to aplikacja do wysokiej jakości telewizji przeznaczona do
używania z kartami przechwytującymi obraz. tvtime przetwarza wejście z
karty i wyświetla je na monitorze lub projektorze komputerowym. W
przeciwieństwie do innych aplikacji telewizyjnych tvtime skupia się na
wysokiej jakości obrazu, co czyni go idealnym dla wideofili.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	CC=gcc \
	CXX=g++ \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README data/COPYING.* docs/html
%attr(755,root,root) %{_bindir}/tvtime
%attr(755,root,root) %{_bindir}/tvtime-command
%attr(755,root,root) %{_bindir}/tvtime-configure
%attr(755,root,root) %{_bindir}/tvtime-scanner
%dir %{_sysconfdir}/tvtime
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/tvtime/tvtime.xml
%{_datadir}/appdata/tvtime.appdata.xml
%{_desktopdir}/tvtime.desktop
%{_iconsdir}/hicolor/*x*/apps/tvtime.png
%{_datadir}/tvtime
%{_mandir}/man1/tvtime.1*
%{_mandir}/man1/tvtime-command.1*
%{_mandir}/man1/tvtime-configure.1*
%{_mandir}/man1/tvtime-scanner.1*
%{_mandir}/man5/stationlist.xml.5*
%{_mandir}/man5/tvtime.xml.5*
%lang(de) %{_mandir}/de/man1/tvtime.1*
%lang(de) %{_mandir}/de/man1/tvtime-command.1*
%lang(de) %{_mandir}/de/man1/tvtime-configure.1*
%lang(de) %{_mandir}/de/man1/tvtime-scanner.1*
%lang(de) %{_mandir}/de/man5/stationlist.xml.5*
%lang(de) %{_mandir}/de/man5/tvtime.xml.5*
%lang(es) %{_mandir}/es/man1/tvtime.1*
%lang(es) %{_mandir}/es/man1/tvtime-command.1*
%lang(es) %{_mandir}/es/man1/tvtime-configure.1*
%lang(es) %{_mandir}/es/man1/tvtime-scanner.1*
%lang(es) %{_mandir}/es/man5/stationlist.xml.5*
%lang(es) %{_mandir}/es/man5/tvtime.xml.5*
