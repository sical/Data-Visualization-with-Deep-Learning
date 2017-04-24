import argparse 
import tensorflow as tf
import numpy as np
from PIL import Image

def main(_):
    print('lalalal')
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

def go(typ, image):
    print("laalalalala")
    graph = load_graph('graph/output_graph.pb')
    
    # We access the input and output nodes
    input = graph.get_tensor_by_name('prefix/DecodeJpeg:0')
    output = graph.get_tensor_by_name('prefix/final_result:0')
    image = Image.open(image)
    image_array = None
    if typ == 'jpg':
        image_array = np.array(image)
    else:
        image_array = np.array(image)[:, :, 0:3]  # Select RGB channels only.

    with tf.Session(graph=graph) as sess:
        result = sess.run(output, feed_dict={
            input: image_array
        })

        datatemp = {
                'message': 'Model trained',
                'result': [
                    {
                        'prediction': [
                            {
                                'label':        'Bar Chart',
                                "probability":  """ + result[3] + """,
                            },
                            {
                                'label':        'Line Chart',
                                "probability":  """ + result[1] + """,
                            },
                            {
                                'label':        'Pie chart',
                                'probability':  """ + result[2] + """,
                            },
                            {
                                'label':        'Scatter plot',
                                'probability':  """ + result[0] + """,
                            },
                        ],
                        'file':'image.jpg'
                    }
                ]
            }
        print(json.dumps(datatemp))
    return json.dumps(datatemp)


if __name__ == '__main__':
    # Let's allow the user to pass the filename as an argument
    parser = argparse.ArgumentParser()
    parser.add_argument("--frozen_model_filename", default="graph.pb", type=str, help="Frozen model file to import")
    args = parser.parse_args()
    


