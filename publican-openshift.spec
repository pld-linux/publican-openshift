Summary:	Publican documentation template files for OpenShift
Summary(pl.UTF-8):	Pliki szablonów dokumentacji Publicana dla projektu OpenShift
Name:		publican-openshift
Version:	0.13
Release:	1
License:	CC-BY-SA
Group:		Development/Tools
Source0:	https://fedorahosted.org/releases/p/u/publican/%{name}-%{version}.tgz
# Source0-md5:	2e43ee8da07fdee47fe9ddf31d833fdf
URL:		https://publican.fedorahosted.org/
BuildRequires:	publican >= 3.0
Requires:	publican >= 3.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides common files and templates needed to build
documentation for OpenShift with Publican.

%description -l pl.UTF-8
Ten pakiet udostępnia wspólne pliki oraz szablony wymagane do
budowania dokumentacji dla projektu OpenShift przy użyciu Publicana.

%prep
%setup -q

%build
publican build --formats=xml --langs=all --publish

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/publican/Common_Content

publican install_brand --path=$RPM_BUILD_ROOT%{_datadir}/publican/Common_Content

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README
%{_datadir}/publican/Common_Content/OpenShift
