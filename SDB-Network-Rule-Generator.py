from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient
from ipaddress import ip_network
import argparse


class Program:
    def parse_arguments(self):
        parser = argparse.ArgumentParser(
                        prog = 'app.py',
                        description = 'Generates Terraform compatable Azure SDB network rules from Microsoft provided ServiceTag CIDR addresses https://www.microsoft.com/en-us/download/confirmation.aspx?id=56519')
        parser.add_argument('-i','--item', action='append', help='<Required> Set flag', required=True)
        args = parser.parse_args()
        return args.item
    
    def return_variable_name(self, name, cdir_address):
        cdir_address_without_forward_slash = cdir_address.replace('/', '::')
        variable_name = '{}.{}'.format(name, cdir_address_without_forward_slash)
        return variable_name


    def return_tfvars_format(self, variable_name, start_address, end_address, cdir_address):
        template = '''      "{variable_name}" = {{
        # {cdir_address}
        startIpAddress = "{start_address}"
        endIpAddress   = "{end_address}"
      }}
    '''.format(variable_name=variable_name, cdir_address=cdir_address, start_address=start_address, end_address=end_address)
        return template

    def return_servicetag_json_document(self, location):
        client = NetworkManagementClient(
            credential=DefaultAzureCredential(),
            subscription_id=self.subscription_id,
        )

        response = client.service_tags.list(
            location=location,
        )
        return response
    
    def build_data_object(self):
        self.data_object = {}

        # For each location
        for location in self.servicetag_locations_list:
            self.data_object[location] = self.return_servicetag_json_document(location).values
            
            # For each service in location
            temp = []
            for ServiceTagInformation in self.data_object[location]:
                if ServiceTagInformation.name.lower() == 'sql.' + location:
                    self.data_object[location] = ServiceTagInformation.properties.address_prefixes
        return self.data_object

    def return_tf_format_ip_ranges(self, address_prefixes, name):
        for cdir_address in address_prefixes:
            ipv4_network_object = ip_network(cdir_address)
            if ipv4_network_object.version == 6 : break
            print(self.return_tfvars_format(self.return_variable_name(name, cdir_address), ipv4_network_object[0], ipv4_network_object[-1], cdir_address))
    
    def __init__(self):
        self.servicetag_locations_list = self.parse_arguments()
        self.subscription_id = "feacfb0e-b391-4b00-b3a0-0743513c11a5"
        self.data_object = self.build_data_object()

        if __name__ == "__main__":
            self.main()


    def main(self):
        for location in self.data_object:
            self.return_tf_format_ip_ranges(self.data_object[location], 'sql.' + location)


main = Program()
