# Knowledge Graph Embedding Models in Drug Discovery

![Maturity level-1](https://img.shields.io/badge/Maturity%20Level-ML--1-yellow)
[![Arxiv](https://img.shields.io/badge/ArXiv-2105.10488-orange.svg)](https://arxiv.org/abs/2105.10488)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/pykeen)](https://img.shields.io/pypi/pyversions/pykeen)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

This repository accompanies our paper [Understanding the Performance of Knowledge Graph Embeddings in Drug Discovery](https://arxiv.org/abs/2105.10488) and enables replication of the key results.

## Installation Dependencies

The dependencies required to run the notebooks can be installed as follows:

```shell
$ pip install -r requirements.txt
```

The code relies primarily on the [PyKEEN](https://github.com/pykeen/pykeen) package, which uses [PyTorch](https://pytorch.org/) behind the scenes for gradient computation. If you are planning to retrain the models, instead of using the pretrained weight file provided as part of this repository, it would be advisable to ensure you install a GPU enabled version of PyTorch first. Details on how to do this are provided [here](https://pytorch.org/get-started/locally/).


## Citation

Please consider citing the paper for this repo if you find it useful:

```
@article{bonner2021understanding,
  title={Understanding the performance of knowledge graph embeddings in drug discovery},
  author={Bonner, Stephen and Barrett, Ian P and Ye, Cheng and Swiers, Rowan and Engkvist, Ola and Hoyt, Charles Tapley and Hamilton, William L},
  journal={arXiv preprint arXiv:2105.10488},
  year={2021}
}
```

**License**

- [Apache 2.0](https://github.com/AstraZeneca/awesome-drug-discovery-knowledge-graphs/blob/master/LICENSE)
