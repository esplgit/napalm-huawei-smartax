import unittest

from napalm_huawei_smartax import huawei_smartax
from napalm.base.test.base import TestConfigNetworkDriver, TestGettersNetworkDriver  # noqa


class TestConfigSmartAXDriver(unittest.TestCase, TestConfigNetworkDriver):

    @classmethod
    def setUpClass(cls):
        """Executed when the class is instantiated."""
        cls.vendor = 'huawei_smartax'
        cls.device = huawei_smartax.SmartAXDriver(
            '127.0.0.1',
            'vagrant',
            'vagrant',
            timeout=60,
            optional_args={
                'port': 22,
            },
        )
        cls.device.open()
