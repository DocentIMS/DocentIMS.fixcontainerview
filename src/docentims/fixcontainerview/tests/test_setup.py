# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from docentims.fixcontainerview.testing import DOCENTIMS_FIXCONTAINERVIEW_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that docentims.fixcontainerview is properly installed."""

    layer = DOCENTIMS_FIXCONTAINERVIEW_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if docentims.fixcontainerview is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'docentims.fixcontainerview'))

    def test_browserlayer(self):
        """Test that IDocentimsFixcontainerviewLayer is registered."""
        from docentims.fixcontainerview.interfaces import (
            IDocentimsFixcontainerviewLayer)
        from plone.browserlayer import utils
        self.assertIn(IDocentimsFixcontainerviewLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = DOCENTIMS_FIXCONTAINERVIEW_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['docentims.fixcontainerview'])

    def test_product_uninstalled(self):
        """Test if docentims.fixcontainerview is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'docentims.fixcontainerview'))

    def test_browserlayer_removed(self):
        """Test that IDocentimsFixcontainerviewLayer is removed."""
        from docentims.fixcontainerview.interfaces import IDocentimsFixcontainerviewLayer
        from plone.browserlayer import utils
        self.assertNotIn(IDocentimsFixcontainerviewLayer, utils.registered_layers())
