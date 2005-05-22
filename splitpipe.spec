# TODO: optflags
Summary:	Split streams into volumes
Summary(pl):	Dzielenie strumieni na wolumeny
Name:		splitpipe
Version:	0.4
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://ds9a.nl/splitpipe/%{name}-%{version}.tar.gz
# Source0-md5:	2ac1358055af126d1c6bf8ccd51ac784
Patch0:		%{name}-ncurses.patch
URL:		http://ds9a.nl/splitpipe/
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Splitpipe is a program that allows the output of a program to span
multiple volumes. Volumes might be DVD's, CD's, files, entire hard
disks or floppies.

%description -l pl
Splitpipe to program pozwalaj±cy na podzia³ wyj¶cia programu na wiele
wolumenów. Wolumeny mog± byæ p³ytami DVD, p³ytami CD, plikami, ca³ymi
dyskami twardymi lub dyskietkami.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
