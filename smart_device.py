#!/usr/bin/env python3
"""
This module defines a SmartDevice class that represents a smart device.
"""


from typing import Any


class SmartDevice:
    """
    Represents a smart device.
    """
    device_count = 0

    def __init__(self, device_name, model_number):
        """
        Initialize a SmartDevice instance.
        """
        self.device_name = device_name
        self.model_number = model_number
        self.is_online = False
        self.status = {}
        SmartDevice.device_count += 1

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """
        Call the device.
        """
        return f"{self.device_name} (Model: {self.model_number})"

    def update_status(self, attribute, value):
        """
        Update the status of the device.
        """
        self.status[attribute] = value

    def get_status(self, attribute):
        """
        Get the status of the device.
        """
        return self.status.get(attribute, 'Attribute not found')

    def toggle_online(self):
        """
        Toggle the online status of the device.
        """
        self.is_online = not self.is_online

    def reset(self):
        """
        Reset the device.
        """
        self.is_online = False
        self.status = {}

    def device_info():
        """
        Get the device information.
        """
        return {
            "is_online": SmartDevice.is_online,
            "status": SmartDevice.status,
        }
