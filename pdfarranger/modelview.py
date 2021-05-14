# Copyright (C) 2021 Manfred Holger
# Copyright (C) 2008-2017 Konstantinos Poulios, 2018-2019 Jerome Robert
#
# pdfarranger is free software; you can redistribute it and/or modify
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

import gi

# check that we don't need GObject.threads_init()
#gi.check_version('3.10.2')
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GObject


class Selection:

    def __init__(self, view):
        self._view =view
        self._items = sorted(view.get_selected_items(), key=lambda x: x[0])

    def __len__(self):
        return len(self._items)

    @property
    def indices(self):
        '''
        Sorted list of indices of selected items
        '''
        return [item[0] for item in self._items]

    @property
    def is_contiguous(self):
        indices = self.indices
        return len(indices) == indices[-1] - indices[0] + 1

    @property
    def items(self):
        '''
        Sorted list of selected items (paths)
        '''
        return self._items

    @property
    def pages(self):
        return [row[0] for row in self._view.model if row.path in self._items]


class PageStore(Gtk.ListStore):
    '''
    The PageStore keeps track of all pages in PDF Arranger.
    Each element is a list [page, page.description()] where
    page is an instance of core.Page
    '''

    def __init__(self, *args, **kw):
        super().__init__(GObject.TYPE_PYOBJECT, str)

    @property
    def pages(self):
        return [row[0] for row in self]

    def paginate(self):
        for i, page in enumerate(self.pages):
            page.page_no = i + 1


class PageView(Gtk.IconView):

    def __init__(self):
        super().__init__(PageStore())

    @property
    def model(self):
        return self.get_model()

    @property
    def selection(self):
        return Selection(self)
