import argparse 
import tensorflow as tf
import numpy as np
from PIL import Image

def main(_):
    go('jpg','pic_007.jpg')

def load_graph(frozen_graph_filename):
    # We load the protobuf file from the disk and parse it to retrieve the 
    # unserialized graph_def
    with tf.gfile.GFile(frozen_graph_filename, "rb") as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())

    # Then, we can use again a convenient built-in function to import a graph_def into the 
    # current default Graph
    with tf.Graph().as_default() as graph:
        tf.import_graph_def(
            graph_def, 
            input_map=None, 
            return_elements=None, 
            name="prefix", 
            op_dict=None, 
            producer_op_list=None
        )
    return graph

def go(typ,imgpath):
    png_data = tf.placeholder(tf.string, shape=[])
    decoded_png = tf.image.decode_png(png_data, channels=3)

    # We use our "load_graph" function
    graph = load_graph(args.frozen_model_filename)

    # We can verify that we can access the list of operations in the graph
    for op in graph.get_operations():
        print(op.name)
        # prefix/Placeholder/inputs_placeholder
        # ...
        # prefix/Accuracy/predictions
        
    # We access the input and output nodes 
    x = graph.get_tensor_by_name('prefix/DecodeJpeg:0')
    y = graph.get_tensor_by_name('prefix/final_result:0')


    image = Image.open(imgpath)
    image_array=None
    if typ == 'jpg':
        image_array = np.array(image)
    else:
         image_array = np.array(image)[:, :, 0:3]  # Select RGB channels only.

    with tf.Session(graph=graph) as sess:
        y_out = sess.run(y, feed_dict={
          x : image_array
        })
        print(y_out)
        print(max(max(y_out)))



if __name__ == '__main__':
    # Let's allow the user to pass the filename as an argument
    parser = argparse.ArgumentParser()
    parser.add_argument("--frozen_model_filename", default="graph.pb", type=str, help="Frozen model file to import")
    args = parser.parse_args()
    


