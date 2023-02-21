# ABC Export

ABC Export is a tool to export ABCs with versioning

## How to install

You will need some files that several Illogic tools need. You can get them via this link :
https://github.com/Illogicstudios/common

You must specify the correct path of the installation folder in the template_main.py file :
```python
if __name__ == '__main__':
    # TODO specify the right path
    install_dir = 'PATH/TO/abc_export'
    # [...]
```


You also must have a folder "database" full of text file for each asset. A data text file look like this :
```json
{
  "name": "ch_chara",
  "geo": ["ch_chara_rigging_lib:geo"],
  "rig": "ch_chara_rigging_lib",
  "attr": [""],
  "shading": "path\\to\\assets\\ch_chara\\ch_chara_shading_lib.mb"
}
```
---

## Features

### Visualizing

<div align="center">
  <span>
    <img src="https://user-images.githubusercontent.com/94440879/219337250-e517b841-a07e-4e39-b88a-f4fb86363e15.png" width=100%>
  </span>
  <p weight="bold">The snail character reference has been found and displayed in the list of assets</p>
  <br/>
</div>

<div align="center">
  <span>
    <img src="https://user-images.githubusercontent.com/94440879/219337741-24e4670e-3387-4c94-a65f-6ecfa7c94c52.png" width=60%>
  </span>
  <p weight="bold">By specifying the "abc" folder the version in which the asset will be exported is displayed</p>
  <br/>
</div>

A valid folder is an existing folder named "abc".

### Exporting as .abc

<div align="center">
  <span>
    <img src="https://user-images.githubusercontent.com/94440879/219338368-e5218621-3a2a-46d7-a327-208eb314918c.png" width=60%>
  </span>
  <p weight="bold">The export button is ready to export</p>
  <br/>
</div>

The button is enabled when the folder is valid and when atleast one asset is selected. You can specify from which frame to which frame you want to export.

<div align="center">
  <span>
    <img src="https://user-images.githubusercontent.com/94440879/219347243-0525e34d-dcf6-425d-8c7c-8554ac32bd87.png" width=30%>
  </span>
  <p weight="bold">Example of the file architecture built from the ABC Export tool</p>
  <br/>
</div>

With this architecture many assets with the same rigging can be export to differents ABCs (for example "chara_00" and "chara_01").
