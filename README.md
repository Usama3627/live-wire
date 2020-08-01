# Livewire Fast Implementation in Python

Livewire is a semi-automatic 2D image segmentation software. This implementation is based on python 3.7. It aims to be optimal and have minimum response time. It is based on [paper of Dr Omer Ishaq on Livewire:](https://pdfs.semanticscholar.org/3788/6be0aad4767acd9e07da28d6b2d4c719655d.pdf)

## Working

Image is read and converted to grayscale. It is converted in a undirected weight graph. The weights are calculated using simple gradient and each pixel is assigned weights (right and bottom). The edges of object gets the lowest weights. Dijkastra is used to compute the edge of object as it follows the shortest path.

The shortest path nodes (pixels) are returned and are converted to white to display the edge. Next edge can be calculated likewise.

## Usage

1. Run the script.
2. Image will open
3. Click and mouse left button at one point
4. Relase mouse left button at another point
5. Press 'c'
6. New image will open showing the segment with white border
7. You can press 'c' to close the new window and select the points again

## Technical Requirement

Python 3.x

Libraries used:
* OpenCv
* Numpy
* math
* [Dijkstar 2.5](https://pypi.org/project/Dijkstar/)
* Time

Tested on Ubuntu 19.04, Ubuntu 18.04, Windows 10 with Python 3.7

## Contributions

Check [contribution guidelines](https://github.com/Usama3627/live-wire/blob/master/CONTRIBUTING.md) for more information

## License
GNU GPL V3

See the [License](https://github.com/Usama3627/live-wire/blob/master/LICENSE) for more information
