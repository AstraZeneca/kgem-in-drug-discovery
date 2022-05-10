# -*- coding: utf-8 -*-

"""
Provides code to replicate the HPO experiments
"""

import argparse

from pykeen.hpo import hpo_pipeline

from utils import load_config


def run_hpo(config: dict) -> None:
    """Run a HPO run using the provided config"""

    hpo_pipeline_result = hpo_pipeline(
        study_name=config["save"]["study_name"],
        n_trials=config["hpo"]["ntrials"],
        pruner="MedianPruner",
        sampler=config["hpo"]["sampler"],
        dataset=config["dataset"],
        dataset_kwargs={
            "random_state": config["seed"],
            "create_inverse_triples": config["train"]["create_inverse"],
        },
        model=config["model"]["name"],
        model_kwargs={
            "random_seed": config["seed"],
        },
        model_kwargs_ranges=dict(
            embedding_dim=dict(
                type=int,
                low=config["hpo"]["emb"]["low"],
                high=config["hpo"]["emb"]["high"],
                q=config["hpo"]["emb"]["step"],
            ),
        ),
        training_loop="sLCWA",
        training_kwargs_ranges=dict(
            num_epochs=dict(
                type=int,
                low=config["hpo"]["num_epochs"]["low"],
                high=config["hpo"]["num_epochs"]["high"],
                q=config["hpo"]["num_epochs"]["step"],
            ),
        ),
        optimizer=config["optimizer"]["class"],
        optimizer_kwargs_ranges=dict(
            lr=dict(
                type=float,
                low=config["hpo"]["lr"]["low"],
                high=config["hpo"]["lr"]["high"],
            ),
        ),
        negative_sampler_kwargs_ranges=dict(
            num_negs_per_pos=dict(
                type=int,
                low=config["hpo"]["neg"]["low"],
                high=config["hpo"]["neg"]["high"],
                q=config["hpo"]["neg"]["step"],
            ),
        ),
        evaluator_kwargs={"filtered": True},
    )

    hpo_pipeline_result.save_to_directory(config["save"]["path"])

    print("Run Complete!")


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
    assert run_config["type"] == "hpo", "Incorrect Config Type"

    run_hpo(run_config)
