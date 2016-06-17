import pytest
import corna.helpers as help
import pandas as pd

def test_get_atomic_weight():
    assert help.get_atomic_weight('Al') == 26.981538

def test_get_atomic_weight_wildcard():
    with pytest.raises(KeyError) as err:
        help.get_atomic_weight('R')
    assert err.value.message == 'Element doesnt exist'

def test_get_isotope_details():
    assert help.get_isotope('C13') == {'NA':0.0107, 'mol_mass':13.0033548378, 'nat_form':'C12'}

def test_get_isotope_na():
    assert help.get_isotope_na('C13') == 0.0107

def	test_get_isotope_mass():
    assert help.get_isotope_mass('C13') == 13.0033548378

def test_get_isotope_natural():
    assert help.get_isotope_natural('C13') == 'C12'

def test_get_isotope_keyerror():
    with pytest.raises(KeyError) as err:
        help.get_isotope('Ind5')
    assert err.value.args == ('Check available isotope list', 'Ind5')

def test_label_dict_to_key():
    assert help.label_dict_to_key({'C13':2, 'N14':4}) == 'N14_4_C13_2'

def test_read_file():
	path = 'incorrectpath.xlsx'
	with pytest.raises(IOError):
		file_in = help.read_file(path)

def test_read_file_ext():
	path = 'no_or_invalid_extension'
	with pytest.raises(IOError):
		file_in = help.read_file(path)

def test_filter_df():
	df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [2, 2, 2]})
	with pytest.raises(KeyError):
		filter_df = help.filter_df(df, 'col_1', 10)

def test_create_dict_from_isotope_label_list():
    assert help.create_dict_from_isotope_label_list(['C13',2,'N15',5]) == {'C13': 2, 'N15': 5}

def test_create_dict_from_isotope_label_list_missing_number():
    with pytest.raises(ValueError) as err:
        help.create_dict_from_isotope_label_list(['C13','N15',5])
    assert err.value.message == 'The number of labels should be integer'

def test_create_dict_from_isotope_label_list_no_isotope():
    with pytest.raises(KeyError) as err:
        help. create_dict_from_isotope_label_list([6, 'C13','N15',5])
    assert err.value.message == 'The key must be an isotope'

def test_get_key_from_single_value_dict():
    assert help.get_key_from_single_value_dict({'C13':1}) == 'C13'

def test_get_value_from_single_value_dict():
    assert help.get_value_from_single_value_dict({'C13':1}) == 1

def test_get_key_from_single_value_dict_len_error():
    with pytest.raises(OverflowError):
        help.get_key_from_single_value_dict({'C13':1, 'C14':2})


