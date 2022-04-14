# -*- coding: utf-8 -*-

import argparse

from pykeen.pipeline import pipeline

from utils import load_config


def run_baseline(config: dict) -> None:
    """Run a Baseline Model With Default Parameters"""

    pipeline_result = pipeline(
        dataset=config["dataset"],
        dataset_kwargs={
            "random_state": config["seed"],
            "create_inverse_triples": config["train"]["create_inverse"],
        },
        model=config["model"]["name"],
        model_kwargs={
            "embedding_dim": config["model"]["embedding_dim"],
            "random_seed": config["seed"],
        },
        training_loop="sLCWA",
        training_kwargs={
            "num_epochs": config["train"]["num_epoch"],
        },
        optimizer=config["optimizer"]["class"],
        optimizer_kwargs={"lr": config["optimizer"]["lr"]},
        negative_sampler_kwargs={
            "num_negs_per_pos": config["train"]["num_negative"],
        },
        random_seed=config["seed"],
        evaluator_kwargs={"filtered": True},
        use_testing_data=False,
    )

    pipeline_result.save_to_directory(config["save"]["path"])


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--config",
        help="Path to required YAML configuration file",
        required=True,
    )

    args = parser.parse_args()

    config: dict = load_config(args.config)
    assert config["type"] == "baseline", "Incorrect Config Type"

    run_baseline(config)
