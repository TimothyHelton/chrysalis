#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Test Configuration File

.. moduleauthor:: Timothy Helton <timothy.j.helton@gmail.com>
"""
from collections import namedtuple
import os
from pathlib import Path

from PIL import Image
import pytest
import tensorflow as tf
from object_detection.utils import dataset_util as du


Detect = namedtuple('Detect',
                    'path, x_min, x_max, y_min, y_max, class_name,class_id')


@pytest.fixture(scope='session')
def training_dataset(tmpdir_factory):
    data_dir = 'data'
    data_path = tmpdir_factory.mktemp(data_dir)
    label_path = data_path.join('label_map.pbtxt')
    label_path.write('item {\n  name: "cat"\n  id: 1\n}\n'
                     'item {\n  name: "dog"\n  id: 2\n}\n')

    def create_tf_example(det: Detect) -> tf.train.Example:
        """
        Create TensorFlow Example for detection.
        :param det: namedtuple describing the detection
        :return: TensorFlow Example of detection
        """
        im = Image.open(det.path)
        width, height = im.size
        filename = det.path.name.encode()
        encoded_image_data = None

        return tf.train.Example(features=tf.train.Features(feature={
            'image/height': du.int64_feature(height),
            'image/width': du.int64_feature(width),
            'image/filename': du.bytes_feature(filename),
            'image/source_id': du.bytes_feature(filename),
            # 'image/encoded': du.bytes_feature(encoded_image_data),
            'image/format': du.bytes_feature(det.path.suffix.encode()),
            'image/object/bbox/xmin': du.float_list_feature([det.x_min]),
            'image/object/bbox/xmax': du.float_list_feature([det.x_max]),
            'image/object/bbox/ymin': du.float_list_feature([det.y_min]),
            'image/object/bbox/ymax': du.float_list_feature([det.y_max]),
            'image/object/class/text': du.bytes_list_feature([det.class_name]),
            'image/object/class/label': du.int64_list_feature([det.class_id]),
        }))

    example = Path(os.sep, 'opt', 'models', 'research', 'object_detection',
                   'g3doc', 'img', 'example_cat.jpg')
    detection = Detect(example, 322, 1062, 174, 761, 'cat'.encode(), 1)

    record_filename = str(data_path.join('test.record')).encode()
    with tf.python_io.TFRecordWriter(record_filename) as writer:
        tf_example = create_tf_example(detection)
        writer.write(tf_example.SerializeToString())

    return Path(tmpdir_factory.getbasetemp(), data_dir)


if __name__ == '__main__':
    pass
