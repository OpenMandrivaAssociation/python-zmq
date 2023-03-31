Summary:	Python bindings for zeromq
Name:		python-zmq
Version:	20.0.0
Release:	3
Group:		Development/Python
License:	GPLv2+
Url:		https://github.com/zeromq/pyzmq
Source0:	https://github.com/zeromq/pyzmq/archive/v%{version}/pyzmq-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(libzmq)
BuildRequires:	python-cython

%description
This package contains Python bindings for ØMQ. ØMQ is a lightweight and
fast messaging implementation.

PyZMQ should work with any reasonable version of Python (≥ 3.4), as well
as Python 2.7 and 3.3, as well as PyPy. The Cython backend used by CPython
supports libzmq ≥ 2.1.4 (including 3.2.x and 4.x), but the CFFI backend
used by PyPy only supports libzmq ≥ 3.2.2 (including 4.x).

%files
%{python_sitearch}/pyzmq-%{version}-py*.*.egg-info
%{python_sitearch}/zmq/

#------------------------------------------------------------
%prep
%autosetup -p1 -n pyzmq-%{version}

%build
%setup_compile_flags

export LDFLAGS="%{ldflags} -lpython3.11"

python setup.py \
	build

%install
python setup.py \
	install \
	--root="%{buildroot}" \
	--record="%{name}.list"

%check
python setup.py \
	check
