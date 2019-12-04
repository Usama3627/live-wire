# Livewire Fast Implementation in Python

Livewire is a semi-automatic 2D image segmentation software. This implementation is based on python 3.7. It aims to be optimal and have minimum response time. It is based on [paper of Dr Omer Ishaq on Livewire:](https://pdfs.semanticscholar.org/3788/6be0aad4767acd9e07da28d6b2d4c719655d.pdf)

## Working

Image is read and converted to grayscale. It is converted in a undirected weight graph. The weights are calculated using simple gradient and each pixel is assigned weights (right and bottom). The edges of object gets the lowest weights. Dijkastra is used to compute the edge of object as it follows the shortest path.

The shortest path nodes (pixels) are returned and are converted to white to display the edge. Next edge can be calculated.

## Usage

Run the script.
Image will open
Click and mouse left button at one point
Relase mouse left button at another point
Press 'c'
New image will open showing the segment with white border
You can press 'c' to close the new window and select the points again

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

This project has 3 contributors:
* Usama3627
* Ahmed
* Abdullah

We welcome and support contributions. Here is a list of tasks to do:

* Undo the previous edge made
* Apply cython to achieve faster results
* Remove press and hold mouse click and replace with single clicks (better interface)
* Select a point and click to get segementated part, now the last point should become first point and we will only need to click once for the second segmentation
* Make the white border thicker (Perferably depending on the size of image)

## License
GNU GPL V3

See the licnese for more information
