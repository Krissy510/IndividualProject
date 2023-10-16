---
sidebar_position: 1
---

# Introduction

**PyTerrier is a Python-based information retrieval (IR) framework** that is used for researching, testing, and building IR models and systems. It is built on top of the Terrier IR platform and provides a declarative interface and a set of operators that make it easy to build and experiment with different IR pipelines.

Here are some specific examples of how PyTerrier can be used:

- **Researching IR models:** Implement and evaluate a wide range of IR models, such as Boolean models, language models, and neural ranking models.
- **Testing IR systems:** Test the performance of IR systems on standard test collections, such as TREC and CLEF.
- **Building IR systems:** Build production IR systems for a variety of applications, such as web search, enterprise search, and e-commerce search

[**Don't know what IR is? <u>Click here!</u>**](./category/beginner-start-here)

## Getting started

### What you'll need

- [Python](https://www.python.org/downloads/) 3.7  or newer.
- [Java](https://www.java.com/en/download/) 11 or newer. 
- PyTerrier is natively supported on Linux, Mac OS X and Windows.

You can check the requirements using the following command:


**Python**
```bash
python -V
```
> Note: If `python` is not found, try `python3 -V` instead

**Java**
```bash
java -version
```

### Installation

Installing PyTerrier is easy - it can be installed from the command-line in the normal way using Pip:
```bash
pip install python-terrier
```

If you want the latest version of PyTerrier, you can install direct from the Github repo:

```bash
pip install --upgrade git+https://github.com/terrier-org/pyterrier.git#egg=python-terrier
```
> There is no need to have a local installation of the Java component, Terrier. PyTerrier will download the latest release on startup.

### Your first PyTerrier

Similar to other Python library you will need to start by importing PyTerrrier and running `init()`.
```python
import pyterrier as pt
pt.init()
```
## Start your site

Run the development server:

```bash
cd my-website
npm run start
```

The `cd` command changes the directory you're working with. In order to work with your newly created Docusaurus site, you'll need to navigate the terminal there.

The `npm run start` command builds your website locally and serves it through a development server, ready for you to view at http://localhost:3000/.

Open `docs/intro.md` (this page) and edit some lines: the site **reloads automatically** and displays your changes.
