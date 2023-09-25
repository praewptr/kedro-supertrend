"""
This is a boilerplate pipeline 'preprocessdata'
generated using Kedro 0.18.12
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import df_preprocess


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=df_preprocess,
            inputs="params:preprocess_data",
            outputs="preprocessed_data_1d",
            name="df_preprocess",
        )
    ])
