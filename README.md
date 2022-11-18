# Roadmaper - a Roadmap as Code (RaC) Tool

## Purpose
As the repo name implies, this purpose of this python library is used to draw roadmap by using python code. This is the first Roadmap as Code (RaC) library. RaC helps to create and edit roadmap in a more efficient way without having to use any graphical tools that are not always easy to use to create or update a roadmap.

With git repository like GitHub or Bitbucket, roadmaps created using RaC can be version controlled, track changes and can be easily shared with others.

### Current version
v.0.1.0-beta2

### Python version requirements:
* Python 3.10+
  
### Library Dependencies
* PyCairo 1.21.0
* Colour 0.1.5
* python-dateutil

<hr>

## Installation
### Install from PyPI
```bash
pip install roadmap-generator
```
### Upgrade to the latest version
If you are running older version of roadmap-generator, you can upgrade to the latest version by running the following command:
```bash
pip install --upgrade roadmap-generator
```

<hr>

## Documentation
Please refer to [Roadmapper Wiki](https://github.com/csgoh/roadmap-generator/wiki) for more information on how to use this RaC library.

<hr>

## Code Example

```python 
from generator.roadmap import Roadmap
from generator.timelinemode import TimelineMode

roadmap = Roadmap(1200, 312)
roadmap.set_title("My Demo Roadmap")
roadmap.set_timeline(TimelineMode.MONTHLY, "2023-02-01", 12)

group = roadmap.add_group("Core Product Work Stream")

task = group.add_task("Base Functionality", "2022-11-01", "2023-10-31")
task.add_milestone("v.1.0", "2023-02-15")
task.add_milestone("v.1.1", "2023-08-01")

parellel_task = task.add_parallel_task("Enhancements", "2023-11-15", "2024-03-31")
parellel_task.add_milestone("v.2.0", "2024-03-30")

task = group.add_task("Showcase #1", "2023-03-01", "2023-05-07")
task.add_parallel_task("Showcase #2", "2023-06-01", "2023-08-07")


roadmap.set_footer("Generated by Roadmap Generator")
roadmap.draw()
roadmap.save("demo01.png")
```

### Output

![name](demo07.png)



