import asyncio
from bleak import BleakScanner
import math
import time

TARGET_NAME = "GuideBeacon"
TX_POWER = -59  # Adjust based on calibration

# Smoothing to reduce noise
last_rssi = None
alpha = 0.2  # for exponential moving average

def estimate_distance(rssi, tx_power=TX_POWER, n=2.0):
    return 10 ** ((tx_power - rssi) / (10 * n))

def detection_callback(device, advertisement_data):
    global last_rssi

    if device.name == TARGET_NAME:
        rssi = device.rssi

        # Optional: smooth noisy RSSI
        if last_rssi is not None:
            rssi = alpha * rssi + (1 - alpha) * last_rssi
        last_rssi = rssi

        distance = estimate_distance(rssi)
        print(f"[{time.strftime('%H:%M:%S')}] RSSI: {rssi:.2f}, Distance: {distance:.2f} meters")

async def main():
    scanner = BleakScanner(detection_callback)
    await scanner.start()
    print("Scanner started (real-time mode)...")
    while True:
        await asyncio.sleep(0.1)  # Keep loop alive

asyncio.run(main())
