# -*- coding: utf-8 -*-

"""
Provides code to replicate the ablation experiments
"""

from pykeen.ablation import ablation_pipeline


def run_ablation() -> None:
    """Run an Ablation study"""

    save_dir: str = "./results/ablation"
    ablation_pipeline(
        directory=save_dir,
        models=[
            "ComplEx",
            "DistMult",
            "RotatE",
            "TransE",
            "TransH",
        ],
        datasets=[
            "Hetionet",
            "BioKG",
        ],
        losses=[
            "BCEAfterSigmoidLoss",
            "NSSA",
            "MarginRankingLoss",
            "SoftplusLoss",
        ],
        optimizers=[
            "Adam",
            "SGD",
            "Adagrad",
        ],
        create_inverse_triples=[
            True,
            False,
        ],
        training_loops="sLCWA",
        epochs=500,
        n_trials=1,
    )


if __name__ == "__main__":

    run_ablation()
