# IUS spec file for uwsgi-plugin-python35u
#
# This package is intended to work with uwsgi from EPEL and python35u from IUS.
# It should remain at the same version as the EPEL uwsgi package to ensure
# compatibility.

%global python python35u

Name: uwsgi-plugin-%{python}
Version: 2.0.16
Release: 1.ius%{?dist}
Summary: uWSGI - Plugin for Python support
Group: System Environment/Daemons
License: GPLv2 with exceptions
URL: https://github.com/unbit/uwsgi
BuildRequires: uwsgi-devel = %{version}
BuildRequires: %{python}-devel
BuildRequires: libuuid-devel
BuildRequires: pcre-devel
BuildRequires: openssl-devel
BuildRequires: libcap-devel
Requires: uwsgi-plugin-common = %{version}
Requires: %{python}

%{?filter_provides_in: %filter_provides_in %{_libdir}/uwsgi/.*\.so$}
%{?filter_setup}


%description
This package contains the python plugin for uWSGI.  Designed to work with the
uwsgi packages in EPEL, but built against %{python} from IUS.


%prep
%setup -q -c -T
cp -a %{_usrsrc}/uwsgi/%{version}/plugins/python .


%build
export CFLAGS="%{optflags} -Wno-unused-but-set-variable"
export PYTHON=%{__python35u}
uwsgi --build-plugin "python %{python}"


%install
install -D -p -m 0755 %{python}_plugin.so %{buildroot}%{_libdir}/uwsgi/%{python}_plugin.so


%files
%{_libdir}/uwsgi/%{python}_plugin.so


%changelog
* Thu Feb 22 2018 Jessica Widener <jessica.widener@rackspace.com> - 2.0.16-1.ius
- Rebuild against uwsgi 2.0.16

* Tue May 23 2017 Ben Harper <ben.harper@rackspace.com> - 2.0.15-1.ius
- Rebuild against uwsgi 2.0.15

* Wed Oct 12 2016 Carl George <carl.george@rackspace.com> - 2.0.14-1.ius
- Rebuild against uwsgi 2.0.14

* Thu Sep 01 2016 Carl George <carl.george@rackspace.com> - 2.0.13.1-1.ius
- Initial package
