# coding: utf-8

"""
    Arm API

    REST API to manage your virtual devices.  # noqa: E501

    The version of the OpenAPI document: 1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import AvhClientAsync
from AvhClientAsync.models.project_settings import ProjectSettings  # noqa: E501
from AvhClientAsync.rest import ApiException

class TestProjectSettings(unittest.TestCase):
    """ProjectSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProjectSettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = AvhClientAsync.models.project_settings.ProjectSettings()  # noqa: E501
        if include_optional :
            return ProjectSettings(
                version = 1.337, 
                internet_access = True, 
                dhcp = True
            )
        else :
            return ProjectSettings(
        )

    def testProjectSettings(self):
        """Test ProjectSettings"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()