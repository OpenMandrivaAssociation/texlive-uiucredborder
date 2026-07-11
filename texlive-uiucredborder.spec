%global tl_name uiucredborder
%global tl_revision 29974

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.00
Release:	%{tl_revision}.1
Summary:	Class for UIUC thesis red-bordered forms
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/uiucredborder
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uiucredborder.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uiucredborder.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uiucredborder.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class offers a means of filling out the "red-bordered form" that
gets signed by the department head, your advisor, and -- for doctoral
dissertations -- your thesis committee members.

