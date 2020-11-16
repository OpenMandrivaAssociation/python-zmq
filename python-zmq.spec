Summary:	Python bindings for zeromq
Name:		python-zmq
Version:	20.0.0
Release:	1
Group:		Development/Python
License:	GPLv2+
Url:		https://github.com/zeromq/pyzmq
Source0:	https://github.com/zeromq/pyzmq/archive/v%{version}/pyzmq-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(libzmq)
BuildRequires:	python-cython

%description
This package contains Python bindings for ØMQ. ØMQ is a lightweight and
fast messaging implementation.

PyZMQ should work with any reasonable version of Python (≥ 3.4), as well
as Python 2.7 and 3.3, as well as PyPy. The Cython backend used by CPython
supports libzmq ≥ 2.1.4 (including 3.2.x and 4.x), but the CFFI backend
used by PyPy only supports libzmq ≥ 3.2.2 (including 4.x).

%files -f %{name}.list
%{py_platsitedir}/zmq/__pycache__
#{py_platsitedir}/zmq/asyncio/__pycache__
#{py_platsitedir}/zmq/auth/__pycache__
%{py_platsitedir}/zmq/auth/asyncio/__pycache__
%{py_platsitedir}/zmq/backend/__pycache__
%{py_platsitedir}/zmq/backend/cffi/__pycache__
%{py_platsitedir}/zmq/backend/cython/__pycache__
%{py_platsitedir}/zmq/devices/__pycache__
%{py_platsitedir}/zmq/eventloop/__pycache__
%{py_platsitedir}/zmq/eventloop/minitornado/__pycache__
%{py_platsitedir}/zmq/eventloop/minitornado/platform/__pycache__
%{py_platsitedir}/zmq/green/__pycache__
%{py_platsitedir}/zmq/green/eventloop/__pycache__
%{py_platsitedir}/zmq/log/__pycache__
%{py_platsitedir}/zmq/ssh/__pycache__
%{py_platsitedir}/zmq/sugar/__pycache__
#{py_platsitedir}/zmq/tests/__pycache__
%{py_platsitedir}/zmq/tests/asyncio/__pycache__
%{py_platsitedir}/zmq/utils/__pycache__

#------------------------------------------------------------
%prep
%autosetup -p1 -n pyzmq-%{version}

%build
%setup_compile_flags

export LDFLAGS="%{ldflags} -lpython3.9"

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
