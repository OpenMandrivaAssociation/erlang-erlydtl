%global debug_package %{nil}
%global git_short_hash 6a9845f
%global short_name erlydtl
%global github_username evanmiller


Name:           erlang-%{short_name}
Version:        0.7.0
Release:        5.20130214git%{git_short_hash}.2
Summary:        Erlang implementation of the Django Template Language
Group:          Development/Java
License:        MIT
URL:            https://github.com/%{github_username}/%{short_name}
# The tarball comes from here:
# http://github.com/%{github_username}/%{short_name}/tarball/master
# GitHub has layers of redirection and renames that make this a troublesome
# URL to include directly.
Source0:        %{github_username}-%{short_name}-%{git_short_hash}.tar.gz
Patch1:         erlang-erlydtl-0001-Remove-support-for-parametrized-modules.patch
Provides:       ErlyDTL = %{version}-%{release}
BuildRequires:  erlang-rebar
Requires:       erlang-compiler%{?_isa}
Requires:       erlang-erts%{?_isa}
Requires:       erlang-eunit%{?_isa}
# FIXME
# Error:erlang(gettext_compile:close_file/0)
# Error:erlang(gettext_compile:fmt_fileinfo/1)
# Error:erlang(gettext_compile:open_po_file/3)
# Error:erlang(gettext_compile:write_header/0)
# Error:erlang(gettext_compile:write_pretty/1)
Requires:       erlang-gettext%{?_isa}
Requires:       erlang-kernel%{?_isa}
Requires:       erlang-stdlib%{?_isa}
Requires:       erlang-syntax_tools%{?_isa}


%description
ErlyDTL is an Erlang implementation of the Django Template Language. The
erlydtl module compiles Django Template source code into Erlang bytecode. The
compiled template has a "render" function that takes a list of variables and
returns a fully rendered document.


%prep
%setup -q -n %{github_username}-%{short_name}-%{git_short_hash}
%patch1 -p1 -b .no_parametrized_modules


%build
rebar compile -v


%check
make test


%install
mkdir -p %{buildroot}/%{_libdir}/erlang/lib/erlydtl-%{version}/
cp -r ebin     %{buildroot}/%{_libdir}/erlang/lib/erlydtl-%{version}/
cp -r bin      %{buildroot}/%{_libdir}/erlang/lib/erlydtl-%{version}/
cp -r priv     %{buildroot}/%{_libdir}/erlang/lib/erlydtl-%{version}/


%files
%dir %{_libdir}/erlang/lib/erlydtl-%{version}
%{_libdir}/erlang/lib/erlydtl-%{version}/*
%doc README_I18N
%doc README.markdown



%changelog
* Fri May 06 2016 neoclust <neoclust> 0.7.0-5.20130214git6a9845f.2.mga6
+ Revision: 1009765
- Rebuild post boostrap
- imported package erlang-erlydtl

