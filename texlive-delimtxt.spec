# revision 16549
# category Package
# catalog-ctan /macros/latex/exptl/delimtxt
# catalog-date 2008-08-18 10:38:42 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-delimtxt
Version:	20180303
Release:	2
Summary:	Read and parse text tables
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/exptl/delimtxt
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/delimtxt.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/delimtxt.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/delimtxt.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080818-2
+ Revision: 750885
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080818-1
+ Revision: 718215
- texlive-delimtxt
- texlive-delimtxt
- texlive-delimtxt
- texlive-delimtxt

