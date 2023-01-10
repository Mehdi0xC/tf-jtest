import tensorflow as tf
# check cuda availability for tensorflow
print("Tensorflow version: ", tf.__version__)
print("Is CUDA available: ", tf.test.is_built_with_cuda())
print("Is GPU available: ", tf.test.is_gpu_available(cuda_only=True))

