
<p align="center">
  <img src="https://user-images.githubusercontent.com/61835816/145718141-78fe305a-0017-4539-bd02-3dd5c1f5a51a.png"/>
</p>


<div align="center">
 <img alt="GitHub" src="https://img.shields.io/github/license/retr0cube/fluoly?logo=github&style=for-the-badge">
 <img alt="GitHub all releases" src="https://img.shields.io/github/downloads/retr0cube/fluoly/total?color=gree&logo=Markdown&style=for-the-badge"> 
 <img alt="GitHub issues" src="https://img.shields.io/github/issues/retr0cube/fluoly?color=yellow&logo=GitHub%20Actions&logoColor=white&style=for-the-badge">
 <a href="https://github.com/retr0cube/fluoly/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/retr0cube/fluoly?logo=Riseup&style=for-the-badge"></a>
  <img alt="Travis (.com)" src="https://img.shields.io/travis/com/retr0cube/fluoly?logo=travis&logoColor=white&style=for-the-badge">
</div>



## ð Contents:
- [Introduction â](https://github.com/retr0cube/fluoly#-introduction)
- [Installation â](https://github.com/retr0cube/fluoly#-installation)
     - [Windows â](https://github.com/retr0cube/fluoly#-windows)
     - [Build from source (Linux) â](https://github.com/retr0cube/fluoly#-build-from-source)
- [Usage â](https://github.com/retr0cube/fluoly#-usage)
## â Introduction
- Fluoly is a package manager that downloads any Minecraft: Bedrock Edition Add-on, tool/software or plugins you'd ever imagine using a CLI.
## ð¥ Installation
###  ðª _Windows_:
- To install fluoly on Windows use the installer [here â](https://github.com/retr0cube/fluoly/releases/latest), open it and 
then the installer will prompt you to choose the path of installation, click `Next` and the installation process will start, & **VoilÃ **! You now have fluoly installed.
- Next to check if Fluoly is installed correctly, open `powershell` or Windows terminal, then type `fluoly --version` if it shows something similar to this image ![image](https://user-images.githubusercontent.com/61835816/145718519-aa54831b-9a57-4bb6-b52a-1bf53c20db08.png), then you're good to go. 
- If it dumps an error similar to: 
```
"fluoly" is not recognised as an interal or external command
```
***or:***
```
fluoly: The term 'fluoly' is not recognized as a name of a cmdlet, function, script file, or executable program.
```
- Please check if the installation path is Added correctly to the ![PATH environnement variable â]("https://www.architectryan.com/2018/08/31/how-to-change-environment-variables-on-windows-10").

### ð¿ _Build from source_:
- To Buid fluoly from source, open terminal and type the following commands:
```bash
git clone https://github.com/retr0cube/fluoly.git
cd ./fluoly
pip install .
```
**These commands will download and install fluoly as a python module, when the process is done delete the `fluoly` directory.**

- Then to test if it's installed correctly, type the following command:
```
python -m fluoly --version
```
- if it shows the following image ![image](https://user-images.githubusercontent.com/61835816/145718519-aa54831b-9a57-4bb6-b52a-1bf53c20db08.png), Then you're good to go 
- if the past step doesn't work, please go back and repeat the installation process, if that didn't help don't hesitate to open an issue [here â](https://github.com/retr0cube/fluoly/issues). 

## ð Usage
- Currently, there are two commands:

#### - â¬ Install:
```
  install - Installs an Package.
      Options:
          -sys           TEXT   Let's you choose which operating system version of a
                                package to choose. Note: This is only available for
                                Tools.
          -c, --cpu_arch TEXT   Let's you choose which CPU architecture version of a
                                package to choose. Note: This is only available for
                                Tools.
          -v, --version  TEXT   Let's you choose which version of a package to choose.
          -p, --path     TEXT   Let's you change the path where the package will be
                                downloaded to.
          -n, --name     TEXT   Changes the file name of the downloaded package.
```
#### - ð Find:
```
  find - Shows info about an Add-on. 
      Options:
          -md, --read_me TEXT  Shows the README.md of a package
  
```

