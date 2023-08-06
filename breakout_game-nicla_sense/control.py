import asyncio
import pyautogui
import time
from struct import unpack
from bleak import BleakClient

address = "2c:06:e5:19:ce:89"
characteristic_uuid = "19b10000-2905-537e-4f6c-d104768a1214"

async def main(address):
    async with BleakClient(address) as client:
        client.get_services()
        while True: 
            data = await client.read_gatt_char(characteristic_uuid)
            x, y, z = unpack('fff', data)
            print(x,y,z)
            '''if x<-2500 and x<2500:
                pyautogui.press('up')
                print("up")
                time.sleep(1)
            if x>2500 and x>-2500:
                pyautogui.press('down')
                ..      print("down")'''
            if y<-2500 and y<2500:
                pyautogui.press('left')
                print("left")
            if y>2500 and y>-2500:
                pyautogui.press('right')
                print("right")
            if z>10000:
                print("Pause")
                pyautogui.press('space')

asyncio.run(main(address))