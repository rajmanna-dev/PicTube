# PicTube: Background Remover

## 🗿 Introduction
This is an <b>official PicTube</b> repository.

A flask (python web framework) based web application 
that can remove background from JPG, PNG and JPEG image 
files.

## 🔧 Dependencies and Installation

* Python >= 3.10 (Recommended version: 3.12.1)
* Pip 23.3.2

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PicTube.

```bash
# Upgrade pip package manager
pip install -U pip

# Install requirements
pip install -r requirements.txt

# Install PicTube
pip install git+https://github.com/rajmanna-dev/PicTube.git
```

## 🚀 Usage

```python
import pictube

# returns 'Pictube-rembg-pic.png'
pictube.del_bg('pic.png')

# returns 'Pictube-rembg-pic.png'
pictube.del_bg('pic.jpg')

# returns 'Pictube-rembg-pic.png'
pictube.del_bg('pic.jpeg')
```

## ⭐ Contributing

Pull requests are welcome. For major changes, 
open an issue first to discuss what you would like to change.

Please make sure to updates tests as appropriate.

## 💻 Testing

Make sure that the application is not returning any 
errors on runtime. Please run and test the application 
on your local machine before making PR by providing .JPG,
.PNG and .JPEG image files as input.
