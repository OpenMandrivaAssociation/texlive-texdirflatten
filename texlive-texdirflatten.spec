%global tl_name texdirflatten
%global tl_revision 55064

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Collect files related to a LaTeX job in a single directory
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/texdirflatten
License:	artistic
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texdirflatten.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texdirflatten.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(texdirflatten.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The Perl script parses a LaTeX file recursively, scanning all child
files, and collects details of any included and other data files. These
component files, are then all put into a single directory (thus
"flattening" the document's directory tree).

