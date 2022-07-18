import os
import importlib


for base, dirs, files in os.walk("src/k8s_datamodels"):
    module = base.replace("src/", "").replace("/__pycache__", "").replace("/", ".")
    importlib.import_module(module)
