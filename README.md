
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



## 🔖 Contents:
- [Introduction ⇗](https://github.com/retr0cube/fluoly#-introduction)
- [Installation ⇗](https://github.com/retr0cube/fluoly#-installation)
     - [Windows ⇗](https://github.com/retr0cube/fluoly#-windows)
     - [Build from source (Linux) ⇗](https://github.com/retr0cube/fluoly#-build-from-source)
- [Usage ⇗](https://github.com/retr0cube/fluoly#-usage)
## ❔ Introduction
- Fluoly is a package manager that lets you download any Minecraft: Bedrock Edition Add-on, tool or plugins you'd ever imagine by only using a CLI & completely free.
## 🖥 Installation
###  🪟 _Windows_:
- To install fluoly on Windows use the official binaries [here ⇗](https://github.com/retr0cube/fluoly/releases/latest), open it and 
then the installer will prompt you to choose the path of installation, click `Next` and the installation process will start, & **Voilà**! You have successfully installed fluoly.
- Next to check if Fluoly is installed correctly, open `powershell` or Windows terminal, then type `fluoly --version` if it shows something similar to this image ![image](https://user-images.githubusercontent.com/61835816/145718519-aa54831b-9a57-4bb6-b52a-1bf53c20db08.png), then you're good to go. 
- If it dumps an error similar to: 
```
"fluoly" is not recognised as an interal or external command
```
***or:***
```
fluoly: The term 'fluoly' is not recognized as a name of a cmdlet, function, script file, or executable program.
```
- Please check if the installation path is added correctly to the ![PATH environnement variable ⇗]("https://www.architectryan.com/2018/08/31/how-to-change-environment-variables-on-windows-10").

### 💿 _Build from source_:
- To build fluoly from source, open the terminal and type the following commands:
```bash
git clone https://github.com/retr0cube/fluoly.git
cd ./fluoly
pip install .
```
**These commands will download and install fluoly as a python module, when the process is done delete the `fluoly` directory.**

- To test if it's installed correctly, type the following command:
```
python -m fluoly --version
```
- if it shows the following image ![image](https://user-images.githubusercontent.com/61835816/145718519-aa54831b-9a57-4bb6-b52a-1bf53c20db08.png), Then you're good to go 
- if the latter didn't work, please repeat the installation process, if that didn't help either, don't hesitate to open an issue [here ⇗](https://github.com/retr0cube/fluoly/issues). 

## 📚 Usage
- Currently, there are two commands:

#### - ⬇ Install:
```
  install - Installs an Package.
      Options:
          -sys           TEXT   Lets you choose which operating system version of a
                                package to choose. Note: This is only available for
                                Tools.
          -c, --cpu_arch TEXT   Lets you choose which CPU architecture version of a
                                package to choose. Note: This is also only available for
                                Tools.
          -v, --version  TEXT   Lets you choose which version of a package to choose.
          -p, --path     TEXT   Lets you change the path where the package will be
                                downloaded to.
          -n, --name     TEXT   Changes the file name of the downloaded package file.
```
#### - 🔍 Find:
```
  find - Shows info about an Add-on. 
      Options:
          -md, --read_me TEXT  Shows the README.md of a package
  
```

