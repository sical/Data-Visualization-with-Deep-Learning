# Data-Visualization-with-Deep-Learning

The aim of this project is to explore the possibilities the deep learning can offer to the data visualization domain.

## Using and understanding tensorFlow 

First of all , we choose tensorFlow API to build and train neuronal networks because :

  - This allows us to code in python a language we are familiar to.

  - TensorFlow is quite fast and can be used with a GPU to run even faster.A GPU can handle large amounts of data in many streams, performing relatively simple operations which is excatly what we do. (we went from 260 ms to 8 ms on convolutional.py)

  - Tensor flow has a great and active community and a lot of documentation which help develop faster.
 
 > tutorials available here https://www.tensorflow.org/tutorials/ .

### Installation

### firstStepMNIST.py

firstStepMnist.py is a script provided by tensorflow as a demo  and learning support.
   > This script comes with an explanation available here https://www.tensorflow.org/tutorials/mnist/beginners/
 
 To sum up, this script is a basic machine learning program "hello world" like. But, however it allows to understand how 
it works.

First of all, the script downloads the data set and divides it to use it efficiently. A neuronal network must never learn from validation and test data. This will make	laborious the study of any result as there will be no tracks. It may also interfer with the trainning sessions (especially if you are using the deep learning for classification and test it on pictures out of output possibilities).

  Once you have the right dataset, the next steps is modelization. The modelization can be divided in 3 parts:
  
  - Input and Output modelization must be choosen wisely as it will affect the structure of the neuronal network.
  
  - The loss modelization can be summarized in a function representing the loss to determine if the trainnig was efficient.
  
  - The test modelization is the function that we will use to train the algorithm in order to reduce the loss.


