from __future__ import print_function
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os
from time import time
from openvino.inference_engine import IENetwork, IEPlugin
import openvino as ov


def display_comparewriter(our_image, prediction):
    plt.title('Prediction: {0:.0f}'.format(prediction))
    plt.imshow(our_image.reshape([28, 28]), cmap=plt.get_cmap('gray_r'))
    plt.show()


def main():

    model_xml = 'models' + os.sep + 'my_CNNmodel.h5.xml'
    model_bin = 'models' + os.sep + 'my_CNNmodel.h5.bin'
    plugin_dir = None
    inputdata = 'test.png'
    number_top = 1
    #hw_device: 'CPU', 'GPU', 'FPGA', 'HETERO:FPGA,GPU,CPU'
    hw_device = 'CPU'

    # Plugin initialization for specified device and load extensions library if specified
    plugin = IEPlugin(device=hw_device, plugin_dirs=plugin_dir)

    #print("Adding CPU extenstions...")
    #plugin.add_cpu_extension("/opt/intel/computer_vision_sdk_2018.3.343/deployment_tools/inference_engine/lib/ubuntu_16.04/intel64/libcpu_extension_sse4.so")

    # Read IR
    net = IENetwork.from_ir(model=model_xml, weights=model_bin)

    input_blob = next(iter(net.inputs))
    #activation_1/Softmax
    out_blob = next(iter(net.outputs))
    net.batch_size = 1

    #samples, channels, high, wide
    n, c, h, w = net.inputs[input_blob]

    #Open the data you wrote
    im = Image.open(inputdata)
    #normalized
    im = im.convert('1')
    writetmp = np.array(im.getdata())
    writetmp = (255 - writetmp) / 255
    images = writetmp.reshape(n, c, h, w)

    # Loading model to the plugin
    exec_net = plugin.load(network=net)
    del net

    for tmpi in range(10):
        # Start sync inference
        infer_time = []
        t0 = time()
        res = exec_net.infer(inputs={input_blob: images})
        infer_time.append((time() - t0) * 1000)
        print("The running time of one iteration: {} ms".format(
            np.average(np.asarray(infer_time))))


    if hw_device == 'CPU':
        perf_counts = exec_net.requests[0].get_perf_counts()
        print("Performance counters:")
        print("{:<35} {:<15} {:<15} {:<15} {:<10} {:<10}".format(
            'name', 'layer_type', 'exet_type', 'status', 'real_time',
            'cpu_time, us'))

        for layer, stats in perf_counts.items():
            print("{:<35} {:<15} {:<15} {:<15} {:<10} {:<10}".format(
                layer, stats['layer_type'], stats['exec_type'], stats['status'],
                stats['real_time'], stats['cpu_time']))


    # Processing output blob
    res = res[out_blob]

    the_results = np.ndarray(shape=(n))

    for i, probs in enumerate(res):
        probs = np.squeeze(probs)
        top_ind = np.argsort(probs)[-number_top:][::-1]
        the_results[i] = top_ind[0]

    del exec_net
    del plugin

    print("The prediction result is: {}".format(int(the_results[0])))

    display_comparewriter(images, the_results[0])


if __name__ == '__main__':
    main()
