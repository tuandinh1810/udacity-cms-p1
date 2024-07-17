# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

Cost:Azure App Service:Typically charged based on the tier (Basic, Standard, Premium, etc.) and the number of instances. Pricing includes compute resources, storage, and other features such as traffic management.Easier to predict costs due to fixed pricing tiers while VM charged based on the size of the VM, the number of VMs, and the duration they are running. Other factors include OS, storage, and network usage so an be harder to predict as costs vary with usage and configuration.
Scalability:Azure App Service easy auto scalling out as well as scale up. For the scalling of VM will be complex based on setting up and managing Azure VM scale set
Availability: App Service automatically handles availability with built-in load balancing and redundancy with offers an SLA of 99.95% or higher, depending on the tier.VM need to requires setting up availability sets or zones to ensure high availability.
Workflow: App service easily integrates with Azure DevOps, GitHub, and other CI/CD tools and other Azure services and built-in support many languages and frameworks such as .NET, .NET Core, Java, Node.js, PHP, and Python. For VM spent lots of effort to deploy and configure and also involves managing the OS, updates, patches, and other configurations.
### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 
