Summary:	Library to support cross-platform C locale functions
Summary(pl.UTF-8):	Biblioteka wspierająca wieloplatformowe funkcje obsługi lokalizacji w C
Name:		libclocale
Version:	20150101
Release:	2
License:	LGPL v3+
Group:		Libraries
Source0:	https://github.com/libyal/libclocale/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	da7b987fc9729d71fc6ce351106a7e7e
Patch0:		%{name}-system-libs.patch
URL:		https://github.com/libyal/libclocale/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	libcerror-devel >= 20120425
BuildRequires:	libcstring-devel >= 20120425
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	libcerror >= 20120425
Requires:	libcstring >= 20120425
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libclocale is a library to support cross-platform C locale functions.

%description -l pl.UTF-8
libclocale to biblioteka wspierająca wieloplatformowe funkcje obsługi
lokalizacji w C.

%package devel
Summary:	Header files for libclocale library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libclocale
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libcerror-devel >= 20120425
Requires:	libcstring-devel >= 20120425

%description devel
Header files for libclocale library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libclocale.

%package static
Summary:	Static libclocale library
Summary(pl.UTF-8):	Statyczna biblioteka libclocale
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libclocale library.

%description static -l pl.UTF-8
Statyczna biblioteka libclocale.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__sed} -i -e 's/ po\/Makefile.in//' configure.ac
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libclocale.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libclocale.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libclocale.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libclocale.so
%{_includedir}/libclocale
%{_includedir}/libclocale.h
%{_pkgconfigdir}/libclocale.pc
%{_mandir}/man3/libclocale.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libclocale.a
