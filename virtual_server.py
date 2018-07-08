import SoftLayer
import ConfigParser
from SoftLayer.managers.vs import VSManager


class VirtualServer:
    def __init__(self):
        self.conf = ConfigParser.ConfigParser()
        self.conf.read('client_info.conf')
        self.username = self.get_config_val('DEFAULT', 'username')
        self.api_key = self.get_config_val('DEFAULT', 'api_key')

        self.client = SoftLayer.Client(username=self.username, api_key=self.api_key)
        self.virtual_server_manager = VSManager(self.client)

    def get_config_val(self, section, field):
        return self.conf.get(section, field)

    def list_virtual_server(self):
        """
        1. Function signature
            list_instances(self, hourly=True, monthly=True, tags=None, cpus=None,
                       memory=None, hostname=None, domain=None,
                       local_disk=None, datacenter=None, nic_speed=None,
                       public_ip=None, private_ip=None, **kwargs):

            **kwargs can be mask, limits and so on.

        2. Can have following masks
            'id',
            'globalIdentifier',
            'hostname',
            'domain',
            'fullyQualifiedDomainName',
            'primaryBackendIpAddress',
            'primaryIpAddress',
            'lastKnownPowerState.name',
            'powerState',
            'maxCpu',
            'maxMemory',
            'datacenter',
            'activeTransaction.transactionStatus[friendlyName,name]',
            'status',

        :return: list of virtual servers
        """
        mask = 'id,hostname'
        return self.virtual_server_manager.list_instances(mask=mask)


def main():
    vs = VirtualServer()
    virtual_server_list = vs.list_virtual_server()
    for vs in virtual_server_list:
        print vs['id'], '--', vs['hostname']


if __name__ == '__main__':
    main()
