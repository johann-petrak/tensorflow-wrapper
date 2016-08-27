from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
import os.path

# create a dense neural networ with the vector vnrhidden
# giving the number of hidden units for each layer, starting from the input.
# The output is represented by a softwax layer for the given number of classes
def classification(vnrhidden=[100],nrclasses=2):
  import tensorflow as tf
  in = tf.placeholder('float',None) # allow any size, but only one dimension
  ## create a simple 
   
