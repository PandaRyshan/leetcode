import asyncio
import websockets


connected = {}


async def server(websocket, path):
    global connected
    
    if len(connected) >= 2:
        return

    # 获取客户端id
    client_id = await websocket.recv()
    
    # 注册新客户端
    connected[client_id] = websocket

    try:
        async for message in websocket:
            if message == 'exit':
                break
            
            # 消息格式 [target_id, message]
            target_id, msg = message.split(' ', 1)
            if target_id in connected:
                await connected[target_id].send(msg)
    finally:
        # 客户端断开连接
        del connected[client_id]


start_server = websockets.serve(server, 'localhost', 12345)
print('Server is listening...')

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
