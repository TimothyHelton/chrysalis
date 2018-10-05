## Add Tensorflow Object Detection API

### Set the environment variable PYTHONPATH in the Dockerfile.


### Console
1. Preferences
1. Build, Execution, Deployment
1. Console
1. Python Console
1. Environment Variables

`PYTHONPATH=$PYTHONPATH:/opt/models/research:/opt/models/research/slim:/opt/models/research/object_detection`


### Run/Debug Configuration
1. Edit Configurations...
1. Python
    1. Environment Variables
1. pytest
    1. Environment Variables

`PYTHONPATH=$PYTHONPATH:/opt/models/research:/opt/models/research/slim:/opt/models/research/object_detection`


### Editor
1. Clone the TensorFlow models repository into the /opt directory.

    `git clone git@github.com:tensorflow/models.git /opt`

1. Create a soft link to the TensorFlow models directory in the project directory.

    `ln -s /opt/models`

1. Set the research and object detection directories as `Sources Root`.