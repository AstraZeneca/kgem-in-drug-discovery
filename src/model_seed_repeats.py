# -*- coding: utf-8 -*-

"""
Provides code to replicate model initialisation experiments
"""

import argparse
import random

from pykeen.pipeline import pipeline

from utils import load_config


def run_model_repeats(config: dict) -> None:
    """Run a Baseline Model over different seeds"""

    random.seed(config["seed"])
    seed_list: list = list(random.sample(range(0, 10000), 10))

    for model_seed in seed_list:
        model_seed = int(model_seed)

        pipeline_result = pipeline(
            dataset=config["dataset"],
            dataset_kwargs={
                "random_state": config["seed"],
                "create_inverse_triples": config["train"]["create_inverse"],
            },
            model=config["model"]["name"],
            model_kwargs={
                "embedding_dim": config["model"]["embedding_dim"],
                "random_seed": model_seed,
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
        save_path = config["save"]["path"]
        pipeline_result.save_to_directory(f"{save_path}_{str(model_seed)}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--config",
        help="Path to required YAML configuration file",
        required=True,
    )

    args = parser.parse_args()

    run_config: dict = load_config(args.config)
    assert run_config["type"] == "model_repeat", "Incorrect Config Type"

    run_model_repeats(run_config)
