Summary:	A high quality TV viewer
Summary(pl):	Program do ogl±dania TV w wysokiej jako¶ci
Name:		tvtime
Version:	0.9.15
Release:	2
License:	GPL
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/tvtime/%{name}-%{version}.tar.gz
# Source0-md5:	bf1b1547e8979cb6486584684e315847
Patch0:		%{name}-videoinput.patch
URL:		http://tvtime.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	libpng-devel
BuildRequires:	libxml2-devel
BuildRequires:	rpmbuild(macros) >= 1.121
BuildRequires:	zlib-devel
ExclusiveArch:	%{ix86} amd64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fomit-frame-pointer

%description
tvtime is a high quality television application for use with video
capture cards. tvtime processes the input from a capture card and
displays it on a computer monitor or projector. Unlike other
television applications, tvtime focuses on high visual quality making
it ideal for videophiles.

%description -l pl
tvtime to aplikacja do wysokiej jako¶ci telewizji przeznaczona do
u¿ywania z kartami przechwytuj±cymi obraz. tvtime przetwarza wej¶cie z
karty i wy¶wietla je na monitorze lub projektorze komputerowym. W
przeciwieñstwie do innych aplikacji telewizyjnych tvtime skupia siê na
wysokiej jako¶ci obrazu, co czyni go idealnym dla wideofili.

%prep
%setup -q
%patch0 -p1

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
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/tvtime/*.xml
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/tvtime.png
%{_pixmapsdir}/*
%{_datadir}/tvtime
%{_mandir}/man?/*
%lang(de) %{_mandir}/de/man?/*
