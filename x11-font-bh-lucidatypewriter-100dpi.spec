Name: x11-font-bh-lucidatypewriter-100dpi
Version: 1.0.3
Release: 13
Summary: Xorg X11 font bh-lucidatypewriter-100dpi
Group: Development/X11
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/font/font-bh-lucidatypewriter-100dpi-%{version}.tar.bz2
# See #38627 for licensing
License: MIT
BuildArch: noarch
BuildRequires: fontconfig
BuildRequires: x11-font-util >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-100dpi-fonts <= 6.9.0
Requires(post): mkfontdir
Requires(postun): mkfontdir
Requires(post): mkfontscale
Requires(postun): mkfontscale

%description
Xorg X11 font bh-lucidatypewriter-100dpi

%prep
%setup -q -n font-bh-lucidatypewriter-100dpi-%{version}

%build
%configure --with-fontdir=%_datadir/fonts/100dpi

%make

%install
%makeinstall_std
rm -f %{buildroot}%_datadir/fonts/100dpi/fonts.dir
rm -f %{buildroot}%_datadir/fonts/100dpi/fonts.scale

%post
mkfontscale %_datadir/fonts/100dpi
mkfontdir %_datadir/fonts/100dpi

%postun
mkfontscale %_datadir/fonts/100dpi
mkfontdir %_datadir/fonts/100dpi

%files
%doc COPYING
%_datadir/fonts/100dpi/lut*.pcf.gz
