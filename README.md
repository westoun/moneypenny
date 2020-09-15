# Moneypenny

Moneypenny is my attempt to create a minimalistic and easy-to-extend voice assistant for various purposes (without sending all my data to Amazon & Co.)


## Architecture and Design


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install any missing dependencies:
```bash
pip3 install -r requirements.txt
```

If you are planning to use [InferSent](https://github.com/facebookresearch/InferSent) to compute sentence similarity, make sure you have the corresponding [model file](https://github.com/facebookresearch/InferSent/blob/master/models.py) available within the project folder.

## Usage

```bash
python3 main.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)