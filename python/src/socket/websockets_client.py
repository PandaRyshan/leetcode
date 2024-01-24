import asyncio
import websockets


async def client():
    client_id = input('Your id: ')
    async with websockets.connect('ws://localhost:12345') as websocket:
        # 发送客户端id
        await websocket.send(client_id)
        
        # 接收消息
        async def receive_message():
            while True:
                message = await websocket.recv()
                print(f"Received: {message}")

        receive_task = asyncio.ensure_future(receive_message())

        # 用户输入
        while True:
            message = input("Message(target_id, msg): ")
            if message == 'exit':
                break
            await websocket.send(message)

        receive_task.cancel()
        await websocket.close()


async def send_msg(websocket):
    while True:
        message = input("Message(target_id, msg): ")
        if message == 'exit':
            break
        await websocket.send(message)


async def receive_msg(websocket):
    while True:
        try:
            message = await websocket.recv()
            print(f"Received: {message}")
        except websockets.ConnectionClosed:
            print("Connection closed")
            break


async def main():
    uri = "ws://localhost:12345"
    async with websockets.connect(uri) as websocket:
        send_task = asyncio.ensure_future(send_msg(websocket))
        receive_task = asyncio.ensure_future(receive_msg(websocket))

        await asyncio.gather(send_task, receive_task)


asyncio.get_event_loop().run_until_complete(main())
