%define		module		tagging
Summary:	A generic tagging application for Django projects.
Summary(pl.UTF-8):	Aplikacja do obsługi tagów w projektach Django.
Name:		python-django_tagging
Version:	0.2.1
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	http://django-tagging.googlecode.com/files/%{module}-%{version}.zip
# Source0-md5:	478817d8e3f8d062b54b8d9cdaaa00cd
URL:		http://code.google.com/p/django-tagging/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	unzip
#%pyrequires_eq	python-libs
%pyrequires_eq	python-modules
Requires:	python-django >= 1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -n %{module}-%{version}

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/tagging-%{version}-*.egg-info
