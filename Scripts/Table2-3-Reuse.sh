#!/bin/sh
# Ask the experiments
echo "Please choose the correct option for the experiment"
echo "1- MNIST Intra Reuse"
echo "2- FMNIST Intra Reuse"
echo "3- KMNIST Intra Reuse"
echo "4- EMNIST Intra Reuse"
echo "5- MNIST-EMNIST Inter Reuse"
echo "6- MNIST-KMNIST Inter Reuse"
read varexperiment
# Approach 1
if [ "$varexperiment" = "1" ]
then cd '../Reuse/MNIST' && python 'Reuse.py' && python 'trainModel.py'
fi
if [ "$varexperiment" = "2" ]
then cd '../Reuse/FMNIST' && python 'Reuse.py' && python 'trainModel.py'
fi
if [ "$varexperiment" = "3" ]
then cd '../Reuse/KMNIST' && python 'Reuse.py' && python 'trainModel.py'
fi
if [ "$varexperiment" = "4" ]
then cd '../Reuse/EMNIST' && python 'Reuse.py' && python 'trainModel.py'
fi
if [ "$varexperiment" = "5" ]
then cd '../Reuse/MNISTEMNIST' && python 'Reuse.py' && python 'trainModel.py'
fi
if [ "$varexperiment" = "6" ]
then cd '../Reuse/KMNISTMNIST' && python 'Reuse.py' && python 'trainModel.py'
fi
