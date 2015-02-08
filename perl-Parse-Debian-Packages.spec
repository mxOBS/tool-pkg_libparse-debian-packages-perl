#
# spec file for package perl-Parse-Debian-Packages
#
# Copyright (c) 2015 Josua Mayer <privacy@not.given>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

#
# Summary and description taken from debian package on Feb 8 2015:
#
# Copyright:
#  2004, Joachim Breitner <nomeata@debian.org>
#  2010, Ansgar Burchardt <ansgar@debian.org>
#  2012, gregor herrmann <gregoa@debian.org>
# License: Artistic or GPL-1+
#
# License: Artistic
# This program is free software; you can redistribute it and/or modify
# it under the terms of the Artistic License, which comes with Perl.
#
# On Debian systems, the complete text of the Artistic License can be
# found in `/usr/share/common-licenses/Artistic'.
#
# License: GPL-1+
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 1, or (at your option)
# any later version.
#
# On Debian systems, the complete text of version 1 of the GNU General
# Public License can be found in `/usr/share/common-licenses/GPL-1'.
#

Name: perl-Parse-Debian-Packages
Version: 0.03
Release: 1
License: Artistic-1.0 or GPL-1.0+
Url: http://search.cpan.org/dist/Parse-Debian-Packages/
Group: Development/Libraries/Perl

BuildArch: noarch
Source: %{name}-%{version}.tar.xz
BuildRequires: perl
BuildRequires: perl-macros
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)

Requires: perl = %{perl_version}
Requires: perl(strict)

Summary: Module for parsing the data from a Debian Packages.gz
%description
Parse::Debian::Packages parses the Packages files used by the Debian
package management tools.

It presents itself as an iterator.  Each call of the ->next method
will return the next package found in the file.

%prep
%setup -q

%build
perl Makefile.PL
make

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root)

%changelog
