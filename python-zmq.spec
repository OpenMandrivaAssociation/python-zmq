%global debug_package %{nil}
%define module pyzmq

Name:		python-zmq
Summary:	Python bindings for zeromq
Version:	27.1.0
Release:	1
Group:		Development/Python
License:	BSD-3-Clause
URL:		https://github.com/zeromq/pyzmq
Source0:	https://github.com/zeromq/pyzmq/archive/v%{version}/%{module}-%{version}.tar.gz
BuildSystem:	python

BuildRequires:	clang
BuildRequires:	cmake
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(libzmq)
BuildRequires:	python%{pyver}dist(cffi)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(packaging)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(scikit-build-core)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
This package contains Python bindings for ØMQ. ØMQ is a lightweight and
fast messaging implementation.

PyZMQ should work with any reasonable version of Python (≥ 3.4), as well
as Python 2.7 and 3.3, as well as PyPy. The Cython backend used by CPython
supports libzmq ≥ 2.1.4 (including 3.2.x and 4.x), but the CFFI backend
used by PyPy only supports libzmq ≥ 3.2.2 (including 4.x).

%package devel
Summary:	Development files for %{name}
Group:		Development/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-devel
Requires:	zeromq-devel

%description devel
Development libraries and headers needed to build software using %{name}.

%prep
%autosetup -n pyzmq-%{version} -p1

# Fix non-executable script rpmlint warning:
find examples zmq -name "*.py" -exec sed -i "s|#\!\/usr\/bin\/env python||" {} \;
find . -name ".gitignore" -exec rm {} \;
chmod -x examples/pubsub/topics_pub.py examples/pubsub/topics_sub.py

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{ldflags} -lpython%{pyver}"
%py_build

%install
%py_install

%files
%doc README.md examples
%license LICENSE.md
%{python_sitearch}/zmq/
%{python_sitearch}/%{module}-%{version}.dist-info
%exclude %{python_sitearch}/zmq/utils/*.h
%exclude %{python_sitearch}/zmq/backend/cffi/*.c
%exclude %{python_sitearch}/zmq/backend/cffi/_cdefs.h

%files devel
%{python_sitearch}/zmq/utils/*.h
%{python_sitearch}/zmq/backend/cffi/*.c
%{python_sitearch}/zmq/backend/cffi/_cdefs.h
