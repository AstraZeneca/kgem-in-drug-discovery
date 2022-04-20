# Knowledge Graph Embedding Models in Drug Discovery

![Maturity level-1](https://img.shields.io/badge/Maturity%20Level-ML--1-yellow)
[![Arxiv](https://img.shields.io/badge/ArXiv-2105.10488-orange.svg)](https://arxiv.org/abs/2105.10488)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/pykeen)](https://img.shields.io/pypi/pyversions/pykeen)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

<p align="center">
  <img width="800" src="https://github.com/AstraZeneca/kgem-in-drug-discovery/raw/master/result.png">
</p>

This repository accompanies our paper [Understanding the Performance of Knowledge Graph Embeddings in Drug Discovery](https://arxiv.org/abs/2105.10488) and enables replication of the key results.

## Overview

In this work we investigate the predictive performance of five KGE models on two public drug discovery-oriented KGs. Our goal is not to focus on the best overall model or configuration, instead we take a deeper look at how performance can be affected by changes in the training setup, choice of hyperparameters, model parameter initialisation seed and different splits of the datasets. Our results highlight that these factors have significant impact on performance and can even affect the ranking of models. Indeed these factors should be reported along with model architectures to ensure complete reproducibility and fair comparisons of future work, and we argue this is critical for the acceptance of use, and impact of KGEs in a biomedical setting.

The models we investigate are: 

- [ComplEX](https://arxiv.org/abs/1606.06357)
- [DistMult](https://arxiv.org/abs/1412.6575)
- [RotatE](https://arxiv.org/abs/1902.10197)
- [TransE](https://papers.nips.cc/paper/2013/hash/1cecc7a77928ca8133fa24680a88d2f9-Abstract.html)
- [TransH](https://ojs.aaai.org/index.php/AAAI/article/view/8870)

With the following datasets being used:

- [Hetionet](https://het.io)
- [BioKG](https://github.com/dsi-bdi/biokg)

### HyperParameter Values

Part of this study was a detailed search over the hyperparameter space for all models and across both datasets. Below we report the best overall values below for each dataset. Note that these values are taken from experiments with a fixed training setup consisting of the Adagrad optimiser and the use of Margin Ranking Loss with no inverse relations.

#### **Hetionet**

| **Model** | **Embedding Size** | **Num Epochs** | **Learning Rate** | **Num Negatives** |
|-----------|--------------------|----------------|-------------------|-------------------|
| ComplEx   | 272                | 700            | 0.03              | 91                |
| DistMult  | 80                 | 400            | 0.02              | 41                |
| RotatE    | 512                | 500            | 0.03              | 41                |
| TransE    | 304                | 500            | 0.02              | 61                |
| TransH    | 480                | 800            | 0.005             | 1                 |

#### **BioKG**

| **Model** | **Embedding Size** | **Num Epochs** | **Learning Rate** | **Num Negatives** |
|-----------|--------------------|----------------|-------------------|-------------------|
| ComplEx   | 464                | 600            | 0.09              | 91                |
| DistMult  | 480                | 100            | 0.05              | 71                |
| RotatE    | 448                | 900            | 0.06              | 31                |
| TransE    | 448                | 600            | 0.1               | 91                |
| TransH    | 368                | 900            | 0.06              | 31                |

## Installation Dependencies

The dependencies required to run the notebooks can be installed as follows:

```shell
$ pip install -r requirements.txt
```

The code relies primarily on the [PyKEEN](https://github.com/pykeen/pykeen) package, which uses [PyTorch](https://pytorch.org/) behind the scenes for gradient computation. If you want to run the experiments, it would be advisable to ensure you install a GPU enabled version of PyTorch first. Details on how to do this are provided [here](https://pytorch.org/get-started/locally/).

Note that all of the models and both of the datasets are provided as part of the the PyKEEN package so there is no need to download the datasets separately.

## Reproducing Experiments 

This repository contains code to replicate the experiments detailed in the accompanying manuscript. Each experiment is run by using the combination of a python scrip and associated YAML configuration file. The general format of this is *experiment.py* with the path to the config file providing the remaining information in the format : *experiment/dataset/model*.

We now provide examples of running each experiment. Please note that the results of these experiments will be saved in the **results** directory at the root of this repository.

### Baseline Experiments

The baseline experiments are run using sensible default hyper-parameters and can be used to compare again more optimised values. The baseline experiments can each be run as follows:

```shell
$ python src/baseline.py -c config/baseline/hetionet/rotate.yaml
```
Where both the dataset and model can be chosen from those available.

### Hyper-Parameter Optimisation Experiments

The HPO experiments will perform 100 repeats to find the optimal hyper parameters for a given dataset and model combination. The HPO experiments can each be run as follows:

```shell
$ python src/hpo.py -c config/hpo/hetionet/rotate.yaml
```
Where both the dataset and model can be chosen from those available. Note that by default we use the TPE search method, however a random search can also be used by changing the value for the sampler configuration option in the YAML files.

#### Task Specific HPO

The previous experiment optimised the hyperparameters across all relation types. In these experiments, we optimise over only edges between gene and disease entities. 

```shell
$ python src/hpo_relation.py -c config/hpo_relation/hetionet/rotate.yaml
```
Note that only the Hetionet dataset can be used for these experiments.

### Model Random Seed Experiments

The model seeds experiments are designed to assess how variations in the random seed used to initialise the model parameters affect predictive performance. As such, ten repeats over different random seeds are performed. The model random seed experiments can each be run as follows:

```shell
$ python src/model_seed_repeats.py -c config/model_repeats/hetionet/rotate.yaml
```
Where both the dataset and model can be chosen from those available.

### Dataset Split Experiments

These experiments are designed to assess how changes in the train/test split in the dataset can affect predictive performance. These experiments can each be run as follows:

```shell
$ python src/dataset_repeats.py -c config/datasplits/hetionet/rotate.yaml
```
Where both the dataset and model can be chosen from those available.

### Ablation Experiments

In these experiments, we investigate how the training setup (loss function, optimizer and use of inverse relations) can impact predictive performance. Please note this this experiment will run the repeats over all models and datasets from a single script - thus there is no need to specify a specific model or dataset choice.

```shell
$ python src/ablation.py
```

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
