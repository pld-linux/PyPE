# TODO: better way to start program
Summary:	Python Programmers' Editor
Summary(pl.UTF-8):	Edytor dla programistów Pythona
Name:		PyPE
Version:	2.9.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Editors
Source0:	http://dl.sourceforge.net/project/pype/pype/PyPE%202.9/%{name}-%{version}-src.zip
# Source0-md5:	dbd964244cb89b8e15944e78be2e0d65
URL:		http://netactview.sourceforge.net
Requires:	python
Requires:	python-wxPython
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python-oriented editor with support for multiple platforms.

%description -l pl.UTF-8
Edytor ukierunkowany na Pythona ze wsparciem dla wielu platform.

%clean
rm -rf $RPM_BUILD_ROOT

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/macros/samples}
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name}/icons,%{_datadir}/%{name}/plugins}

install {*.py,*.pyw,*.cfg,sample_alphabet.txt,sample_dictionary.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}
install macros/samples/*  $RPM_BUILD_ROOT%{_datadir}/%{name}/macros/samples/
install plugins/* $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/
install icons/* $RPM_BUILD_ROOT%{_datadir}/%{name}/icons/

#TODO - better way to start program
echo '#!/bin/sh' > $RPM_BUILD_ROOT%{_bindir}/pype
echo 'exec python /usr/share/PyPE/pype.py "$@"' >> $RPM_BUILD_ROOT%{_bindir}/pype

%files
%defattr(644,root,root,755)
%doc changelog.txt gpl.txt MANIFEST.in readme.html readme.txt
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.py
%{_datadir}/%{name}/*.pyw
%{_datadir}/%{name}/*.txt
%{_datadir}/%{name}/*.cfg
%{_datadir}/%{name}/plugins
%{_datadir}/%{name}/macros
%{_datadir}/%{name}/icons
