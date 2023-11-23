import logging
import subprocess

from tidevice._device import Device

if __name__ == '__main__':
    device_id = '00008110-001261920EA1401E'
    IOS_APP_BUNDLE = 'com.kwai.video.stannis.TestApp'
    idev = Device(device_id)
    cmd = f'python -m tidevice launch {IOS_APP_BUNDLE}'
    count = 0
    while True:
        subprocess.run(cmd, shell=True)
        # idev.app_kill(IOS_APP_BUNDLE)
        # pid = idev.app_start(IOS_APP_BUNDLE)
        # assert pid != -1, 'launch app error'
        count += 1
        print(f'count: {count}')