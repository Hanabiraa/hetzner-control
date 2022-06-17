# hetzner-control


`hetzner-control` its CLI tool, which lets you easily manage servers on [the Hetzner platform](https://www.hetzner.com/)

![Sample usage gif](./assets/sample_usage.gif)

## Table of contents
* [Motivation](#Motivation)
* [Usage](#Usage)
* [Installation guide](#Installation-guide)
* [Want to contribute?](#Want-to-contribute?)
* [License](#License)

## Motivation

I wanted to create a console application that would interact 
with the REST API of the cloud service for convenient server management
and the platform in general. 

I also wanted to improve my skills in application
design and API work while I'm studying software engineering in university.

## Usage

```shell
$ htz [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show documentation message for available commands/flags

**Commands**:

* `info`: Information about available data centers, servers, prices
* `server`: Operations with servers
* `version`: Show app version

[For a more detailed description of the command, see wiki page](https://github.com/Hanabiraa/hetzner-control/wiki)

## Installation guide
1. First, install environment variable, i.e. in .bashrc
```shell
$ export HETZNER_API_TOKEN="YOUR_HETZNER_TOKEN_HERE"
```

2. Installation option
   * You can install hetzner-control from pip 
      ```shell
      $ pip3 install hetzner-control
      ```
   * Or you can clone the repository and build the wheel/sdist module with poetry (you can preinstall poetry):
       ```shell
       $ git clone https://github.com/Hanabiraa/hetzner-control.git
       $ cd hetzner-control
       $ poetry install
       $ poetry build
       ```

## Want to contribute?

1. Clone repo and create a new branch: $ git checkout https://github.com/Hanabiraa/hetzner-control -b name_for_new_branch.
2. Make changes and test
3. Submit Pull Request with comprehensive description of changes

## License

MIT License