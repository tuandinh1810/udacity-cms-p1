# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

### Analyze
Cost: 
    - App Service: Typically charged based on the tier (Basic, Standard, Premium, etc.) and the number of instances. Pricing includes compute resources, storage, and features such as traffic management. Easy predict costs due to fixed pricing tiers.
    - VM: Costs are based on the size of the VM, the number of VMs, and the duration they are running. Other factors include OS, storage, and network usage, making it harder to predict costs as they vary with usage and configuration.

Scalability:
    - App Service: Support auto-scaling out as well as scaling up.
    - VM:Support scale  (by resizing the VM) or horizontally (by adding more VMs) but can be complex and involves setting up and managing Azure VM scale sets.

Availability:
    - Azure App Service: Automatically handles availability with built-in load balancing and redundancy, offering an SLA of 99.95% or higher, depending on the tier.
    - Azure VM: Requires manually setting up high availability,fault tolerance, and disaster recovery, offering high flexibility  but complexity and management.

Workflow: 
    - Azure App Service: Easily integrates with Azure DevOps, GitHub, and other CI/CD tools, as well as other Azure services. It has built-in support for many languages and frameworks such as .NET, .NET Core, Java, Node.js, PHP, and Python.
    - Azure VM: Requires significant effort to deploy and configure, including managing the OS, updates, patches, and other configurations.

### Appropriate Solution
Based on the above analysis, I choose Azure App Service for deploying my website due to its advantages in cost predictability, scalability, availability, and workflow integration.
### Why I choose App service
- I don't need to care about infrastructure, sercurity, pathching and scaling
- Support multiple languages such as Python, .NET, .NET Core, Java, Ruby, Node.js, PHP, or Python.
- CI/CD intergated for quickly build and deploy

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

- If the app scales significantly, with a vast increase in the number of users or added features, I would switch to a Virtual Machine.

- Using Azure App Service limits access to the host server. If I need to control the underlying OS or install specific software, I would opt for a Virtual Machine.

- If the application is later implemented in a programming language not supported by Azure App Service, I would choose a VM to create the necessary environment for that language.