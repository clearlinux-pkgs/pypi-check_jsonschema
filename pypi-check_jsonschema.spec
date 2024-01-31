#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
# autospec version: v3
# autospec commit: fae1327
#
Name     : pypi-check_jsonschema
Version  : 0.27.4
Release  : 21
URL      : https://files.pythonhosted.org/packages/f9/a8/469129f40d8c8010183dab1e187d516eeaa428d58ca93128d7c250f33b90/check-jsonschema-0.27.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/f9/a8/469129f40d8c8010183dab1e187d516eeaa428d58ca93128d7c250f33b90/check-jsonschema-0.27.4.tar.gz
Summary  : A jsonschema CLI and pre-commit hook
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: pypi-check_jsonschema-bin = %{version}-%{release}
Requires: pypi-check_jsonschema-license = %{version}-%{release}
Requires: pypi-check_jsonschema-python = %{version}-%{release}
Requires: pypi-check_jsonschema-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(click)
BuildRequires : pypi(jsonschema)
BuildRequires : pypi(py)
BuildRequires : pypi(regress)
BuildRequires : pypi(requests)
BuildRequires : pypi(ruamel.yaml)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![pypi version](https://img.shields.io/pypi/v/check-jsonschema.svg)](https://pypi.org/project/check-jsonschema/)
[![supported pythons](https://img.shields.io/pypi/pyversions/check-jsonschema.svg)](https://pypi.org/project/check-jsonschema/)
[![build](https://github.com/python-jsonschema/check-jsonschema/actions/workflows/build.yaml/badge.svg)](https://github.com/python-jsonschema/check-jsonschema/actions/workflows/build.yaml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/python-jsonschema/check-jsonschema/main.svg)](https://results.pre-commit.ci/latest/github/python-jsonschema/check-jsonschema/main)
[![readthedocs documentation](https://readthedocs.org/projects/check-jsonschema/badge/?version=stable&style=flat)](https://check-jsonschema.readthedocs.io/en/stable)

%package bin
Summary: bin components for the pypi-check_jsonschema package.
Group: Binaries
Requires: pypi-check_jsonschema-license = %{version}-%{release}

%description bin
bin components for the pypi-check_jsonschema package.


%package license
Summary: license components for the pypi-check_jsonschema package.
Group: Default

%description license
license components for the pypi-check_jsonschema package.


%package python
Summary: python components for the pypi-check_jsonschema package.
Group: Default
Requires: pypi-check_jsonschema-python3 = %{version}-%{release}

%description python
python components for the pypi-check_jsonschema package.


%package python3
Summary: python3 components for the pypi-check_jsonschema package.
Group: Default
Requires: python3-core
Provides: pypi(check_jsonschema)
Requires: pypi(click)
Requires: pypi(jsonschema)
Requires: pypi(regress)
Requires: pypi(requests)
Requires: pypi(ruamel.yaml)

%description python3
python3 components for the pypi-check_jsonschema package.


%prep
%setup -q -n check-jsonschema-0.27.4
cd %{_builddir}/check-jsonschema-0.27.4
pushd ..
cp -a check-jsonschema-0.27.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1706718337
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . ruamel-yaml
pypi-dep-fix.py . ruamel.yaml
python3 setup.py build

pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
pypi-dep-fix.py . ruamel-yaml
pypi-dep-fix.py . ruamel.yaml
python3 setup.py build

popd
%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-check_jsonschema
cp %{_builddir}/check-jsonschema-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-check_jsonschema/24005878468a9906f3f1e94a33a0b85679bcf2fe || :
cp %{_builddir}/check-jsonschema-%{version}/src/check_jsonschema/builtin_schemas/vendor/LICENSE.azure-pipelines %{buildroot}/usr/share/package-licenses/pypi-check_jsonschema/03e1fe6fd0bc6d73c3cd3370d5f0a73c4fcb60d6 || :
cp %{_builddir}/check-jsonschema-%{version}/src/check_jsonschema/builtin_schemas/vendor/LICENSE.bitbucket-pipelines %{buildroot}/usr/share/package-licenses/pypi-check_jsonschema/2c6c10e45965bfdb418679514d000a3412dd984c || :
cp %{_builddir}/check-jsonschema-%{version}/src/check_jsonschema/builtin_schemas/vendor/LICENSE.buildkite %{buildroot}/usr/share/package-licenses/pypi-check_jsonschema/3fe44e366d6da1a816d9198bd496389b9d895781 || :
cp %{_builddir}/check-jsonschema-%{version}/src/check_jsonschema/builtin_schemas/vendor/LICENSE.gitlab %{buildroot}/usr/share/package-licenses/pypi-check_jsonschema/8f6011197d56095a01b8fd90f93c75ad1eb171b7 || :
cp %{_builddir}/check-jsonschema-%{version}/src/check_jsonschema/builtin_schemas/vendor/LICENSE.readthedocs %{buildroot}/usr/share/package-licenses/pypi-check_jsonschema/e25ae60dff530c1ed4ca76836a4fb41b7e680274 || :
cp %{_builddir}/check-jsonschema-%{version}/src/check_jsonschema/builtin_schemas/vendor/LICENSE.schemastore %{buildroot}/usr/share/package-licenses/pypi-check_jsonschema/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
python3 -tt setup.py build  install --root=%{buildroot}
pypi-dep-fix.py %{buildroot} ruamel-yaml
pypi-dep-fix.py %{buildroot} ruamel.yaml
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/check-jsonschema

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-check_jsonschema/03e1fe6fd0bc6d73c3cd3370d5f0a73c4fcb60d6
/usr/share/package-licenses/pypi-check_jsonschema/24005878468a9906f3f1e94a33a0b85679bcf2fe
/usr/share/package-licenses/pypi-check_jsonschema/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/pypi-check_jsonschema/2c6c10e45965bfdb418679514d000a3412dd984c
/usr/share/package-licenses/pypi-check_jsonschema/3fe44e366d6da1a816d9198bd496389b9d895781
/usr/share/package-licenses/pypi-check_jsonschema/8f6011197d56095a01b8fd90f93c75ad1eb171b7
/usr/share/package-licenses/pypi-check_jsonschema/e25ae60dff530c1ed4ca76836a4fb41b7e680274

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
