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
  "type":"tool",
  "is_on_github":"True",
  "name":"Regolith",
  "desc":"Regolith is an Addon Compiler for the Bedrock Edition of Minecraft.",
  "author":"Bedrock-OSS",
  "supported_platforms":["Windows","Linux"],
  
  "supported_platforms_download_links":{
    "Windows":{
      "AMD64":"https://github.com/Bedrock-OSS/regolith/releases/download/{}/regolith_{}_Windows_x86_64.zip",
      "x86":"https://github.com/Bedrock-OSS/regolith/releases/download/{}/regolith_{}_Windows_x86.zip"
    },
    "Linux":{
      "AMD64":"https://github.com/Bedrock-OSS/regolith/releases/download/{}/regolith_{}_Linux_x86_64.zip",
      "x86":"https://github.com/Bedrock-OSS/regolith/releases/download/{}/regolith_{}_Linux_x86.zip"

    }

  }
}
```



