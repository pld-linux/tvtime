Summary:	A high quality TV viewer.
Name:		tvtime
Version:	0.9.12
Release:	1
License:	GPL
Group:		Applications/Multimedia
URL:		http://tvtime.sourceforge.net/
Source0:	http://dl.sourceforge.net/tvtime/%{name}-%{version}.tar.gz
# Source0-md5:	
BuildRequires:	freetype-devel
BuildRequires:	zlib-devel
BuildRequires:	libpng-devel
BuildRequires:	XFree86-devel
BuildRequires:	SDL-devel
BuildRequires:	libxml2-devel
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tvtime is a high quality television application for use with video
capture cards. tvtime processes the input from a capture card and
displays it on a computer monitor or projector. Unlike other
television applications, tvtime focuses on high visual quality making
it ideal for videophiles.

%prep
%setup -q

%build
%configure \
	--disable-dependency-tracking
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
%doc AUTHORS ChangeLog COPYING NEWS README* data/COPYING* docs/html/
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/tvtime/
%attr(755,root,root) %{_bindir}/tvtime-command
%attr(755,root,root) %{_bindir}/tvtime-configure
%attr(755,root,root) %{_bindir}/tvtime-scanner
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/tvtime.png
%{_datadir}/pixmaps/*
%{_datadir}/tvtime/
%defattr(4775, root, root, 0755)
%attr(755,root,root) %{_bindir}/tvtime
