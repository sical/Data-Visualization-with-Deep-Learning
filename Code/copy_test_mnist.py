
from tensorflow.examples.tutorials.mnist import input_data # importe les données mnist (data)
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True) # lit les données importées

import tensorflow as tf # utilisation de la librairie tensorflow
x = tf.placeholder(tf.float32, [None, 784]) # crée un tableau dynamique (placeholder), en 2D, une qui va bouger au fil de l'apprentissage, et une autre de 784, correspondant aux pixels de l'image. 


W = tf.Variable(tf.zeros([784, 10])) # initialisation des poids à zéro pour chaque pixels, et pour 10 choix possibles
b = tf.Variable(tf.zeros([10])) # initialisation des biais pour les 10 choix possibles.




