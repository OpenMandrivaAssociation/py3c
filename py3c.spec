Summary:	Library for helping port Python 2.x extensions to Python 3.x
Group:		System/Libraries
Name:		py3c
Version:	1.4
Release:	3
Url:		https://pypi.org/project/py3c/
# The official release package seems to be missing the headers
#Source0:	https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
Source0:	https://github.com/encukou/py3c/archive/%{name}-%{version}.tar.gz
License:	MIT
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	make

%description
Library for helping port Python 2.x extensions to Python 3.x

%prep
%autosetup -p1

%build
make prefix=%{_prefix}

%install
make install prefix=%{buildroot}%{_prefix}
#mkdir %{buildroot}/%{libdir}
mv  %{buildroot}/%{_datadir}/ %{buildroot}/%{_libdir}
#rm -
sed -i 's,%{buildroot},,' %{buildroot}/%{_libdir}/pkgconfig/py3c.pc

%files
%{_includedir}/py3c.h
%{_includedir}/py3c
%{_libdir}/pkgconfig/py3c.pc
