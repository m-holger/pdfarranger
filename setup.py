#!/usr/bin/env python3

#
# pdfarranger - GTK+ based utility for splitting, rearrangement and
# modification of PDF documents.
# Copyright (C) 2008-2017 Konstantinos Poulios
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
import os
from setuptools import setup
from DistUtilsExtra.command import (
    build_i18n, clean_i18n, build_extra, build_icons)

gh_workflow = os.environ.get('GH', None)

if gh_workflow is None:
    install_requires = ['pikepdf>=2.12.0','python-dateutil>=2.8.1']
    extras_require = {
            'image': ['img2pdf>=0.4.1'],
    }
else:
    install_requires = ['pikepdf>=1.7.0','python-dateutil>=2.4.0']
    extras_require = {
            'image': ['img2pdf>=0.3.4'],
        }


data_files = [
    ('share/applications', ['data/com.github.jeromerobert.pdfarranger.desktop']),
    ('share/pdfarranger', ['data/pdfarranger.ui', 'data/menu.ui']),
    ('share/man/man1', ['doc/pdfarranger.1']),
    ('share/metainfo', ['data/com.github.jeromerobert.pdfarranger.metainfo.xml']),
]

setup(
    name='pdfarranger',
    version='1.7.1',
    author='Jerome Robert',
    author_email='jeromerobert@gmx.com',
    description='A simple application for PDF Merging, Rearranging, and Splitting',
    url='https://github.com/pdfarranger/pdfarranger',
    license='GNU GPL-3',
    packages=['pdfarranger'],
    data_files=data_files,
    zip_safe=False,
    cmdclass={
        "build": build_extra.build_extra,
        "build_i18n": build_i18n.build_i18n,
        "clean_i18n": clean_i18n.clean_i18n,
        "build_icons": build_icons.build_icons,
    },
    entry_points={
        'console_scripts': ['pdfarranger=pdfarranger.pdfarranger:main']
    },
    install_requires=install_requires,
    extras_require=extras_require
)
