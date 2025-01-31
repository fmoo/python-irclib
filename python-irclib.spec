Summary: A set of Python modules for IRC support.
Name: python-irclib
Version: 0.5.0
Release: 1
Group: Development/Libraries
License: LGPL
URL: http://python-irclib.sourceforge.net
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Requires: python
BuildPrereq: python
BuildArch: noarch

%description
This library is intended to encapsulate the IRC protocol at a quite
low level.  It provides an event-driven IRC client framework.  It has
a fairly thorough support for the basic IRC protocol, CTCP and DCC
connections.

%prep
%setup -q
chmod 644 *

%build
python -c "import py_compile; py_compile.compile('irclib.py')"
python -c "import py_compile; py_compile.compile('ircbot.py')"

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT/usr/lib/python1.5/site-packages
%{__install} -m 644 irclib.py* $RPM_BUILD_ROOT/usr/lib/python1.5/site-packages
%{__install} -m 644 ircbot.py* $RPM_BUILD_ROOT/usr/lib/python1.5/site-packages

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README ChangeLog COPYING irccat irccat2 servermap testbot.py dccsend dccreceive
/usr/lib/python*/site-packages/*

%changelog
* Sat Sep 11 2008 Keltus <keltus@users.sourceforge.net> 0.4.8-1
- upgraded to 0.4.8

* Sat Aug 29 2008 Keltus <keltus@users.sourceforge.net> 0.4.7-1
- upgraded to 0.4.7

* Sat Dec 24 2005 Keltus <keltus@users.sourceforge.net> 0.4.6-1
- upgraded to 0.4.6

* Wed May 18 2005 Keltus <keltus@users.sourceforge.net> 0.4.5-1
- upgraded to 0.4.5

* Wed Feb 23 2005 Keltus <keltus@users.sourceforge.net> 0.4.4-1
- upgraded to 0.4.4

* Sun Jan 19 2005 Joel Rosdahl <joel@rosdahl.net> 0.4.3-1
- upgraded to 0.4.3

* Fri Jul  9 2004 Joel Rosdahl <joel@rosdahl.net> 0.4.2-1
- upgraded to 0.4.2

* Thu Oct 30 2003 Joel Rosdahl <joel@rosdahl.net> 0.4.1-1
- upgraded to 0.4.1

* Mon Sep  1 2002 Gary Benson <gary@inauspicious.org> 0.4.0-1
- upgraded to 0.4.0

* Wed Feb 20 2002 Gary Benson <gary@inauspicious.org> 0.3.4-1
- upgraded to 0.3.4

* Wed Feb 20 2002 Gary Benson <gary@inauspicious.org> 0.3.3-1
- initial revision
