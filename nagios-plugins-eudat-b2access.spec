#   Licensed to the Apache Software Foundation (ASF) under one or more
#   contributor license agreements.  See the NOTICE file distributed with
#   this work for additional information regarding copyright ownership.
#   The ASF licenses this file to You under the Apache License, Version 2.0
#   (the "License"); you may not use this file except in compliance with
#   the License.  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

Name:		nagios-plugins-eudat-b2access
Version:	0.2
Release:	1%{?dist}
Summary:	Nagios B2ACCESS probes
License:	Apache License, Version 2.0
Packager:	Shiraz Memon <a.memon@fz-juelich.de>

Source:		%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

Requires:	python
Requires:	python-argparse
Requires:	python-lxml
Requires:	python-simplejson
Requires:	python-defusedxml
Requires:	python-httplib2
Requires:	python-json
Requires:	python-sys
Requires:	python-requests
Requires:	python-signal

%description
Nagios probes to check functionality of B2ACCESS Service

%prep
%setup -q

%define _unpackaged_files_terminate_build 0
%define probe_namespace eudat-b2access 

%install

install -d %{buildroot}/%{_libexecdir}/argo-monitoring/probes/%{probe_namespace}
install -m 755 check_b2access.py %{buildroot}/%{_libexecdir}/argo-monitoring/probes/%{probe_namespace}/check_b2access.py

%files
%dir /%{_libexecdir}/argo-monitoring
%dir /%{_libexecdir}/argo-monitoring/probes/
%dir /%{_libexecdir}/argo-monitoring/probes/%{probe_namespace}

%attr(0755,root,root) /%{_libexecdir}/argo-monitoring/probes/%{probe_namespace}/check_b2access.py

%changelog
* Thu Sep 15 2016 Shiraz Memon <a.memon@fz-juelich.de> - 0.2-1
- Updated namespace and license information
* Thu Jul 28 2016 Shiraz Memon <a.memon@fz-juelich.de> - 0.1-1
- Initial version of the package 