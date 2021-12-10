<h1 align="center">Fluoly</h1>

<p align="center">
  <img src="https://user-images.githubusercontent.com/61835816/138651284-ca4ad676-9d0a-432e-8d6c-276c6cd21983.png"/>
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

## 🔖 Index:
- [Installation](https://github.com/retr0cube/fluoly#installation)
     - [Windows](https://github.com/retr0cube/fluoly#windows)
- [Usage](https://github.com/retr0cube/fluoly#usage)
## 🖥 Installation
###  Windows:
- To install fluoly on Windows use the installer [here](https://github.com/retr0cube/fluoly/releases/latest),
  Then the installer will prompt you to choose the path of installation, click `Next` and the installation will start, & **Voilà**! You now have fluoly installed.
- Next to check if it's installed correctly, open `powershell`, or Windows terminal if you are on Windows 11, then type `fluoly --help` if it    shows something similar to this image, then you're good to go:

<p align="center">
  <img src="https://user-images.githubusercontent.com/61835816/138596786-28d14256-f957-403d-ad92-f8fbf4429a2b.png" />
</p>  

- If it dumps an error similar to: 
  ```"fluoly" is not recognised as an interal or external command```;
 ```fluoly: The term 'fluoly' is not recognized as a name of a cmdlet, function, script file, or executable program.```.
- Please check if the installation path is Added correctly to the ![PATH environnement variable ↗]("https://www.architectryan.com/2018/08/31/how-to-change-environment-variables-on-windows-10").


## 📚 Usage
- Currently, there are two commands with the `install` command having more options: 
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

  find - Shows info about an Add-on. 
      Options:
          -md, --read_me TEXT  Shows the README.md of a package
           
  
```

