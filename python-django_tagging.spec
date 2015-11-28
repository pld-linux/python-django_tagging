%define		module		tagging
Summary:	A generic tagging application for Django projects
Summary(pl.UTF-8):	Aplikacja do obsługi tagów w projektach Django.
Name:		python-django_tagging
Version:	0.3.1
Release:	2
License:	MIT
Group:		Development/Languages/Python
Source0:	https://django-tagging.googlecode.com/files/django-%{module}-%{version}.tar.gz
# Source0-md5:	a0855f2b044db15f3f8a025fa1016ddf
URL:		http://code.google.com/p/django-tagging/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-django >= 1.0
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A generic tagging application for Django projects, which allows
association of a number of tags with any Model instance and makes
retrieval of tags simple.

%prep
%setup -q -n django-%{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/tests

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%{py_sitescriptdir}/%{module}/templatetags
%{py_sitescriptdir}/django_tagging-%{version}-py*.egg-info
