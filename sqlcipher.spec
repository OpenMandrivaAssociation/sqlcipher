%define	major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

%define _disable_lto 1

#global optflags %{optflags} --rtlib=compiler-rt

Summary:	An SQLite extension that provides 256 bit AES encryption of database files
Name:		sqlcipher
Version:	4.2.0
Release:	1
License:	BSD-style
Group:		System/Libraries
URL:		https://www.zetetic.net/sqlcipher/
Source0:	https://github.com/sqlcipher/sqlcipher/archive/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(readline)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	tcl

%description
SQLCipher is an SQLite extension that provides transparent 256-bit AES
encryption of database files. Pages are encrypted before being written to
disk and are decrypted when read back. Due to the small footprint and great
performance it’s ideal for protecting embedded application databases and
is well suited for mobile development.

%package -n	%{libname}
Summary:	An SQLite extension that provides 256 bit AES encryption of database files
Group:		System/Libraries

%description -n	%{libname}
SQLCipher is an SQLite extension that provides transparent 256-bit AES
encryption of database files. Pages are encrypted before being written to
disk and are decrypted when read back. Due to the small footprint and great
performance it’s ideal for protecting embedded application databases and
is well suited for mobile development.

This package contains the shared libraries for %{name}

%package -n	%{develname}
Summary:	Development library and header files for the %{name} library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
SQLCipher is an SQLite extension that provides transparent 256-bit AES
encryption of database files. Pages are encrypted before being written to
disk and are decrypted when read back. Due to the small footprint and great
performance it’s ideal for protecting embedded application databases and
is well suited for mobile development.

This package contains the static %{libname} library and its header
files.

%prep
%setup -qn %{name}-%{version}

%build
export CC=gcc
export CXX=g++
export CFLAGS="%optflags -DSQLITE_HAS_CODEC"
%configure --disable-static --disable-tcl --enable-tempstore=yes
%make_build

%install
%make_install

rm -f %{buildroot}%{_libdir}/*.la

%files
%{_bindir}/%{name}

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}
%{_libdir}/lib%{name}.so.%{major}.*

%files -n %{develname}
%doc CHANGELOG.md README.md LICENSE
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

