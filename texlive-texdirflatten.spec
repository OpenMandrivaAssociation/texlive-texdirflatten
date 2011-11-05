# revision 18835
# category Package
# catalog-ctan /support/texdirflatten
# catalog-date 2009-04-22 09:01:36 +0200
# catalog-license artistic
# catalog-version undef
Name:		texlive-texdirflatten
Version:	20090422
Release:	1
Summary:	Collect files related to a LaTeX job in a single directory
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/texdirflatten
License:	ARTISTIC
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texdirflatten.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texdirflatten.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-texdirflatten.bin = %{EVRD}
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The Perl script parses a LaTeX file recursively, scanning all
child files, and collects details of any included and other
data files. These component files, are then all put into a
single directory (thus "flattening" the document's directory
tree).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/texdirflatten
%{_texmfdistdir}/scripts/texdirflatten/texdirflatten
%doc %{_mandir}/man1/texdirflatten.1*
%doc %{_texmfdir}/doc/man/man1/texdirflatten.man1.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/texdirflatten/texdirflatten texdirflatten
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
