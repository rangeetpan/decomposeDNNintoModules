#!/bin/sh
# Ask the experiments
echo "Please choose the correct option for the experiment"
echo "1- MNIST Intra Replacement"
echo "2- FMNIST Intra Replacement"
echo "3- KMNIST Intra Replacement"
echo "4- EMNIST Intra Replacement"
echo "5- MNIST-EMNIST Inter Replacement"
echo "6- MNIST-KMNIST Inter Replacement"
read varexperiment
# Approach 1
if [ "$varexperiment" = "1" ]
then cd '../Replacement/MNIST' && python 'Reuse.py'
fi
if [ "$varexperiment" = "2" ]
then cd '../Replacement/FMNIST' && python 'Reuse.py'
fi
if [ "$varexperiment" = "3" ]
then cd '../Replacement/KMNIST' && python 'Reuse.py'
fi
if [ "$varexperiment" = "4" ]
then cd '../Replacement/EMNIST' && python 'Reuse.py'
fi
if [ "$varexperiment" = "5" ]
then cd '../Replacement/MNISTEMNIST' && python 'Reuse.py' && python 'trainModel.py'
fi
if [ "$varexperiment" = "6" ]
then cd '../Replacement/MNISTKMNIST' && python 'Reuse.py' && python 'trainModel.py'
fi
