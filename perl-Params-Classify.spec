#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Params-Classify
Version  : 0.015
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Params-Classify-0.015.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Params-Classify-0.015.tar.gz
Summary  : 'argument type classification'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Params-Classify-lib = %{version}-%{release}
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
Requires: perl-Params-Classify-lib = %{version}-%{release}
Provides: perl-Params-Classify-devel = %{version}-%{release}

%description dev
dev components for the perl-Params-Classify package.


%package lib
Summary: lib components for the perl-Params-Classify package.
Group: Libraries

%description lib
lib components for the perl-Params-Classify package.


%prep
%setup -q -n Params-Classify-0.015

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
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
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/Params/Classify.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Params::Classify.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/auto/Params/Classify/Classify.so
