Summary:	Library for helping port Python 2.x extensions to Python 3.x
Group:		System/Libraries
Name:		py3c
Version:	1.1
Release:	1
Url:		https://pypi.org/project/py3c/
# The official release package seems to be missing the headers
#Source0:	https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
Source0:	https://github.com/encukou/py3c/archive/v%{version}.tar.gz
License:	MIT
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python3dist(setuptools)

%description
Library for helping port Python 2.x extensions to Python 3.x

%prep
%autosetup -p1

%build
python setup.py build

%install
python setup.py install --skip-build --root %{buildroot}

%files
%{python_sitelib}/*
%{_includedir}/python*/py3c
