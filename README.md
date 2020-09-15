# Moneypenny

Moneypenny is my attempt to create a minimalistic and easy-to-extend voice assistant for various purposes. 
It was designed in a way that (should!) yield to a high degree of modularity, both during usage and development.
While far from being perfect, I am rather happy with how it turned out.


## Architecture and Design

The project was designed and structured so that new functionality can easily be added and integrated with only a small amount of changes on the existing code base.
In the nomenclature of the project, each functionality is implemented as an *agent*, derived from the *TopicAgent* class. 
All agents registered with moneypenny are started in seperate threads to ensure a high degree of decoupling between the server (moneypenny) and its clients (the agents). 
Communication is between server and client is handled through multiprocessing queues.

The definition of each agent contains a set of commands representative for that agent's functionality.
Once the user issues a command, it is compared to the example of all registered agents.
The agent with the highest similarity to the issued command gets chosen.
For simplicity reasons (and a personal interest in sentence embeddings), I decided to use [InferSent](https://github.com/facebookresearch/InferSent) for computing the sentence vectors for both comparison and actual commands. 
The similarity between both is then derived using cosine similarity.




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

<!-- ## License
[MIT](https://choosealicense.com/licenses/mit/) -->