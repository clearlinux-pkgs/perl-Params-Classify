#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Params-Classify
Version  : 0.015
Release  : 23
URL      : https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Params-Classify-0.015.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Params-Classify-0.015.tar.gz
Summary  : 'argument type classification'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Params-Classify-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Params::Classify - argument type classification
DESCRIPTION
This module provides various type-testing functions.  These are intended
for functions that, unlike most Perl code, care what type of data they
are operating on.  For example, some functions wish to behave differently
depending on the type of their arguments (like overloaded functions
in C++).

%package dev
Summary: dev components for the perl-Params-Classify package.
Group: Development
Provides: perl-Params-Classify-devel = %{version}-%{release}
Requires: perl-Params-Classify = %{version}-%{release}

%description dev
dev components for the perl-Params-Classify package.


%package perl
Summary: perl components for the perl-Params-Classify package.
Group: Default
Requires: perl-Params-Classify = %{version}-%{release}

%description perl
perl components for the perl-Params-Classify package.


%prep
%setup -q -n Params-Classify-0.015
cd %{_builddir}/Params-Classify-0.015

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Params::Classify.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
