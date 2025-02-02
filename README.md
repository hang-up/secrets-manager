# Keeper Secrets Manager

Keeper Secrets Manager is a component of the Keeper Enterprise platform. It provides your DevOps, IT Security and
software development teams with a fully cloud-based, Zero-Knowledge platform for managing all of your
infrastructure secrets such as API keys, Database passwords, access keys, certificates and any type of confidential data.

Common use cases for Secrets Manager include:
- Removing hard-coded credentials from source code
- Replacing configuration file secrets
- Pulling secrets into CI/CD systems like Jenkins, GitHub Actions and More
- Protecting access to privileged passwords, API keys and other managed secrets.
- Providing vault access to machines and applications

### Documentation
[Secrets Manager Guide](https://docs.keeper.io/secrets-manager/secrets-manager/overview)

[Keeper Commander Guide](https://docs.keeper.io/secrets-manager/commander-cli/overview)

[Enterprise Admin Guide](https://docs.keeper.io/enterprise-guide/)


### Integrations

|    | Links     |  Test Status                                                                                                | Published Artifacts                                                                                                                                                                                         |
-----|------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
**Ansible** | [Docs](https://docs.keeper.io/secrets-manager/secrets-manager/integrations/ansible-plugin)  <br />[Source](https://github.com/Keeper-Security/secrets-manager/tree/master/integration/keeper_secrets_manager_ansible)   | ![Ansible](https://github.com/Keeper-Security/secrets-manager/actions/workflows/test.ansible.yml/badge.svg) | [![Ansible](https://img.shields.io/pypi/v/keeper-secrets-manager-ansible?style=for-the-badge&logo=ansible)](https://pypi.org/project/keeper-secrets-manager-ansible/) |
**Azure DevOps Extension** | [Docs](https://docs.keeper.io/secrets-manager/secrets-manager/integrations/azure-devops-plugin) <br /> [Source](https://github.com/Keeper-Security/secrets-manager/tree/master/integration/keeper_secrets_manager_azure_pipeline_extension)  |                                                                                                    | [![Visual Studio Marketplace Version](https://img.shields.io/visual-studio-marketplace/v/KeeperSecurity.keeper-secrets-manager?label=Azure%20DevOps%20Extension&logo=azuredevops&style=for-the-badge)](https://marketplace.visualstudio.com/items?itemName=KeeperSecurity.keeper-secrets-manager)           |
**GitHub Action**  | [Docs](https://docs.keeper.io/secrets-manager/secrets-manager/integrations/github-actions) <br /> [Source](https://github.com/Keeper-Security/ksm-action) | | [![GitHub Action](https://img.shields.io/github/v/tag/Keeper-Security/ksm-action?label=GitHub%20Action&logo=github&logoColor=white&style=for-the-badge)](https://github.com/marketplace/actions/keeper-secrets-manager-github-action) |
**Terraform Provider**  | [Docs](https://docs.keeper.io/secrets-manager/secrets-manager/integrations/terraform)  <br /> [Source](https://github.com/keeper-security/terraform-provider-secretsmanager) | | [![Terraform Provider](https://img.shields.io/github/v/tag/Keeper-Security/terraform-provider-keeper?label=Terraform&logo=terraform&logoColor=white&style=for-the-badge)](https://registry.terraform.io/providers/Keeper-Security/secretsmanager/latest) |
**Jenkins Plugin**  | [Docs](https://docs.keeper.io/secrets-manager/secrets-manager/integrations/jenkins-plugin)  <br />[Source](https://github.com/jenkinsci/keeper-secrets-manager-plugin) | | [![Jenkins](https://img.shields.io/github/v/tag/jenkinsci/keeper-secrets-manager-plugin?label=Plugins%20Index&logo=jenkins&logoColor=white&style=for-the-badge)](https://plugins.jenkins.io/keeper-secrets-manager/) |
**BitBucket Plugin**  | [Docs](https://docs.keeper.io/secrets-manager/secrets-manager/integrations/bitbucket-plugin) <br /> [Source](https://bitbucket.org/keepersecurity/keeper-secrets-manager-pipe)| |
**Docker Image** | [Docs](https://docs.keeper.io/secrets-manager/secrets-manager/integrations/docker-image) | |
**Docker Runtime** | [Docs](https://docs.keeper.io/secrets-manager/secrets-manager/integrations/docker-runtime)| |
**Kubernetes** | [Docs](https://docs.keeper.io/secrets-manager/secrets-manager/integrations/kubernetes)| |
**GitLab** | [Docs](https://docs.keeper.io/secrets-manager/secrets-manager/integrations/gitlab-plugin)| |


### Tools

|    | Links     |  Test Status                                                                                                | Published Artifacts                                                                                                                                                                                         |
-----|------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
**KSM CLI** | [Docs](https://docs.keeper.io/secrets-manager/secrets-manager/secrets-manager-command-line-interface)  <br /> [Source](https://github.com/Keeper-Security/secrets-manager/tree/master/integration/keeper_secrets_manager_cli)     | ![CLI](https://github.com/Keeper-Security/secrets-manager/actions/workflows/test.cli.yml/badge.svg)         | [![PyPi](https://img.shields.io/pypi/v/keeper-secrets-manager-cli?style=for-the-badge&logo=windowsterminal)](https://pypi.org/project/keeper-secrets-manager-cli/)<br />[Installer](https://github.com/Keeper-Security/secrets-manager/releases?q=cli&expanded=true)                                                     |
**PowerShell** | [Docs](https://docs.keeper.io/secrets-manager/secrets-manager/integrations/powershell-plugin) <br />  [Source](https://github.com/Keeper-Security/secrets-manager/tree/master/integration/keeper_secrets_manager_cli) | | [![PowerShell](https://img.shields.io/powershellgallery/v/SecretManagement.Keeper?style=for-the-badge&logo=powershell&logoColor=white)](https://www.powershellgallery.com/packages/SecretManagement.Keeper)                                                     |

### SDKs

|    | Links     |  Test Status                                                                                                | Published Artifacts                                                                                                                                                                                         |
-----|------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
**JavaScript** | [Docs](https://docs.keeper.io/secrets-manager/secrets-manager/developer-sdk-library/javascript-sdk) <br />[Source](https://github.com/Keeper-Security/secrets-manager/tree/master/sdk/javascript/packages/core)  | ![Javascript](https://github.com/Keeper-Security/secrets-manager/actions/workflows/test.js.yml/badge.svg)   | [![NPM](https://img.shields.io/npm/v/@keeper-security/secrets-manager-core?style=for-the-badge&logo=npm&logoColor=white)](https://www.npmjs.com/package/@keeper-security/secrets-manager-core)    |
**Python** | [Docs](https://docs.keeper.io/secrets-manager/secrets-manager/developer-sdk-library/python-sdk) <br /> [Source](https://github.com/Keeper-Security/secrets-manager/tree/master/sdk/python)      | ![Python](https://github.com/Keeper-Security/secrets-manager/actions/workflows/test.python.yml/badge.svg)   | [![PyPi](https://img.shields.io/pypi/v/keeper-secrets-manager-core?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/keeper-secrets-manager-core/)                     |
**Java** |  [Docs](https://docs.keeper.io/secrets-manager/secrets-manager/developer-sdk-library/java-sdk)  <br /> [Source](https://github.com/Keeper-Security/secrets-manager/tree/master/sdk/java/core)       | ![Java](https://github.com/Keeper-Security/secrets-manager/actions/workflows/test.java.yml/badge.svg)       | [![Maven Central](https://img.shields.io/maven-central/v/com.keepersecurity.secrets-manager/core?style=for-the-badge&logo=java&logoColor=white)](https://search.maven.org/artifact/com.keepersecurity.secrets-manager/core) |
**.NET** |  [Docs](https://docs.keeper.io/secrets-manager/secrets-manager/developer-sdk-library/.net-sdk)  <br /> [Source](https://github.com/Keeper-Security/secrets-manager/tree/master/sdk/dotNet)     | ![.NET](https://github.com/Keeper-Security/secrets-manager/actions/workflows/test.dotnet.yml/badge.svg)     | [![Nuget](https://img.shields.io/nuget/v/Keeper.SecretsManager?style=for-the-badge&logo=nuget&logoColor=white)](https://www.nuget.org/packages/Keeper.SecretsManager)                                                       |
**Go** | [Docs](https://docs.keeper.io/secrets-manager/secrets-manager/developer-sdk-library/golang-sdk) <br /> [Source](https://github.com/Keeper-Security/secrets-manager-go)  | ![GoLang](https://github.com/keeper-security/secrets-manager-go/actions/workflows/test.go.yml/badge.svg)    | [![Go](https://img.shields.io/github/v/tag/Keeper-Security/secrets-manager-go?label=Go&logo=go&logoColor=white&style=for-the-badge)](https://github.com/Keeper-Security/secrets-manager-go)                                   |

More information about Keeper Secrets Manager, SDKs, tools, and integrations can be found in our [official documentation 
portal](https://docs.keeper.io/secrets-manager/secrets-manager/overview)

### About Keeper Security
Keeper is the leading cybersecurity platform for preventing password-related data breaches and cyberthreats.

Learn More at:
[https://keepersecurity.com](https://keepersecurity.com)
