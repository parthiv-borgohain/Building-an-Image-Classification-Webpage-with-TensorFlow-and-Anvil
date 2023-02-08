# Building an Image Classification Webpage with TensorFlow and Anvil

Coursework for Optimization II Class

### About the Project:

In this project, I built an interactive webpage to present my work on creating a neural network that achieved greater than 99% accuracy on the MNIST dataset. The goal of the project was to find the best network structure that would result in high accuracy on the MNIST dataset. I tried different approaches such as using multiple convolutional layers, different filter sizes, different number of filters, multiple max pool layers, several dense layers, regularizers, dropout layers, different batch sizes, or number of epochs. In the end, I found a network structure that gave me more than 99% accuracy on the validation set and then trained the network on the entire training set. I also tested the network on the MNIST test set and plotted a few of the numbers that were misclassified.

To present my work, I built an interactive webpage using Anvil, an online service that allows for easy web page creation through dragging and dropping components. The webpage described my process, the network structure I used, what worked well and what didn't, and allowed visitors to upload a CSV file with the pixel intensities of a 28x28 image. The webpage would then display the image and call my TensorFlow model to classify the image.

Anvil and TensorFlow do not work together, so I used Anvil's Uplink feature to allow my Python function to sit on another computer and be called from the Anvil page. This allowed me to classify an image using my neural network on my computer and have the webpage send the image to my computer, which then returned the classification to the page.

The URL to my webpage and the link to clone my page were submitted as the final product of this project.

URL to Webpage: https://msbaoptim43.anvil.app 

**Note:** Username is: Dan, Password is: Optimization1234. Please do note that the CNN Model is deployed on AWS Lightsail. The digit classification feature may not work if the Lightsail Instance is offline
