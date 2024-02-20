---
sidebar_position: 1
---

# Introduction

**PyTerrier is a Python-based information retrieval (IR) framework** that is used for researching, testing, and building IR models and systems. It is built on top of the Terrier IR platform and provides a declarative interface and a set of operators that make it easy to build and experiment with different IR pipelines.

Here are some specific examples of how PyTerrier can be used:

- **Researching IR models:** Implement and evaluate a wide range of IR models, such as Boolean models, language models, and neural ranking models.
- **Testing IR systems:** Test the performance of IR systems on standard test collections, such as TREC and CLEF.
- **Building IR systems:** Build production IR systems for a variety of applications, such as web search, enterprise search, and e-commerce search

[**Don't know what is IR? Don't worry!**](./category/beginner-start-here)

## Getting started
You can either run this library on your local machine or on [Google Colab](https://colab.research.google.com).

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
#### Local Machine
```bash
pip install python-terrier
```
> For Colab use `!pip` instead

### Install from Github

```bash
pip install --upgrade git+https://github.com/terrier-org/pyterrier.git#egg=python-terrier
```
> There is no need to have a local installation of the Java component, Terrier. PyTerrier will download the latest release on startup.

### Verification
To ensure that pyterrier is successfully installed, you can perform a quick check running the following code::

```python
import pyterrier as pt

# Check if pyterrier is already initialized
if not pt.started():
    # If not initialized, initiate pyterrier
    pt.init()
```
If there's no error occur then, volla you have finished installing PyTerrier!

## What's next?
- If you are a beginner, check out the [Beginner start here!](./category/beginner-start-here) section.
- If you are familiar with IR concept already, check out the [Overview](./category/overview) section instead.



