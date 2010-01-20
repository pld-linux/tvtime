Summary:	A high quality TV viewer
Summary(pl.UTF-8):	Program do oglądania TV w wysokiej jakości
Name:		tvtime
Version:	1.0.2
Release:	4
License:	GPL
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/tvtime/%{name}-%{version}.tar.gz
# Source0-md5:	4b3d03afe61be239b08b5e522cd8afed
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-gcc.patch
Patch2:		%{name}-def_user.patch
Patch3:		%{name}-autodetect_textured_overlay.patch
URL:		http://tvtime.sourceforge.net/
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	zlib-devel
ExclusiveArch:	%{ix86} %{x8664}
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
używania z kartami przechwytującymi obraz. tvtime przetwarza
wejście z karty i wyświetla je na monitorze lub projektorze
komputerowym. W przeciwieństwie do innych aplikacji telewizyjnych
tvtime skupia się na wysokiej jakości obrazu, co czyni go idealnym
dla wideofili.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1

%build
cp -f /usr/share/automake/config.sub .
%configure \
	--disable-dependency-tracking
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* data/COPYING.* docs/html
%attr(755,root,root) %{_bindir}/tvtime
%attr(755,root,root) %{_bindir}/tvtime-command
%attr(755,root,root) %{_bindir}/tvtime-configure
%attr(755,root,root) %{_bindir}/tvtime-scanner
%dir %{_sysconfdir}/tvtime
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/tvtime/*.xml
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/tvtime.png
%{_pixmapsdir}/*
%{_datadir}/tvtime
%{_mandir}/man?/*
%lang(de) %{_mandir}/de/man?/*
%lang(es) %{_mandir}/es/man?/*
