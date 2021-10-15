import pandas as pd
import numpy as np
from main import *
from modules.response_processing.load_data import response_data
from modules.response_processing.clean_data import *
import pytest


@pytest.fixture
def raw_test_data():
    raw_test_data = pd.read_csv('data/test_data/survey-results-19-08-21.csv')
    return raw_test_data


@pytest.fixture
def column_headers():
    column_dict = {
        'status_col': 'Status',
        'id_col': 'ID',
        'country_col': 'Country'
    }

    return column_dict

@pytest.fixture
def accepted_countries():
    return ['United States', 'Puerto Rico']


def test_load_data(raw_test_data, column_headers):
    temp_data = response_data(id_column=column_headers['id_col'])
    assert (temp_data.columns[:10] == raw_test_data.columns[:10]).all(), 'File is no Alchemer response file - FAILED'

def test_preprocess_data_clean(raw_test_data, column_headers):
    intermediate_data = drop_incompletes(data=raw_test_data, status_col=column_headers['status_col'])
    assert intermediate_data[column_headers['status_col']].unique() == 'Complete', 'Respondents found with ' \
                                                                                   'incomplete submission - FAILED'

# Dear Candidate, please change this file as much as you like. We have left a few example test functions here which are by all means not perfect but to give you an idea of what we kind of are looking for. Code away and good luck !
