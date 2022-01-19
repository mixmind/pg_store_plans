# SPEC file for pg_store_plans
# Copyright(c) 2021, NIPPON TELEGRAPH AND TELEPHONE CORPORATION

%define _pgdir   /usr/pgsql-10
%define _bindir  %{_pgdir}/bin
%define _libdir  %{_pgdir}/lib
%define _datadir %{_pgdir}/share

%if "%(echo ${MAKE_ROOT})" != ""
  %define _rpmdir %(echo ${MAKE_ROOT})/RPMS
%endif

## Set general information for pg_store_plans.
Summary:    Record executed plans on PostgreSQL 10
Name:       pg_store_plans10
Version:    1.6
Release:    1%{?dist}
License:    BSD
Group:      Applications/Databases
#URL:        http://example.com/pg_store_plans/
Vendor:     NIPPON TELEGRAPH AND TELEPHONE CORPORATION

## We use postgresql-devel package
Requires:  postgresql10-libs, postgresql10-server

## Description for "pg_store_plans"
%description

pg_store_plans provides capability to record statistics for every plan
executed on PostgreSQL.

Note that this package is available for only PostgreSQL 10.

## Set variables for install
%install
PATH=/usr/pgsql-10/bin:$PATH
mkdir -p %{buildroot}/usr/pgsql-10/lib/bitcode/pg_store_plans
mkdir -p %{buildroot}/usr/pgsql-10/share/extension/
cp -r %{_topdir}/../../pg_store_plans.so %{buildroot}/usr/pgsql-10/lib/
cp -r %{_topdir}/../../pg_store_plans.control %{buildroot}/usr/pgsql-10/share/extension/
cp -r %{_topdir}/../../pg_store_plans*.sql %{buildroot}/usr/pgsql-10/share/extension/

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,root)
%{_libdir}/pg_store_plans.so
%defattr(0644,root,root)
%{_datadir}/extension/pg_store_plans--1.6.sql
%{_datadir}/extension/pg_store_plans.control


# History of pg_store_plans.
%changelog
* Wed Nov 18 2021 Tatsuro Yamada, Julien Rouhaud, Kyotaro Horiguchi
- Version 1.6. Supports PostgreSQL 14
* Wed Jan 27 2021 Kyotaro Horiguchi
- Version 1.5. Supports PostgreSQL 13
* Thu Jan 30 2020 Kyotaro Horiguchi
- Version 1.4. Supports PostgreSQL 12
* Tue Jan 22 2019 Kyotaro Horiguchi
- Supports PostgreSQL 10
* Tue Oct 10 2017 Kyotaro Horiguchi
- Supports PostgreSQL 10
* Fri Aug 26 2016 Kyotaro Horiguchi
- Some fix in plan representation functions.
* Wed Apr 13 2016 Kyotaro Horiguchi
- Support PostgreSQL 9.5
* Fri Jun 12 2015 Kyotaro Horiguchi
- Initial version.


