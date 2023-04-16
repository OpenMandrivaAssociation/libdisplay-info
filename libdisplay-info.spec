%define major 1
%define libname %mklibname display-info
%define devname %mklibname display-info -d

Name: libdisplay-info
Version: 0.1.1
Release: 1
Source0: https://gitlab.freedesktop.org/emersion/libdisplay-info/-/archive/%{version}/libdisplay-info-%{version}.tar.bz2
Summary: EDID and DisplayID library
URL: https://emersion.pages.freedesktop.org/libdisplay-info/
License: MIT
Group: System/Libraries
BuildRequires: meson

%description
EDID and DisplayID library.

Goals:

* Provide a set of high-level, easy-to-use, opinionated functions as well
  as low-level functions to access detailed information.
* Simplicity and correctness over performance and resource usage.
* Well-tested and fuzzed.

%package -n %{libname}
Summary: EDID and DisplayID library
Group: System/Libraries

%description -n %{libname}
EDID and DisplayID library.

Goals:

* Provide a set of high-level, easy-to-use, opinionated functions as well
  as low-level functions to access detailed information.
* Simplicity and correctness over performance and resource usage.
* Well-tested and fuzzed.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1
%meson

%build
%meson_build

%install
%meson_install

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*.so.0*
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
