# 🌿 Fluoly ![GitHub](https://img.shields.io/github/license/retr0cube/fluoly?label=License&color=blue&style=flat-square)![GitHub pull requests](https://img.shields.io/github/issues-pr/retr0cube/fluoly?label=Pull%20Requests&style=flat-square)
- An Open Source Add-on Library/Repo for Minecraft: Bedrock Edition.
## How does it work?
- it's a repo full of `.json` files that contains data about an Add-on/Tool, then Fluoly access that data & downloads the requested Add-on/tool.
#### Example:
```cmd
fluoly install regolith
```
- The `.json` data accessed:
```json
{
  "name":"Regolith",
  "desc":"Regolith is an Addon Compiler for the Bedrock Edition of Minecraft.",
  "is_repo_os": "True",
  "author":"Bedrock_OSS",
  "gh_api_link":"https://api.github.com/repos/Bedrock-OSS/regolith/releases/latest",
  "platforms":{
    "win_86":"regolith_{}_Windows_x86.zip",
    "win_amd64":"regolith_{}_Windows_x86_64.zip",
    "win_armv7":"regolith_{}_Windows_armv7.zip",
    "win_armv6":"regolith_{}_Windows_armv6.zip"
  }
}

```
