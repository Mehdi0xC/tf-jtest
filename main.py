import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import tensorflow as tf
# check cuda availability for tensorflow
print("Tensorflow version: ", tf.__version__)
print("Is CUDA available: ", tf.test.is_built_with_cuda())
print("Available GPUs: ", tf.config.list_physical_devices('GPU'))
