import json
from pathlib import Path
from typing import Any, Dict, Iterable, Union

import pandas as pd
from pandas.io.json import json_normalize


SAMPLE_TEXT = {
    'date': '2019-12-23',
    'company': 'ABC corp',
    'data': [
        {
            'name': 'person_1',
            'address': '123 Blue Street',
            'phone': [
                {
                    'home': '555.123.456',
                    'mobile': '555.111.222',
                },
            ],
        },
        {
            'name': 'person_2',
            'address': '987 Green Street',
            'phone': [
                {
                    'home': '333.123.456',
                    'mobile': '333.111.222',
                },
            ],
        },
    ]
}


def write_json(des: Path):
    """
    Write a JSON file.

    :param des: destination file path
    """
    with des.open('w') as f:
        json.dump(SAMPLE_TEXT, f)


def load_json(src: Path) -> Dict[Any, Any]:
    """
    Load data from a JSON file.

    :param src: source file path
    :return:
    """
    with src.open('r') as f:
        return json.load(f)


def load_json_pandas_flat(src: Path) -> pd.DataFrame:
    """
    Load flat and nested data from a JSON file into a Pandas data frame.

    :param src: source file path
    :return: data portion of JSON file

    .. note:: The nested data will be a list. To create a data frame of the \
        nested data see the function `load_json_pandas_2`.
    """
    data = load_json(src)
    return json_normalize(data)


def load_json_pandas_nested(src: Path,
                            nested: Union[str, Iterable[str]],
                            flat_data: Union[str, Iterable[str]],
                            ) -> pd.DataFrame:
    """
    Load nested data from a JSON file into a Pandas data frame.

    :param src: source file path
    :param nested: key name or path of key names for nested variable of JSON \
        file
    :param flat_data: flat data to be included
    :return: nested portion of JSON file
    """
    nested = [nested] if isinstance(nested, str) else nested
    flat_data = [flat_data] if isinstance(flat_data, str) else flat_data
    data = load_json(src)
    return json_normalize(data, record_path=nested, meta=flat_data)


if __name__ == '__main__':
    p = Path('junk.json')
    write_json(p)
    json_data = load_json(p)
    flat_df = load_json_pandas_flat(p)
    single_nested_df = load_json_pandas_nested(p, 'data', ['date', 'company'])
    double_nested_df = load_json_pandas_nested(p, ['data', 'phone'],
                                               ['date', 'company'])
