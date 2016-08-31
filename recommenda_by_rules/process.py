#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from utils.config_helper import ConfigHelper
from get_recmd_model_key import get_recmd_model_key_by_running_model_selector
from get_recmd_result import get_recmd_result_by_running_models
import logging
import os

__author__ = 'LH Liu'

logger = logging.getLogger()


def process(model_conf_path):
    # 1.1 load model selectors and models' conf
    model_confs = ConfigHelper.load_config(model_conf_path)
    model_selector = model_confs.get('model_selector')
    models = model_confs.get('models')
    # 1.2 load recmd requirement's conf
    requirements = ConfigHelper.load_config(os.path.join(os.path.dirname(__file__), 'conf', 'recmd_requirement.yaml'))

    # 2 get model key bu running model selector
    if model_selector:
        recmd_model_key = get_recmd_model_key_by_running_model_selector(requirements, model_selector)
    else:
        recmd_model_key = 'default'

    # 3 get model by recmd key and run model
    if models:
        recmd_result = get_recmd_result_by_running_models(models, recmd_model_key, requirements)
    else:
        raise

    return recmd_result
