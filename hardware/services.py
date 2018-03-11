from .models import Device
from pin.services import switch_pin


def get_devices(limit=None):
    if limit:
        return Device.objects.all()[:limit]
    return Device.objects.all()


def switch_device(device_id, state=None):
    device = Device.objects.get(pk=device_id)
    pin = device.relay.pin.number
    if state is None:
        state = not device.is_active
    switch_pin(int(pin), not state)
    device.is_active = state
    device.save()
    return state

