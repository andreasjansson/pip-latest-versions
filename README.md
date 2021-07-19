# pip-latest-versions

_Simple script that fetches latest versions of pip packages from Pypi, in the requirements.txt format_

## Usage

```
$ python pip_latest_versions.py <requirements_file>
```

## Example

Given a file `~/projects/my-project/requirements.txt` file with the following contents:

```
tqdm
numpy==1.16
sk-video
torch
opencv-python
moviepy
```

Running the script outputs to stdout. Packages that don't have versions will be queried on Pypi and the latest version will be output:

```
$ python pip_latest_versions.py ~/projects/my-project/requirements.txt
tqdm==4.61.2
numpy==1.16
sk-video==1.1.10
torch==1.9.0
opencv-python==4.5.3.56
moviepy==1.0.3
```
