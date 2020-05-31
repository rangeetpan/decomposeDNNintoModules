#!/bin/sh
# Ask the experiments
echo "Please choose the correct option for the experiment"
echo "1- Tangling Identification: Imbalance (TI-I)"
echo "2- Tangling Identification: Punish Negative Examples (TI-PN)"
echo "3- Tangling Identification: Higher Priority to Negative Examples (TI- HP)"
echo "4- Tangling Identification: Strong Negative Edges (TI-SNE)"
echo "5- Concern Modularization: Channeling (CM-C)"
echo "6- Concern Modularization: Remove Irrelevant Edges (CM-RIE)"
read varexperiment
echo "Please choose the correct dataset"
echo "1- MNIST"
echo "2- Extended MNIST (EMNIST)"
echo "3- Fashion MNIST (FMNIST)"
echo "4- Kuzushiji MNIST (KMNIST)"
read vardataset
echo "Please choose the correct model structure"
echo "1- One hidden layer"
echo "2- Two hidden layers"
echo "3- Three hidden layers"
echo "4- Four hidden layers"
read varmodel
# Approach 1
if [ "$varexperiment" = "1" ] && [ "$vardataset" = "1" ] && [ "$varmodel" = "1" ]
then cd '../Approach 1 (TI-I)/MNIST/MNIST-1' && python 'Reuse.py'
fi
if [ "$varexperiment" = "1" ] && [ "$vardataset" = "1" ] && [ "$varmodel" = "2" ]
then cd '../Approach 1 (TI-I)/MNIST/MNIST-2' && python 'Reuse.py'
fi
if [ "$varexperiment" = "1" ] && [ "$vardataset" = "1" ] && [ "$varmodel" = "3" ]
then cd '../Approach 1 (TI-I)/MNIST/MNIST-3' && python 'Reuse.py'
fi
if [ "$varexperiment" = "1" ] && [ "$vardataset" = "1" ] && [ "$varmodel" = "4" ]
then cd '../Approach 1 (TI-I)/MNIST/MNIST-4' && python 'Reuse.py'
fi

if [ "$varexperiment" = "1" ] && [ "$vardataset" = "2" ] && [ "$varmodel" = "1" ]
then cd '../Approach 1 (TI-I)/EMNIST/EMNIST-1' && python 'Reuse.py'
fi
if [ "$varexperiment" = "1" ] && [ "$vardataset" = "2" ] && [ "$varmodel" = "2" ]
then cd '../Approach 1 (TI-I)/EMNIST/EMNIST-2' && python 'Reuse.py'
fi
if [ "$varexperiment" = "1" ] && [ "$vardataset" = "2" ] && [ "$varmodel" = "3" ]
then cd '../Approach 1 (TI-I)/EMNIST/EMNIST-3' && python 'Reuse.py'
fi
if [ "$varexperiment" = "1" ] && [ "$vardataset" = "2" ] && [ "$varmodel" = "4" ]
then cd '../Approach 1 (TI-I)/EMNIST/EMNIST-4' && python 'Reuse.py'
fi

if [ "$varexperiment" = "1" ] && [ "$vardataset" = "3" ] && [ "$varmodel" = "1" ]
then cd '../Approach 1 (TI-I)/FMNIST/FMNIST-1' && python 'Reuse.py'
fi
if [ "$varexperiment" = "1" ] && [ "$vardataset" = "3" ] && [ "$varmodel" = "2" ]
then cd '../Approach 1 (TI-I)/FMNIST/FMNIST-2' && python 'Reuse.py'
fi
if [ "$varexperiment" = "1" ] && [ "$vardataset" = "3" ] && [ "$varmodel" = "3" ]
then cd '../Approach 1 (TI-I)/FMNIST/FMNIST-3' && python 'Reuse.py'
fi
if [ "$varexperiment" = "1" ] && [ "$vardataset" = "3" ] && [ "$varmodel" = "4" ]
then cd '../Approach 1 (TI-I)/FMNIST/FMNIST-4' && python 'Reuse.py'
fi

if [ "$varexperiment" = "1" ] && [ "$vardataset" = "4" ] && [ "$varmodel" = "1" ]
then cd '../Approach 1 (TI-I)/KMNIST/KMNIST-1' && python 'Reuse.py'
fi
if [ "$varexperiment" = "1" ] && [ "$vardataset" = "4" ] && [ "$varmodel" = "2" ]
then cd '../Approach 1 (TI-I)/KMNIST/KMNIST-2' && python 'Reuse.py'
fi
if [ "$varexperiment" = "1" ] && [ "$vardataset" = "4" ] && [ "$varmodel" = "3" ]
then cd '../Approach 1 (TI-I)/KMNIST/KMNIST-3' && python 'Reuse.py'
fi
if [ "$varexperiment" = "1" ] && [ "$vardataset" = "4" ] && [ "$varmodel" = "4" ]
then cd '../Approach 1 (TI-I)/KMNIST/KMNIST-4' && python 'Reuse.py'
fi


# Approach 2
if [ "$varexperiment" = "2" ] && [ "$vardataset" = "1" ] && [ "$varmodel" = "1" ]
then cd '../Approach 2 (TI-PN)/MNIST/MNIST-1' && python 'Reuse.py'
fi
if [ "$varexperiment" = "2" ] && [ "$vardataset" = "1" ] && [ "$varmodel" = "2" ]
then cd '../Approach 2 (TI-PN)/MNIST/MNIST-2' && python 'Reuse.py'
fi
if [ "$varexperiment" = "2" ] && [ "$vardataset" = "1" ] && [ "$varmodel" = "3" ]
then cd '../Approach 2 (TI-PN)/MNIST/MNIST-3' && python 'Reuse.py'
fi
if [ "$varexperiment" = "2" ] && [ "$vardataset" = "1" ] && [ "$varmodel" = "4" ]
then cd '../Approach 2 (TI-PN)/MNIST/MNIST-4' && python 'Reuse.py'
fi

if [ "$varexperiment" = "2" ] && [ "$vardataset" = "2" ] && [ "$varmodel" = "1" ]
then cd '../Approach 2 (TI-PN)/EMNIST/EMNIST-1' && python 'Reuse.py'
fi
if [ "$varexperiment" = "2" ] && [ "$vardataset" = "2" ] && [ "$varmodel" = "2" ]
then cd '../Approach 2 (TI-PN)/EMNIST/EMNIST-2' && python 'Reuse.py'
fi
if [ "$varexperiment" = "2" ] && [ "$vardataset" = "2" ] && [ "$varmodel" = "3" ]
then cd '../Approach 2 (TI-PN)/EMNIST/EMNIST-3' && python 'Reuse.py'
fi
if [ "$varexperiment" = "2" ] && [ "$vardataset" = "2" ] && [ "$varmodel" = "4" ]
then cd '../Approach 2 (TI-PN)/EMNIST/EMNIST-4' && python 'Reuse.py'
fi

if [ "$varexperiment" = "2" ] && [ "$vardataset" = "3" ] && [ "$varmodel" = "1" ]
then cd '../Approach 2 (TI-PN)/FMNIST/FMNIST-1' && python 'Reuse.py'
fi
if [ "$varexperiment" = "2" ] && [ "$vardataset" = "3" ] && [ "$varmodel" = "2" ]
then cd '../Approach 2 (TI-PN)/FMNIST/FMNIST-2' && python 'Reuse.py'
fi
if [ "$varexperiment" = "2" ] && [ "$vardataset" = "3" ] && [ "$varmodel" = "3" ]
then cd '../Approach 2 (TI-PN)/FMNIST/FMNIST-3' && python 'Reuse.py'
fi
if [ "$varexperiment" = "2" ] && [ "$vardataset" = "3" ] && [ "$varmodel" = "4" ]
then cd '../Approach 2 (TI-PN)/FMNIST/FMNIST-4' && python 'Reuse.py'
fi

if [ "$varexperiment" = "2" ] && [ "$vardataset" = "4" ] && [ "$varmodel" = "1" ]
then cd '../Approach 2 (TI-PN)/KMNIST/KMNIST-1' && python 'Reuse.py'
fi
if [ "$varexperiment" = "2" ] && [ "$vardataset" = "4" ] && [ "$varmodel" = "2" ]
then cd '../Approach 2 (TI-PN)/KMNIST/KMNIST-2' && python 'Reuse.py'
fi
if [ "$varexperiment" = "2" ] && [ "$vardataset" = "4" ] && [ "$varmodel" = "3" ]
then cd '../Approach 2 (TI-PN)/KMNIST/KMNIST-3' && python 'Reuse.py'
fi
if [ "$varexperiment" = "2" ] && [ "$vardataset" = "4" ] && [ "$varmodel" = "4" ]
then cd '../Approach 2 (TI-PN)/KMNIST/KMNIST-4' && python 'Reuse.py'
fi

# Approach 3
if [ "$varexperiment" = "3" ] && [ "$vardataset" = "1" ] && [ "$varmodel" = "1" ]
then cd '../Approach 3 (TI-HP)/MNIST/MNIST-1' && python 'Reuse.py'
fi
if [ "$varexperiment" = "3" ] && [ "$vardataset" = "1" ] && [ "$varmodel" = "2" ]
then cd '../Approach 3 (TI-HP)/MNIST/MNIST-2' && python 'Reuse.py'
fi
if [ "$varexperiment" = "3" ] && [ "$vardataset" = "1" ] && [ "$varmodel" = "3" ]
then cd '../Approach 3 (TI-HP)/MNIST/MNIST-3' && python 'Reuse.py'
fi
if [ "$varexperiment" = "3" ] && [ "$vardataset" = "1" ] && [ "$varmodel" = "4" ]
then cd '../Approach 3 (TI-HP)/MNIST/MNIST-4' && python 'Reuse.py'
fi

if [ "$varexperiment" = "3" ] && [ "$vardataset" = "2" ] && [ "$varmodel" = "1" ]
then cd '../Approach 3 (TI-HP)/EMNIST/EMNIST-1' && python 'Reuse.py'
fi
if [ "$varexperiment" = "3" ] && [ "$vardataset" = "2" ] && [ "$varmodel" = "2" ]
then cd '../Approach 3 (TI-HP)/EMNIST/EMNIST-2' && python 'Reuse.py'
fi
if [ "$varexperiment" = "3" ] && [ "$vardataset" = "2" ] && [ "$varmodel" = "3" ]
then cd '../Approach 3 (TI-HP)/EMNIST/EMNIST-3' && python 'Reuse.py'
fi
if [ "$varexperiment" = "3" ] && [ "$vardataset" = "2" ] && [ "$varmodel" = "4" ]
then cd '../Approach 3 (TI-HP)/EMNIST/EMNIST-4' && python 'Reuse.py'
fi

if [ "$varexperiment" = "3" ] && [ "$vardataset" = "3" ] && [ "$varmodel" = "1" ]
then cd '../Approach 3 (TI-HP)/FMNIST/FMNIST-1' && python 'Reuse.py'
fi
if [ "$varexperiment" = "3" ] && [ "$vardataset" = "3" ] && [ "$varmodel" = "2" ]
then cd '../Approach 3 (TI-HP)/FMNIST/FMNIST-2' && python 'Reuse.py'
fi
if [ "$varexperiment" = "3" ] && [ "$vardataset" = "3" ] && [ "$varmodel" = "3" ]
then cd '../Approach 3 (TI-HP)/FMNIST/FMNIST-3' && python 'Reuse.py'
fi
if [ "$varexperiment" = "3" ] && [ "$vardataset" = "3" ] && [ "$varmodel" = "4" ]
then cd '../Approach 3 (TI-HP)/FMNIST/FMNIST-4' && python 'Reuse.py'
fi

if [ "$varexperiment" = "3" ] && [ "$vardataset" = "4" ] && [ "$varmodel" = "1" ]
then cd '../Approach 3 (TI-HP)/KMNIST/KMNIST-1' && python 'Reuse.py'
fi
if [ "$varexperiment" = "3" ] && [ "$vardataset" = "4" ] && [ "$varmodel" = "2" ]
then cd '../Approach 3 (TI-HP)/KMNIST/KMNIST-2' && python 'Reuse.py'
fi
if [ "$varexperiment" = "3" ] && [ "$vardataset" = "4" ] && [ "$varmodel" = "3" ]
then cd '../Approach 3 (TI-HP)/KMNIST/KMNIST-3' && python 'Reuse.py'
fi
if [ "$varexperiment" = "3" ] && [ "$vardataset" = "4" ] && [ "$varmodel" = "4" ]
then cd '../Approach 3 (TI-HP)/KMNIST/KMNIST-4' && python 'Reuse.py'
fi


# Approach 4
if [ "$varexperiment" = "4" ] && [ "$vardataset" = "1" ] && [ "$varmodel" = "1" ]
then cd '../Approach 4 (TI-SNE)/MNIST/MNIST-1' && python 'Reuse.py'
fi
if [ "$varexperiment" = "4" ] && [ "$vardataset" = "1" ] && [ "$varmodel" = "2" ]
then cd '../Approach 4 (TI-SNE)/MNIST/MNIST-2' && python 'Reuse.py'
fi
if [ "$varexperiment" = "4" ] && [ "$vardataset" = "1" ] && [ "$varmodel" = "3" ]
then cd '../Approach 4 (TI-SNE)/MNIST/MNIST-3' && python 'Reuse.py'
fi
if [ "$varexperiment" = "4" ] && [ "$vardataset" = "1" ] && [ "$varmodel" = "4" ]
then cd '../Approach 4 (TI-SNE)/MNIST/MNIST-4' && python 'Reuse.py'
fi

if [ "$varexperiment" = "4" ] && [ "$vardataset" = "2" ] && [ "$varmodel" = "1" ]
then cd '../Approach 4 (TI-SNE)/EMNIST/EMNIST-1' && python 'Reuse.py'
fi
if [ "$varexperiment" = "4" ] && [ "$vardataset" = "2" ] && [ "$varmodel" = "2" ]
then cd '../Approach 4 (TI-SNE)/EMNIST/EMNIST-2' && python 'Reuse.py'
fi
if [ "$varexperiment" = "4" ] && [ "$vardataset" = "2" ] && [ "$varmodel" = "3" ]
then cd '../Approach 4 (TI-SNE)/EMNIST/EMNIST-3' && python 'Reuse.py'
fi
if [ "$varexperiment" = "4" ] && [ "$vardataset" = "2" ] && [ "$varmodel" = "4" ]
then cd '../Approach 4 (TI-SNE)/EMNIST/EMNIST-4' && python 'Reuse.py'
fi

if [ "$varexperiment" = "4" ] && [ "$vardataset" = "3" ] && [ "$varmodel" = "1" ]
then cd '../Approach 4 (TI-SNE)/FMNIST/FMNIST-1' && python 'Reuse.py'
fi
if [ "$varexperiment" = "4" ] && [ "$vardataset" = "3" ] && [ "$varmodel" = "2" ]
then cd '../Approach 4 (TI-SNE)/FMNIST/FMNIST-2' && python 'Reuse.py'
fi
if [ "$varexperiment" = "4" ] && [ "$vardataset" = "3" ] && [ "$varmodel" = "3" ]
then cd '../Approach 4 (TI-SNE)/FMNIST/FMNIST-3' && python 'Reuse.py'
fi
if [ "$varexperiment" = "4" ] && [ "$vardataset" = "3" ] && [ "$varmodel" = "4" ]
then cd '../Approach 4 (TI-SNE)/FMNIST/FMNIST-4' && python 'Reuse.py'
fi

if [ "$varexperiment" = "4" ] && [ "$vardataset" = "4" ] && [ "$varmodel" = "1" ]
then cd '../Approach 4 (TI-SNE)/KMNIST/KMNIST-1' && python 'Reuse.py'
fi
if [ "$varexperiment" = "4" ] && [ "$vardataset" = "4" ] && [ "$varmodel" = "2" ]
then cd '../Approach 4 (TI-SNE)/KMNIST/KMNIST-2' && python 'Reuse.py'
fi
if [ "$varexperiment" = "4" ] && [ "$vardataset" = "4" ] && [ "$varmodel" = "3" ]
then cd '../Approach 4 (TI-SNE)/KMNIST/KMNIST-3' && python 'Reuse.py'
fi
if [ "$varexperiment" = "4" ] && [ "$vardataset" = "4" ] && [ "$varmodel" = "4" ]
then cd '../Approach 4 (TI-SNE)/KMNIST/KMNIST-4' && python 'Reuse.py'
fi

# Approach 5
if [ "$varexperiment" = "5" ] && [ "$vardataset" = "1" ] && [ "$varmodel" = "1" ]
then cd '../Approach 5 (CM-C)/MNIST/MNIST-1' && python 'Reuse.py'
fi
if [ "$varexperiment" = "5" ] && [ "$vardataset" = "1" ] && [ "$varmodel" = "2" ]
then cd '../Approach 5 (CM-C)/MNIST/MNIST-2' && python 'Reuse.py'
fi
if [ "$varexperiment" = "5" ] && [ "$vardataset" = "1" ] && [ "$varmodel" = "3" ]
then cd '../Approach 5 (CM-C)/MNIST/MNIST-3' && python 'Reuse.py'
fi
if [ "$varexperiment" = "5" ] && [ "$vardataset" = "1" ] && [ "$varmodel" = "4" ]
then cd '../Approach 5 (CM-C)/MNIST/MNIST-4' && python 'Reuse.py'
fi

if [ "$varexperiment" = "5" ] && [ "$vardataset" = "2" ] && [ "$varmodel" = "1" ]
then cd '../Approach 5 (CM-C)/EMNIST/EMNIST-1' && python 'Reuse.py'
fi
if [ "$varexperiment" = "5" ] && [ "$vardataset" = "2" ] && [ "$varmodel" = "2" ]
then cd '../Approach 5 (CM-C)/EMNIST/EMNIST-2' && python 'Reuse.py'
fi
if [ "$varexperiment" = "5" ] && [ "$vardataset" = "2" ] && [ "$varmodel" = "3" ]
then cd '../Approach 5 (CM-C)/EMNIST/EMNIST-3' && python 'Reuse.py'
fi
if [ "$varexperiment" = "5" ] && [ "$vardataset" = "2" ] && [ "$varmodel" = "4" ]
then cd '../Approach 5 (CM-C)/EMNIST/EMNIST-4' && python 'Reuse.py'
fi

if [ "$varexperiment" = "5" ] && [ "$vardataset" = "3" ] && [ "$varmodel" = "1" ]
then cd '../Approach 5 (CM-C)/FMNIST/FMNIST-1' && python 'Reuse.py'
fi
if [ "$varexperiment" = "5" ] && [ "$vardataset" = "3" ] && [ "$varmodel" = "2" ]
then cd '../Approach 5 (CM-C)/FMNIST/FMNIST-2' && python 'Reuse.py'
fi
if [ "$varexperiment" = "5" ] && [ "$vardataset" = "3" ] && [ "$varmodel" = "3" ]
then cd '../Approach 5 (CM-C)/FMNIST/FMNIST-3' && python 'Reuse.py'
fi
if [ "$varexperiment" = "5" ] && [ "$vardataset" = "3" ] && [ "$varmodel" = "4" ]
then cd '../Approach 5 (CM-C)/FMNIST/FMNIST-4' && python 'Reuse.py'
fi

if [ "$varexperiment" = "5" ] && [ "$vardataset" = "4" ] && [ "$varmodel" = "1" ]
then cd '../Approach 5 (CM-C)/KMNIST/KMNIST-1' && python 'Reuse.py'
fi
if [ "$varexperiment" = "5" ] && [ "$vardataset" = "4" ] && [ "$varmodel" = "2" ]
then cd '../Approach 5 (CM-C)/KMNIST/KMNIST-2' && python 'Reuse.py'
fi
if [ "$varexperiment" = "5" ] && [ "$vardataset" = "4" ] && [ "$varmodel" = "3" ]
then cd '../Approach 5 (CM-C)/KMNIST/KMNIST-3' && python 'Reuse.py'
fi
if [ "$varexperiment" = "5" ] && [ "$vardataset" = "4" ] && [ "$varmodel" = "4" ]
then cd '../Approach 5 (CM-C)/KMNIST/KMNIST-4' && python 'Reuse.py'
fi

# Approach 6
if [ "$varexperiment" = "6" ] && [ "$vardataset" = "1" ] && [ "$varmodel" = "1" ]
then cd '../Approach 6 (CM-RIE)/MNIST/MNIST-1' && python 'Reuse.py'
fi
if [ "$varexperiment" = "6" ] && [ "$vardataset" = "1" ] && [ "$varmodel" = "2" ]
then cd '../Approach 6 (CM-RIE)/MNIST/MNIST-2' && python 'Reuse.py'
fi
if [ "$varexperiment" = "6" ] && [ "$vardataset" = "1" ] && [ "$varmodel" = "3" ]
then cd '../Approach 6 (CM-RIE)/MNIST/MNIST-3' && python 'Reuse.py'
fi
if [ "$varexperiment" = "6" ] && [ "$vardataset" = "1" ] && [ "$varmodel" = "4" ]
then cd '../Approach 6 (CM-RIE)/MNIST/MNIST-4' && python 'Reuse.py'
fi

if [ "$varexperiment" = "6" ] && [ "$vardataset" = "2" ] && [ "$varmodel" = "1" ]
then cd '../Approach 6 (CM-RIE)/EMNIST/EMNIST-1' && python 'Reuse.py'
fi
if [ "$varexperiment" = "6" ] && [ "$vardataset" = "2" ] && [ "$varmodel" = "2" ]
then cd '../Approach 6 (CM-RIE)/EMNIST/EMNIST-2' && python 'Reuse.py'
fi
if [ "$varexperiment" = "6" ] && [ "$vardataset" = "2" ] && [ "$varmodel" = "3" ]
then cd '../Approach 6 (CM-RIE)/EMNIST/EMNIST-3' && python 'Reuse.py'
fi
if [ "$varexperiment" = "6" ] && [ "$vardataset" = "2" ] && [ "$varmodel" = "4" ]
then cd '../Approach 6 (CM-RIE)/EMNIST/EMNIST-4' && python 'Reuse.py'
fi

if [ "$varexperiment" = "6" ] && [ "$vardataset" = "3" ] && [ "$varmodel" = "1" ]
then cd '../Approach 6 (CM-RIE)/FMNIST/FMNIST-1' && python 'Reuse.py'
fi
if [ "$varexperiment" = "6" ] && [ "$vardataset" = "3" ] && [ "$varmodel" = "2" ]
then cd '../Approach 6 (CM-RIE)/FMNIST/FMNIST-2' && python 'Reuse.py'
fi
if [ "$varexperiment" = "6" ] && [ "$vardataset" = "3" ] && [ "$varmodel" = "3" ]
then cd '../Approach 6 (CM-RIE)/FMNIST/FMNIST-3' && python 'Reuse.py'
fi
if [ "$varexperiment" = "6" ] && [ "$vardataset" = "3" ] && [ "$varmodel" = "4" ]
then cd '../Approach 6 (CM-RIE)/FMNIST/FMNIST-4' && python 'Reuse.py'
fi

if [ "$varexperiment" = "6" ] && [ "$vardataset" = "4" ] && [ "$varmodel" = "1" ]
then cd '../Approach 6 (CM-RIE)/KMNIST/KMNIST-1' && python 'Reuse.py'
fi
if [ "$varexperiment" = "6" ] && [ "$vardataset" = "4" ] && [ "$varmodel" = "2" ]
then cd '../Approach 6 (CM-RIE)/KMNIST/KMNIST-2' && python 'Reuse.py'
fi
if [ "$varexperiment" = "6" ] && [ "$vardataset" = "4" ] && [ "$varmodel" = "3" ]
then cd '../Approach 6 (CM-RIE)/KMNIST/KMNIST-3' && python 'Reuse.py'
fi
if [ "$varexperiment" = "6" ] && [ "$vardataset" = "4" ] && [ "$varmodel" = "4" ]
then cd '../Approach 6 (CM-RIE)/KMNIST/KMNIST-4' && python 'Reuse.py'
fi
