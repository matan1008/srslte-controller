import docker
from docker.types import IPAMPool, IPAMConfig


class LteNetwork:
    NAME = 'lte_network'
    SUBNET = '192.168.52.0/24'
    GATEWAY = '192.168.52.254'
    INTERFACE_NAME = 'lte-network'

    def __init__(self, network):
        """
        :param docker.models.networks.Network network: Docker network to wrap.
        """
        self._network = network

    @staticmethod
    def create(name: str = NAME, subnet: str = SUBNET, gateway: str = GATEWAY, interface_name: str = INTERFACE_NAME):
        """
        Create a network for LTE entities.
        :param name: Network name.
        :param subnet: Network subnet.
        :param gateway: Network gateway.
        :param interface_name: Interface name on host.
        :return: LteNetwork object.
        :rtype: LteNetwork
        """
        client = docker.from_env()
        return LteNetwork(client.networks.create(
            name, driver='bridge', options={'com.docker.network.bridge.name': interface_name},
            ipam=IPAMConfig(pool_configs=[IPAMPool(subnet=subnet, gateway=gateway)])
        ))

    def shutdown(self):
        self._network.remove()
