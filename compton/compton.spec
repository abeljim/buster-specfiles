%global commit 316eac0613bf342ff91cc645a6c3c80e6b9083fb
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20170430

Name    : compton
Version : 0.1
Release : 0.1.%{gitdate}git%{shortcommit}%{?dist}
Summary : Compositor for X11
License : MIT
URL     : https://github.com/chjj/compton
Source0 : https://github.com/chjj/compton/tarball/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
BuildRequires : gcc
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xcomposite)
BuildRequires : pkgconfig(xfixes)
BuildRequires : pkgconfig(xdamage)
BuildRequires : pkgconfig(xrender)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xrandr)
BuildRequires : pkgconfig(xinerama)
BuildRequires : pkgconfig(libconfig) >= 1.4
BuildRequires : pcre-devel
BuildRequires : pkgconfig(libdrm)
BuildRequires : mesa-libGL-devel
BuildRequires : pkgconfig(dbus-1)
BuildRequires : asciidoc
BuildRequires : desktop-file-utils
Requires : xorg-x11-utils
Requires : hicolor-icon-theme

%description
Compton is a compositor for X, and a fork of xcompmgr-dana.

%prep
%autosetup -n chjj-%{name}-%{shortcommit}

%build
export COMPTON_VERSION=%{version}-%{gitdate}git%{shortcommit}
export CFLAGS="%{optflags} -DNDEBUG"
%make_build
%make_build docs

%install
%make_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/compton.desktop

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%{_bindir}/%{name}
%{_bindir}/%{name}-trans
%{_mandir}/man1/compton.1.gz
%{_mandir}/man1/compton-trans.1.gz
%{_datadir}/icons/hicolor/scalable/apps/compton.svg
%{_datadir}/icons/hicolor/48x48/apps/compton.png
%{_datadir}/applications/compton.desktop
%license LICENSE
%doc README.md compton.sample.conf

%changelog
* Fri Dec 15 2017 Dominik Schubert - 0.1-0.1.20170430git316eac0
- Initial packaging
