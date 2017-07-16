import asyncio
import logging
import xknx

from custom_components.xknx import _LOGGER, DATA_XKNX, \
    XKNXSensor

@asyncio.coroutine
def async_setup_platform(hass, config, add_devices, \
        discovery_info=None):
    """Setup the XKNX light platform."""
    if DATA_XKNX not in hass.data \
            or not hass.data[DATA_XKNX].initialized:
        return False

    entities = []

    for device in hass.data[DATA_XKNX].xknx.devices:
        if isinstance(device, xknx.Sensor) and \
                not device.is_binary():
            entities.append(XKNXSensor(hass, device))

    add_devices(entities)

    return True
