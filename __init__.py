# -*- coding: utf-8 -*-

# Copyright (C) 2020 PipelineML
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
This package encapsulates the PipelineML GeoPackager plugin for QGIS.
"""

# Import (from the 'plugin' module within this
# package) the 'PipelineMLGeoPackagerPlugin' class.
from .plugin import PipelineMLGeoPackagerPlugin

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Define the required 'classFactory' function,
# which is called when the plugin is loaded.
def classFactory(iface):
    """
    This function returns an instance of the plugin class.
    """
    return PipelineMLGeoPackagerPlugin(iface)
