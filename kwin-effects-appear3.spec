Name:           kwin-effects-appear3
Version:        1.3
Release:        1%{?dist}
Summary:        Effect that animates the appearing of windows

License:        GPLv3+
URL:            https://github.com/zzag/kwin-effects-appear3

Source0:        https://github.com/zzag/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Base
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules

# Qt
BuildRequires:  qt5-qtbase-devel

# KF
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kwindowsystem-devel

# KWin
BuildRequires:  kwin-devel
Requires:       kwin-libs

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
%make_install -C %{_target_platform}

%files
%license LICENSE
%{_kf5_qtplugindir}/kwin/effects/plugins/libkwin4_effect_appear3.so

%changelog
* Mon May 14 2018 Vlad Zagorodniy <vladzzag@gmail.com> - 1.3-1
- New upstream release

* Sat May 05 2018 Vlad Zagorodniy <vladzzag@gmail.com> - 1.2-1
- Update to upstream

* Fri May 04 2018 Vlad Zagorodniy <vladzzag@gmail.com> - 1.1-1
- Initial commit

