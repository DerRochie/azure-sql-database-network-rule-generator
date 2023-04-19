# SDB-Network-Rule-Generator
Generates Terraform compatable Azure SDB network rules from Microsoft provided ServiceTag CIDR addresses provided here - https://www.microsoft.com/en-us/download/confirmation.aspx?id=56519

## prerequisites
Python 3 (I tested with 3.11.1 and it worked)

pip install azure-identity;
pip install azure-mgmt-network

## usage
python SDB-Network-Rule-Generator.py -i 'canadacentral' -i 'canadaeast' -i 'europenorth'

-i is for each location. Eg. canadacentral, canadaeast. You can have an unlimited amount of -i(tems)
```
python SDB-Network-Rule-Generator.py -i 'canadacentral' -i 'canadaeast' -i 'europenorth'

  "sql.canadacentral.13.71.168.0::27" = {
        # 13.71.168.0/27
        startIpAddress = "13.71.168.0"
        endIpAddress   = "13.71.168.31"
    }
    
  "sql.canadaeast.40.69.104.0::27" = {
        # 40.69.104.0/27
        startIpAddress = "40.69.104.0"
        endIpAddress   = "40.69.104.31"
    }

  "sql.northeurope.191.235.193.140::31" = {
        # 191.235.193.140/31
        startIpAddress = "191.235.193.140"
        endIpAddress   = "191.235.193.141"
    }
```

## location list
australiacentral
australiacentral2
australiaeast
australiasoutheast
brazilsouth
brazilsoutheast
canadacentral
canadaeast
centralindia
centralus
centraluseuap
eastasia
eastus
eastus2
eastus2euap
eastus2stage
francecentral
francesouth
germanynorth
germanywestcentral
japaneast
japanwest
jioindiacentral
jioindiawest
koreacentral
koreasouth
northcentralus
northcentralusstage
northeurope
norwayeast
norwaywest
polandcentral
qatarcentral
southafricanorth
southafricawest
southcentralus
southcentralusstg
southeastasia
southindia
swedencentral
swedensouth
switzerlandnorth
switzerlandwest
uaecentral
uaenorth
uksouth
ukwest
westcentralus
westeurope
westindia
westus
westus2
westus3
