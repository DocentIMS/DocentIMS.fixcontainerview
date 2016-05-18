# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import docentims.fixcontainerview


class DocentimsFixcontainerviewLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=docentims.fixcontainerview)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'docentims.fixcontainerview:default')


DOCENTIMS_FIXCONTAINERVIEW_FIXTURE = DocentimsFixcontainerviewLayer()


DOCENTIMS_FIXCONTAINERVIEW_INTEGRATION_TESTING = IntegrationTesting(
    bases=(DOCENTIMS_FIXCONTAINERVIEW_FIXTURE,),
    name='DocentimsFixcontainerviewLayer:IntegrationTesting'
)


DOCENTIMS_FIXCONTAINERVIEW_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(DOCENTIMS_FIXCONTAINERVIEW_FIXTURE,),
    name='DocentimsFixcontainerviewLayer:FunctionalTesting'
)


DOCENTIMS_FIXCONTAINERVIEW_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        DOCENTIMS_FIXCONTAINERVIEW_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='DocentimsFixcontainerviewLayer:AcceptanceTesting'
)
