Summary:	Free TrueType fonts for CJK ideograms
Summary(pl.UTF-8):	Wolnodostępne fonty TrueType dla ideogramw CJK
Name:		fonts-TTF-hanazono
Version:	20091201
Release:	1
License:	Freeware
Group:		Fonts
Source0:	http://fonts.jp/hanazono/hanazono-%{version}.zip
# Source0-md5:	fb0be93d87c063e6a4c934d4fa8fc5cd
URL:		http://fonts.jp/hanazono/
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
This font is Kanji free font. This font includes 52,809 characters
defined at ISO/IEC 10646 standard / the Unicode standard.

#%%description -l pl.UTF-8
# TODO

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}

install *.ttf $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc *.txt
%{ttffontsdir}/hanazono.ttf