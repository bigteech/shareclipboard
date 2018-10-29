import netifaces
import json
import asyncio

port = 10258

def get_gateways():
    return netifaces.gateways()['default'][netifaces.AF_INET][0]

def get_ip_lists(gateway):
    ip_lists = []
    for i in range(1, 256):
        ip_lists.append('{}{}'.format(gateway[:-1], i))
    return ip_lists

def get_proto(manager):


    class EchoServerClientProtocol(asyncio.DatagramProtocol):

        def connection_made(self, transport):
            self.transport = transport

        def data_received(self, data):
            try:
                msg = json.loads(data.decode())
            except:
                self.transport.close()
                return
            msg_type = msg.get('type')
            if not type:
                self.transport.close()
                return
            handler = manager.get_msg_handler(msg_type)
            if handler:
                self.transport.write(bytes(handler(msg.get('data')), 'utf-8'))
            self.transport.close()

    return EchoServerClientProtocol



class HostManager():
    reged_hosts = {}
    name= ''
    host_change_handler = lambda x: 0
    handler_mapping = {}

    def __init__(self):
        self.echoServerClientProtocol = get_proto(self)

    def reg_msg_handler(self, type, handler):
        self.handler_mapping[type] = handler

    def get_msg_handler(self, type):
        return self.handler_mapping.get(type)

    def set_host_change_handler(self, handler):
        self.host_change_handler = handler;

    def set_name(self, name):
        self.name = ''

    def get_hosts(self):
        return self.reged_hosts

    def reg(self, name, host):
        self.reged_hosts.append((name, host,))

    def heartbeat(self):
        gateway = get_gateways()
        ip_lists = get_ip_lists(gateway)

        loop = asyncio.new_event_loop()
        message = '{"type": "reg", "name": {self.name}}'
        for ip in ip_lists:
            try:
                coro = loop.create_connection(lambda: asyncio.DatagramProtocol(message, loop),
                                          ip, port)
                loop.create_task(coro)
            except Exception as e:
                print(e)
        loop.run_until_complete()
        asyncio.sleep(100)
        self.heartbeat()

    def listen(self):
        loop = asyncio.new_event_loop()
        coro = loop.create_server(self.echoServerClientProtocol, '0.0.0.0', port)
        server = loop.run_until_complete(coro)
        loop.run_forever()


manager = HostManager()