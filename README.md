# ILCD2py

ILCD2py is an ILCD+EPD parser for Python.

# Motivation

This Python package aims to simplify the process of parsing and reading ILCD+EPD files and convert them to a machine
and human-readable format for exchanging EPD data within the building industry.
The de facto EPD standard ILCD+EPD is targeted scientists and environmental professionals, but it is too complex for the
average engineer and architect.

A format that ILCD+EPD can be converted to, but only holds the essential information of the ILCD+EPD that we in the AEC
industry need.

```yaml
name: My EPD
source: https://epd.com/4daa559c-1ddc-41e6-808c-ac50cd077162?version=0.1.0
unit: m
version: 0.1.0
expiration_date: 2025-01-01
gwp:
  a1a3: 25
  a4: 10
odp:
  a1a3: 12
  a4: 2
```

## ILCD+EPD

The ILCD+EPD format is a digital format for EPDs.
Provided in either XML or JSON.

Initially EPDs were provided as PDFs.
That is not very convenient for automation processes and requires large amounts of manual work to process.

The ILCD (International Life Cycle Data System) is a data format developed by the European Commission to give LCA
practitioners a common digital format for life cycle assessments.
In order to integrate EPD specific information (e.g. scenarios, modules, type of data), extensions were added to the
ILCD format. The resulting format got named ILCD+EPD format.

The ECO Platform and Ökobau uses the format to store and expose EPDs through
the [soda4LCA](https://bitbucket.org/okusche/soda4lca/src/7.x-branch/) API.
The API makes it possible for everyone to search and download tons of EPDs to be used free of charge.

The ILCD+EPD format is a node based format. It means that each EPD consists of several layers of nodes that contain
different information.
The first node contains a summary of the EPD, with references to the nodes.
By drilling down the tree of nodes, you have access to more and more specific information, such as EPD manufacturer,
functional unit(s), etc.

Read more about ILCD at the [European Platform on Life Cycle Assessment](https://eplca.jrc.ec.europa.eu/)

# License

Unless otherwise described, the code in this repository is licensed under the Apache-2.0 License. Please note that some
modules, extensions or code herein might be otherwise licensed. This is indicated either in the root of the containing
folder under a different license file, or in the respective file's header. If you have any questions, don't hesitate to
get in touch with us via email.
