Name: hunspell-fo
Summary: Faroese hunspell dictionaries
Version: 0.2.37
Release: 1.1%{?dist}
Source: http://fo.speling.org/filer/myspell-fo-%{version}.tar.bz2
Group: Applications/Text
URL: http://fo.speling.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+
BuildArch: noarch

Requires: hunspell

%description
Faroese hunspell dictionaries.

%prep
%setup -q -n myspell-fo-%{version}

%build
for i in Copyright contributors README; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README Copyright contributors COPYING
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.2.37-1.1
- Rebuilt for RHEL 6

* Fri Sep 04 2009 Caolan McNamara <caolanm@redhat.com> - 0.2.37-1
- latest version

* Mon Aug 10 2009 Caolan McNamara <caolanm@redhat.com> - 0.2.36-4
- .gz -> .bz2

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolan McNamara <caolanm@redhat.com> - 0.2.36-2
- tidy spec

* Tue May 19 2009 Caolan McNamara <caolanm@redhat.com> - 0.2.36-1
- latest version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 23 2008 Caolan McNamara <caolanm@redhat.com> - 0.2.35-1
- latest version

* Mon Sep 08 2008 Caolan McNamara <caolanm@redhat.com> - 0.2.34-1
- latest version

* Mon Jul 07 2008 Caolan McNamara <caolanm@redhat.com> - 0.2.33-1
- latest version

* Thu Mar 27 2008 Caolan McNamara <caolanm@redhat.com> - 0.2.32-1
- initial version
