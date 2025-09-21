%define name countryfetch
%define version 0.2.0
%define release 2%{?dist}

Summary:  A Command-line tool similar to Neofetch for obtaining information about your country 
Name:     %{name}
Version:  %{version}
Release:  %{release}
License:  MIT License
URL:      https://github.com/nik-rev/countryfetch
Source0:  https://github.com/nik-rev/countryfetch/archive/refs/tags/v%{version}.tar.gz

%define debug_package %{nil}

BuildRequires: curl
BuildRequires: gcc
BuildRequires: make
BuildRequires: gzip
BuildRequires: upx
BuildRequires: perl
BuildRequires: perl-IPC-Cmd
BuildRequires: perl-FindBin

%description
Countryfetch is a neofetch-like tool for fetching information about your country.

%prep
%setup -q -n countryfetch-%{version}

%build
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
export PATH="$PATH:$HOME/.cargo/bin"
cargo build --release --locked
strip --strip-all target/release/%{name}
mkdir -p %{buildroot}/%{_bindir}

%install
mkdir -p %{buildroot}/%{_bindir}/
install -m 755 target/release/%{name} %{buildroot}/%{_bindir}/

%files
%doc README.md
%{_bindir}/%{name}
