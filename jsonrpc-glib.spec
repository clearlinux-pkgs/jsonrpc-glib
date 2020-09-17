#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jsonrpc-glib
Version  : 3.38.0
Release  : 5
URL      : https://github.com/GNOME/jsonrpc-glib/archive/3.38.0/jsonrpc-glib-3.38.0.tar.gz
Source0  : https://github.com/GNOME/jsonrpc-glib/archive/3.38.0/jsonrpc-glib-3.38.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: jsonrpc-glib-data = %{version}-%{release}
Requires: jsonrpc-glib-lib = %{version}-%{release}
Requires: jsonrpc-glib-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : json-glib-dev
BuildRequires : pkgconfig(json-glib-1.0)

%description
# Jsonrpc-GLib
Jsonrpc-GLib is a library to communicate with JSON-RPC based peers in either a synchronous or asynchronous fashion.
It also allows communicating using the GVariant serialization format instead of JSON when both peers support it.
You might want that when communicating on a single host to avoid parser overhead and memory-allocator fragmentation.

%package data
Summary: data components for the jsonrpc-glib package.
Group: Data

%description data
data components for the jsonrpc-glib package.


%package dev
Summary: dev components for the jsonrpc-glib package.
Group: Development
Requires: jsonrpc-glib-lib = %{version}-%{release}
Requires: jsonrpc-glib-data = %{version}-%{release}
Provides: jsonrpc-glib-devel = %{version}-%{release}
Requires: jsonrpc-glib = %{version}-%{release}

%description dev
dev components for the jsonrpc-glib package.


%package lib
Summary: lib components for the jsonrpc-glib package.
Group: Libraries
Requires: jsonrpc-glib-data = %{version}-%{release}
Requires: jsonrpc-glib-license = %{version}-%{release}

%description lib
lib components for the jsonrpc-glib package.


%package license
Summary: license components for the jsonrpc-glib package.
Group: Default

%description license
license components for the jsonrpc-glib package.


%prep
%setup -q -n jsonrpc-glib-3.38.0
cd %{_builddir}/jsonrpc-glib-3.38.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600319678
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/jsonrpc-glib
cp %{_builddir}/jsonrpc-glib-3.38.0/COPYING %{buildroot}/usr/share/package-licenses/jsonrpc-glib/01a6b4bf79aca9b556822601186afab86e8c4fbf
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Jsonrpc-1.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/vala/vapi/jsonrpc-glib-1.0.deps
/usr/share/vala/vapi/jsonrpc-glib-1.0.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/jsonrpc-glib-1.0/jsonrpc-client.h
/usr/include/jsonrpc-glib-1.0/jsonrpc-glib.h
/usr/include/jsonrpc-glib-1.0/jsonrpc-input-stream-private.h
/usr/include/jsonrpc-glib-1.0/jsonrpc-input-stream.h
/usr/include/jsonrpc-glib-1.0/jsonrpc-message.h
/usr/include/jsonrpc-glib-1.0/jsonrpc-output-stream.h
/usr/include/jsonrpc-glib-1.0/jsonrpc-server.h
/usr/include/jsonrpc-glib-1.0/jsonrpc-version-macros.h
/usr/include/jsonrpc-glib-1.0/jsonrpc-version.h
/usr/lib64/libjsonrpc-glib-1.0.so
/usr/lib64/pkgconfig/jsonrpc-glib-1.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libjsonrpc-glib-1.0.so.1
/usr/lib64/libjsonrpc-glib-1.0.so.1.3800.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jsonrpc-glib/01a6b4bf79aca9b556822601186afab86e8c4fbf
