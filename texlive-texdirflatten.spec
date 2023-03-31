Name:		texlive-texdirflatten
Epoch:		1
Version:	55064
Release:	2
Summary:	Collect files related to a LaTeX job in a single directory
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/texdirflatten
License:	ARTISTIC
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texdirflatten.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texdirflatten.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-texdirflatten.bin = %{EVRD}

%description
The Perl script parses a LaTeX file recursively, scanning all
child files, and collects details of any included and other
data files. These component files, are then all put into a
single directory (thus "flattening" the document's directory
tree).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/texdirflatten
%{_texmfdistdir}/scripts/texdirflatten
%doc %{_mandir}/man1/texdirflatten.1*
%doc %{_texmfdistdir}/doc/man/man1/texdirflatten.man1.pdf
%doc %{_texmfdistdir}/doc/support/texdirflatten

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/texdirflatten/texdirflatten texdirflatten
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
