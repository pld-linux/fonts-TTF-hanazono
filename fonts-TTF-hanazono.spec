Summary:	Free TrueType fonts for CJK ideograms
Summary(pl.UTF-8):	Wolnodostępne fonty TrueType dla ideogramów CJK
Name:		fonts-TTF-hanazono
Version:	20110915
Release:	1
License:	Freeware
Group:		Fonts
Source0:	http://kage.sourceforge.jp/hanazono/hanazono-%{version}.zip
# Source0-md5:	f2988a9ea2304e40cec02f220c658374
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
%{ttffontsdir}/*.ttf
