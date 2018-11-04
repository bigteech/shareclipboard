import json
import asyncio
import datetime
import socket
port = 10958


def get_proto(manager):
    last=""

    class EchoServerClientProtocol(asyncio.DatagramProtocol):

        def connection_made(self, transport):
            self.transport = transport

        def datagram_received(self, data, addr):
            nonlocal last
            if last == data:
                return
            last = data
            try:
                msg = json.loads(data.decode())
            except:
                return
            msg_type = msg.get('type')
            if not type:
                return
            handler = manager.get_msg_handler(msg_type)
            if handler:
                self.transport.sendto(bytes(handler(msg.get('data'), addr), encoding='utf-8'), addr)

    return EchoServerClientProtocol


class HostManager():
    reged_hosts = {}
    name= ''
    host_change_handler = lambda x: 0
    handler_mapping = {}
    bordercast = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bordercast.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    def __init__(self):
        self.echoServerClientProtocol = get_proto(self)

    def reg_msg_handler(self, type, handler):
        self.handler_mapping[type] = handler

    def get_msg_handler(self, type):
        return self.handler_mapping.get(type)

    def set_name(self, name):
        self.name = name

    def get_hosts(self):
        for k, v in self.reged_hosts.items():
            if (datetime.datetime.now() - v[1]).seconds > 60:
                self.reged_hosts.pop(k, None)
        return self.reged_hosts

    def reg(self, name, host):
        self.reged_hosts['host'] = (name, datetime.datetime.now(),)

    async def heartbeat(self, fun_to_flush):
        self.send_data('{"type": "reg", "data": "%s"}' % self.name)
        await asyncio.sleep(15)
        await self.heartbeat(fun_to_flush)

    def send_msg(self, data):
        self.send_data('{"type": "text", "data": "%s"}' % data)

    def send_data(self, data):
        self.bordercast.sendto(data.encode('utf-8'), ('<broadcast>', port))

    def listen(self):
        loop = asyncio.get_event_loop()
        coro = loop.create_datagram_endpoint(self.echoServerClientProtocol, allow_broadcast=True, local_addr=('0.0.0.0', port))
        loop.create_task(coro)

manager = HostManager()