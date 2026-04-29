# Databricks notebook source
%pip install -e ..
%restart_python


# COMMAND ----------
!pip install yaml

print("hello")
# COMMAND ----------
from pathlib import Path
import sys
sys.path.append(str(Path.cwd().parent / 'src'))


# COMMAND ----------
import pandas as pd
import yaml
from loguru import logger
from pyspark.sql import SparkSession

from marvel_characters.config import ProjectConfig
from marvel_characters.data_processor import DataProcessor

config = ProjectConfig.from_yaml(config_path="../project_config_marvel.yml", env="dev")

logger.info("Configuration loaded:")
logger.info(yaml.dump(config, default_flow_style=False))

# COMMAND ----------
