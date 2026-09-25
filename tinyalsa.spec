%global debug_package %{nil}
%global commit      f78ed25aced2dfea743867b8205a787bfb091340
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapdate    20230918

Name:           tinyalsa
Version:        2.0.0
Release:        2.qcom^%{snapdate}git%{shortcommit}%{?dist}
Summary:        Tiny ALSA library for interfacing with Linux kernel ALSA
License:        BSD-3-Clause
URL:            https://github.com/tinyalsa/tinyalsa
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.tar.gz

ExclusiveArch:  aarch64

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gcc

%description
TinyALSA is a small library to interface with ALSA in the Linux kernel.
It is a lightweight alternative to libasound, used by AudioReach
audio components on Qualcomm platforms.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development headers and pkg-config file for building applications
that use the TinyALSA library.

%prep
%autosetup -n %{name}-%{commit}

%build
%meson -Ddocs=disabled -Dexamples=disabled -Dc_args="-DTINYALSA_USES_PLUGINS -fPIE"
%meson_build

%install
%meson_install

%files
%license NOTICE
%{_libdir}/libtinyalsa.so.*
%{_bindir}/tinycap
%{_bindir}/tinymix
%{_bindir}/tinypcminfo
%{_bindir}/tinyplay
%{_mandir}/man1/tinycap.1*
%{_mandir}/man1/tinymix.1*
%{_mandir}/man1/tinypcminfo.1*
%{_mandir}/man1/tinyplay.1*

%files devel
%{_includedir}/tinyalsa/*.h
%{_libdir}/libtinyalsa.so
%{_libdir}/pkgconfig/tinyalsa.pc

%changelog
* Fri Sep 25 2026 Chiluka Rohith <rchiluka@qti.qualcomm.com> - 2.0.0-2.qcom^20230918gitf78ed25
- The v2.0.0 tag omits attributes.h/plugin.h from installed headers,
  which breaks downstream builds; this snapshot includes that fix

* Thu Sep 18 2026 Chiluka Rohith <rchiluka@qti.qualcomm.com> - 2.0.0-1.qcom
- Use proper upstream version 2.0.0 with qcom release suffix to dominate EPEL
- Drop Epoch, shortcommit and commitdate globals; keep commit hash for Source0

* Wed Sep 18 2023 Qualcomm Linux <quic_linux@quicinc.com> - 0^20230918gitf78ed25a-1
- Initial RPM packaging of tinyalsa for AudioReach components
