Name:           perl-MooseX-App
Version:        1.33
Release:        4%{?dist}
Summary:        Write user-friendly command line apps with even less suffering
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/MooseX-App/
Source0:        http://www.cpan.org/authors/id/M/MA/MAROS/MooseX-App-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl
BuildRequires:  perl(base)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Config::Any)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(I18N::Langinfo)
BuildRequires:  perl(if)
BuildRequires:  perl(IO::Interactive)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Pluggable::Object)
BuildRequires:  perl(Moose) >= 2.00
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Types::Path::Class)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(overload)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Pod::Elemental)
BuildRequires:  perl(Pod::Elemental::Selectors)
BuildRequires:  perl(Pod::Elemental::Transformer::Nester)
BuildRequires:  perl(Pod::Elemental::Transformer::Pod5)
BuildRequires:  perl(Pod::Perldoc)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Text::WagnerFischer)
BuildRequires:  perl(utf8)
# Tests only
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(Test::NoWarnings)
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
Requires:       perl(I18N::Langinfo)
Requires:       perl(Moose) >= 2.00

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Moose\\)$

%description
MooseX-App is a highly customisable helper to write user-friendly command
line applications without having to worry about most of the annoying things
usually involved. Just take any existing Moose class, add a single line
(use MooseX-App qw(PluginA PluginB ...);) and create one class for each
command in an underlying namespace. Options and positional parameters can
be defined as simple Moose accessors.

%prep
%setup -q -n MooseX-App-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENCE
%doc Changes README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.33-2
- Perl 5.22 rebuild

* Tue Apr 21 2015 Petr Šabata <contyk@redhat.com> - 1.33-1
- 1.33 bump

* Sun Mar 22 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.32-1
- Update to 1.32

* Tue Feb 10 2015 Petr Šabata <contyk@redhat.com> - 1.31-1
- 1.31 bump

* Tue Dec 02 2014 Petr Šabata <contyk@redhat.com> - 1.30-2
- Fix build issues pointed out in the review

* Thu Nov 27 2014 Petr Šabata <contyk@redhat.com> 1.30-1
- Initial packaging
