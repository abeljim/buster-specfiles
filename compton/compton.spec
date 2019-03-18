Name:		compton
Version:	0.1
Release:	2%{?dist}
Summary:	Compositor for X

License:	GPLv2
URL:		https://github.com/chjj/compton
Source0:	https://github.com/chjj/compton/archive/master.zip

BuildRequires:	gcc
BuildRequires:	libX11-devel libXcomposite-devel libXdamage-devel
BuildRequires:  libXfixes-devel libXext-devel libXrender-devel
BuildRequires:  libXrandr-devel libXinerama-devel
BuildRequires:  pcre-devel libconfig-devel libdrm-devel mesa-libGL-devel 
BuildRequires:  dbus-devel asciidoc

%description

%prep
%setup -n compton-master

%build
sed -i 's@CFLAGS ?= -DNDEBUG -O2 -D_FORTIFY_SOURCE=2@CFLAGS ?= %{optflags}@' Makefile
sed -i 's@CFLAGS += -Wall@@' Makefile
sed -i 's@LDFLAGS ?= -Wl,-O1 -Wl,--as-needed@LDFLAGS ?= %{__global_ldflags}@' Makefile

make %{?_smp_mflags}

%install
%make_install

%files
%{_bindir}/*
/usr/share/applications/*
/usr/share/icons/hicolor/48x48/apps/*
/usr/share/icons/hicolor/scalable/apps/*
%{_mandir}/man1/*
