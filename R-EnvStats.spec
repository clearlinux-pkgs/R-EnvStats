#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-EnvStats
Version  : 2.3.1
Release  : 12
URL      : https://cran.r-project.org/src/contrib/EnvStats_2.3.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/EnvStats_2.3.1.tar.gz
Summary  : Package for Environmental Statistics, Including US EPA Guidance
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : R-Hmisc
BuildRequires : R-ggplot2
BuildRequires : R-nortest
BuildRequires : clr-R-helpers

%description
focus on analyzing chemical concentrations and physical parameters, usually in 
  the context of mandated environmental monitoring.  Major environmental 
  statistical methods found in the literature and regulatory guidance documents, 
  with extensive help that explains what these methods do, how to use them, 
  and where to find them in the literature.  Numerous built-in data sets from 
  regulatory guidance documents and environmental statistics literature.  Includes

%prep
%setup -q -c -n EnvStats

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1531754972

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1531754972
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library EnvStats
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library EnvStats
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library EnvStats
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library EnvStats|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/EnvStats/CITATION
/usr/lib64/R/library/EnvStats/DESCRIPTION
/usr/lib64/R/library/EnvStats/INDEX
/usr/lib64/R/library/EnvStats/Meta/Rd.rds
/usr/lib64/R/library/EnvStats/Meta/data.rds
/usr/lib64/R/library/EnvStats/Meta/features.rds
/usr/lib64/R/library/EnvStats/Meta/hsearch.rds
/usr/lib64/R/library/EnvStats/Meta/links.rds
/usr/lib64/R/library/EnvStats/Meta/nsInfo.rds
/usr/lib64/R/library/EnvStats/Meta/package.rds
/usr/lib64/R/library/EnvStats/NAMESPACE
/usr/lib64/R/library/EnvStats/NEWS
/usr/lib64/R/library/EnvStats/R/EnvStats
/usr/lib64/R/library/EnvStats/R/EnvStats.rdb
/usr/lib64/R/library/EnvStats/R/EnvStats.rdx
/usr/lib64/R/library/EnvStats/data/Rdata.rdb
/usr/lib64/R/library/EnvStats/data/Rdata.rds
/usr/lib64/R/library/EnvStats/data/Rdata.rdx
/usr/lib64/R/library/EnvStats/doc/EnvStats-manual.pdf
/usr/lib64/R/library/EnvStats/help/AnIndex
/usr/lib64/R/library/EnvStats/help/EnvStats.rdb
/usr/lib64/R/library/EnvStats/help/EnvStats.rdx
/usr/lib64/R/library/EnvStats/help/aliases.rds
/usr/lib64/R/library/EnvStats/help/paths.rds
/usr/lib64/R/library/EnvStats/html/00Index.html
/usr/lib64/R/library/EnvStats/html/R.css
/usr/lib64/R/library/EnvStats/scripts/EPA.2009/Chapter06Examples.R
/usr/lib64/R/library/EnvStats/scripts/EPA.2009/Chapter07Examples.R
/usr/lib64/R/library/EnvStats/scripts/EPA.2009/Chapter09Examples.R
/usr/lib64/R/library/EnvStats/scripts/EPA.2009/Chapter10Examples.R
/usr/lib64/R/library/EnvStats/scripts/EPA.2009/Chapter11Examples.R
/usr/lib64/R/library/EnvStats/scripts/EPA.2009/Chapter12Examples.R
/usr/lib64/R/library/EnvStats/scripts/EPA.2009/Chapter13Examples.R
/usr/lib64/R/library/EnvStats/scripts/EPA.2009/Chapter14Examples.R
/usr/lib64/R/library/EnvStats/scripts/EPA.2009/Chapter15Examples.R
/usr/lib64/R/library/EnvStats/scripts/EPA.2009/Chapter16Examples.R
/usr/lib64/R/library/EnvStats/scripts/EPA.2009/Chapter17Examples.R
/usr/lib64/R/library/EnvStats/scripts/EPA.2009/Chapter18Examples.R
/usr/lib64/R/library/EnvStats/scripts/EPA.2009/Chapter19Examples.R
/usr/lib64/R/library/EnvStats/scripts/EPA.2009/Chapter20Examples.R
/usr/lib64/R/library/EnvStats/scripts/EPA.2009/Chapter21Examples.R
/usr/lib64/R/library/EnvStats/scripts/EPA.2009/Chapter22Examples.R
/usr/lib64/R/library/EnvStats/scripts/Manual/Chapter01.R
/usr/lib64/R/library/EnvStats/scripts/Manual/Chapter02.R
/usr/lib64/R/library/EnvStats/scripts/Manual/Chapter03.R
/usr/lib64/R/library/EnvStats/scripts/Manual/Chapter04.R
/usr/lib64/R/library/EnvStats/scripts/Manual/Chapter05.R
/usr/lib64/R/library/EnvStats/scripts/Manual/Chapter06.R
/usr/lib64/R/library/EnvStats/scripts/Manual/Chapter07.R
/usr/lib64/R/library/EnvStats/scripts/Manual/Chapter08.R
/usr/lib64/R/library/EnvStats/scripts/Manual/Chapter09.R
