Name:		texlive-uiucredborder
Version:	29974
Release:	2
Summary:	Class for UIUC thesis red-bordered forms
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/uiucredborder
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uiucredborder.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uiucredborder.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uiucredborder.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class offers a means of filling out the "red-bordered form"
that gets signed by the department head, your advisor, and --
for doctoral dissertations -- your thesis committee members.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/uiucredborder/uiucredborder.cls
%doc %{_texmfdistdir}/doc/latex/uiucredborder/uiucredborder.pdf
#- source
%doc %{_texmfdistdir}/source/latex/uiucredborder/uiucredborder.dtx
%doc %{_texmfdistdir}/source/latex/uiucredborder/uiucredborder.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
