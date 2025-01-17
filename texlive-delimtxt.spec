Name:		texlive-delimtxt
Version:	16549
Release:	2
Summary:	Read and parse text tables
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/exptl/delimtxt
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/delimtxt.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/delimtxt.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/delimtxt.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This experimental package can read and parse text tables
delimited by user-defined tokens (e.g., tab). It can be used
for serial letters and the like, making it easier to export the
data file from MS-Excel/MS-Word.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/delimtxt/delimtxt.sty
%doc %{_texmfdistdir}/doc/latex/delimtxt/delimtxt.pdf
%doc %{_texmfdistdir}/doc/latex/delimtxt/resulta.dat
%doc %{_texmfdistdir}/doc/latex/delimtxt/resultb.dat
%doc %{_texmfdistdir}/doc/latex/delimtxt/resultc.dat
%doc %{_texmfdistdir}/doc/latex/delimtxt/test1.tex
%doc %{_texmfdistdir}/doc/latex/delimtxt/test2.tex
%doc %{_texmfdistdir}/doc/latex/delimtxt/test3.tex
#- source
%doc %{_texmfdistdir}/source/latex/delimtxt/delimtxt.dtx
%doc %{_texmfdistdir}/source/latex/delimtxt/delimtxt.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
