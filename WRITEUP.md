### Analysis of resource options for deploying the app

Comparison between VM and App Service

|   | VM  | App Service  |  Valuation for case |
|---|---|---|---|
| monthly Costs  | A1 Instance Basic Tier = $23.13 | B1 Instance Basic Tier = $13.14  | App Service is cheaper |
| Scalability  |  Lesser constraints for scalability  |  vertical scaling without redeploy | large Scaling is not an issue -> App Service |
| Availability  | Single Instance, Standard SSD 99.5%  | 99.95%  | App Service has slightly higher availability without choosing Premium Services |
| Workflow  | VMs are IaaS, so comparable with real Hardware  | Instant deployment, integration with Git  | Easier workflow with App Service |

In this case we should choose App Service over VMs because it has advantages over VMs
in all 4 dimensions.


### Which app changes could change the decision in the future?

* If the underlying technology stack may change, with VMs we could use Windows as the underlying OS, so .NET can be used
* If we plan to switch the cloud provider, with App Service we are kind of locked in to the Azure world
* If we need legacy apps, that have to be installed in a VM
* If our scalability requirements increase a lot


