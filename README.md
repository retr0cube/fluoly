<h1 align="center">Fluoly</h1>

<p align="center">
  <img src="https://user-images.githubusercontent.com/61835816/136807923-8e65758d-d12d-47b2-90de-0c510904c069.png" />
</p>

<div align="center">
 <p><img src="https://img.shields.io/github/license/retr0cube/fluoly?color=red&amp;label=Repo%20License&amp;style=flat-square" alt="GitHub"> 
 <img src="https://img.shields.io/github/downloads/retr0cube/fluoly/total?color=blue&amp;label=Downloads&amp;style=flat-square" alt="GitHub all releases"> 
 <img src="https://img.shields.io/github/issues/retr0cube/fluoly?color=green&amp;label=Issues&amp;style=flat-square" alt="GitHub issues"> 
 <a href="https://github.com/retr0cube/fluoly/stargazers">
 <img src="https://img.shields.io/github/stars/retr0cube/fluoly?color=yellow&amp;label=Stars&amp;style=flat-square" alt="GitHub stars"></a> 
</div>

<p align="center">
 ↦ A Package manager that downloads any Add-on, tool/software or plugins you'd ever imagine.
</p>

## How does it work?
↦ It's a repo full of <code>.json</code> files that contains data about an Add-on/Tool, then Fluoly access that data & downloads the requested Add-on/tool.
## Installation
### Windows:
↦ To install fluoly on Windows use the offline installer <a href="https://github.com/retr0cube/fluoly/releases/latest">Here</a>. The installer will prompt you to install it to all users which requires administrator permissions  or the current user only! Then choose the path of installation and Voilà! You now have fluoly installed, to check if it is installed correctly, open <code>powershell</code>, or Windows terminal if you are on Windows 11, then type <code>fluoly --help</code> if it shows something similar to this image, then you're good to go:
<p align="center">
  <img src="https://user-images.githubusercontent.com/61835816/135756126-10b47e41-6d51-405f-8e35-6b54ee3d3885.png" />
</p>  

↦ If it dumps an error similar to: `"fluoly" is not recognised as an interal or external command` or `fluoly: The term 'fluoly' is not recognized as a name of a cmdlet, function, script file, or executable program.` , Then check if the installation path is ![Added correctly to the PATH environnement variable.]("https://www.architectryan.com/2018/08/31/how-to-change-environment-variables-on-windows-10/")

#### Note: Linux/Android are not currently yet supported.
## Usage
↦ Currently, there are two commands: 
  - The `install` command will... well install a package, currently there are 3 types of packages: Tools, Add-ons & Plugins. 
  - The `show` command will show info about a package: name, version, author and description.

