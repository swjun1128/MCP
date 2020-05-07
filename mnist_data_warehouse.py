#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 10:30:19 2019

@author: qq
"""

import glob
import csv
import numpy as np
import matplotlib.pyplot as plt
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

#['lsa','dsa','my','conditional','random']:


#1,2,5,10


dict_fgsm = {'my':[[0.8816,0.8774,0.8817,0.8813,0.8783],
[0.9043,0.8945,0.8984,0.9007,0.9039],
[0.9141,0.9126,0.9128,0.908,0.9153],
[0.9407,0.9422,0.9436,0.9394,0.9465]] ,  
            'my_optimize':[[0.8619,0.8589,0.8616,0.8631,0.8615],
[0.8868,0.8845,0.8877,0.891,0.8844],
[0.8934,0.8953,0.8955,0.8948,0.8935],
[0.9069,0.9087,0.9041,0.9114,0.9095]],       
             'lsa':[[0.7114,0.788,0.7583,0.7615,0.7354],
[0.8475,0.8692,0.8653,0.8657,0.8565],
[0.8926,0.891,0.9018,0.9014,0.8842],
[0.9343,0.925,0.9385,0.9347,0.9364]] , 
            'dsa':[[0.8755,0.8696,0.8654,0.8746,0.8738],
[0.9017,0.8984,0.894,0.9018,0.9021],
[0.9151,0.9255,0.9251,0.9209,0.9218],
[0.9553,0.9496,0.9477,0.9479,0.9491]     
                    ],
            'conditional':[[0.8623,0.8657,0.8522,0.8492,0.8815],
[0.8947,0.8862,0.8905,0.897,0.8879],
[0.9175,0.9156,0.9113,0.9114,0.9054],
[0.9276,0.9252,0.9291,0.931,0.9242]
                    ],
             'random':[[0.8648,0.8562,0.8608,0.8773,0.8662],
[0.8997,0.8994,0.8936,0.9005,0.8893],
[0.9001,0.9072,0.9022,0.9098,0.9071],
[0.9282,0.925,0.9279,0.9217,0.9243]] ,
             'adaptive':[[0.8823,0.8849,0.8811,0.8814,0.8819],
[0.9018,0.8978,0.8993,0.9052,0.8979],
[0.9134,0.9091,0.9092,0.9141,0.9142],
[0.9408,0.9459,0.9479,0.9494,0.9341]],
'original':0.823
}
   

dict_jsma = {'my':[[0.9366,0.9301,0.9374,0.9401,0.9367],
[0.9662,0.9641,0.9642,0.9635,0.9647],
[0.9681,0.968,0.9685,0.9662,0.9719],
[0.9795,0.9803,0.9785,0.9802,0.9782]] ,         
            'my_optimize':[[0.934,0.9309,0.9353,0.9317,0.9388],
[0.9572,0.9639,0.9614,0.9574,0.9634],
[0.967,0.9684,0.9687,0.9685,0.9659],
[0.9763,0.9788,0.9756,0.9792,0.9768]],  
             'lsa':[[0.9027,0.8979,0.9031,0.9029,0.8976],
[0.9354,0.9434,0.9318,0.9332,0.9379],
[0.9574,0.9601,0.9613,0.9619,0.9529],
[0.9733,0.9731,0.9731,0.9755,0.9703]] , 
            'dsa':[[0.9126,0.914,0.9239,0.9248,0.9234],
[0.9551,0.9543,0.956,0.9499,0.9544],
[0.963,0.9664,0.9661,0.9657,0.9631],
[0.9753,0.9793,0.9792,0.9819,0.979]     
                    ],
            'conditional':[[0.9139,0.8988,0.9113,0.9089,0.9049],
[0.9438,0.94,0.937,0.9347,0.9393],
[0.9517,0.9479,0.9606,0.9465,0.9539],
[0.9678,0.9665,0.9679,0.964,0.9666]
                    ],
             'random':[[0.8984,0.906,0.905,0.9122,0.8969],
[0.9341,0.937,0.9486,0.9455,0.9377],
[0.9504,0.9571,0.9513,0.9548,0.9543],
[0.962,0.9659,0.965,0.9646,0.9645]] ,
             'adaptive':[[0.9219,0.9141,0.9244,0.9264,0.9227],
[0.9501,0.9581,0.9518,0.9516,0.9511],
[0.9683,0.9629,0.9681,0.9688,0.968],
[0.9786,0.9772,0.9775,0.9768,0.9768]],
'original':0.8242
}


dict_cwl2 = {'my':[[0.9784,0.9804,0.9764,0.9783,0.9798],
[0.9814,0.9829,0.9826,0.9825,0.9822],
[0.9837,0.984,0.9844,0.984,0.9827],
[0.984,0.9839,0.9834,0.984,0.9847]] ,         
            'my_optimize':[[0.9785,0.9788,0.9759,0.9785,0.9776],
[0.9823,0.9819,0.9818,0.982,0.9828],
[0.983,0.9838,0.9834,0.984,0.9826],
[0.984,0.9849,0.9848,0.9847,0.9851]],  
             'lsa':[[0.964,0.9559,0.9713,0.9686,0.9726],
[0.9805,0.9838,0.9823,0.9839,0.9784],
[0.9837,0.9841,0.9848,0.9835,0.9842],
[0.9871,0.9866,0.9875,0.9864,0.9883]] , 
            'dsa':[[0.9757,0.9757,0.9779,0.9781,0.9753],
[0.9803,0.9793,0.9817,0.9811,0.9804],
[0.9825,0.9814,0.9838,0.9824,0.983],
[0.9853,0.9846,0.9853,0.9856,0.9857]     
                    ],
            'conditional':[[0.9682,0.9635,0.9607,0.9795,0.9705],
[0.9789,0.9711,0.9794,0.9794,0.9817],
[0.9797,0.9777,0.9808,0.9816,0.9779],
[0.9814,0.9779,0.983,0.9808,0.9805]
                    ],
             'random':[[0.966,0.9712,0.9687,0.9652,0.9649],
[0.9763,0.9797,0.9807,0.9816,0.9749],
[0.9808,0.9777,0.9781,0.9821,0.9817],
[0.9816,0.9838,0.9822,0.9819,0.9821]] ,
             'adaptive':[[0.8936,0.879,0.8875,0.8818,0.8823],
[0.9783,0.9786,0.9751,0.9779,0.9784],
[0.981,0.9812,0.9813,0.9803,0.9806],
[0.9837,0.9841,0.985,0.9826,0.984]],
'original':0.7984
}


dict_bima = {'my':[[0.9804,0.9794,0.9798,0.9807,0.9813],
[0.9826,0.9819,0.9832,0.9834,0.9827],
[0.9858,0.9847,0.9847,0.9844,0.9845],
[0.9861,0.9848,0.9852,0.9851,0.9858]] ,         
            'my_optimize':[[0.9805,0.983,0.9831,0.9836,0.9821],
[0.984,0.9846,0.9855,0.9858,0.9839],
[0.9891,0.989,0.989,0.9866,0.9874],
[0.9922,0.992,0.9909,0.9934,0.9933]],  
             'lsa':[[0.8954,0.8763,0.9179,0.8835,0.8898],
[0.9346,0.8956,0.9376,0.9246,0.8875],
[0.9485,0.9657,0.9789,0.9346,0.9512],
[0.9901,0.9919,0.9915,0.9908,0.9929]] , 
            'dsa':[[0.9691,0.9703,0.964,0.9741,0.964],
[0.9782,0.9807,0.9816,0.9808,0.9804],
[0.9835,0.9842,0.9855,0.9852,0.9834],
[0.9922,0.9901,0.9901,0.9885,0.9909]     
                    ],
            'conditional':[[0.9677,0.9745,0.9557,0.973,0.9733],
[0.9798,0.9775,0.9781,0.9791,0.9692],
[0.9787,0.9828,0.9843,0.9801,0.9839],
[0.9852,0.9848,0.9852,0.9863,0.9837]
                    ],
             'random':[[0.9754,0.9793,0.9807,0.9782,0.982],
[0.984,0.9794,0.9826,0.9793,0.9812],
[0.9855,0.9833,0.9837,0.9828,0.9842],
[0.9856,0.9854,0.9851,0.9874,0.9835]] ,
             'adaptive':[[0.9604,0.9624,0.963,0.963,0.9622],
[0.9792,0.9791,0.9781,0.9783,0.9792],
[0.978,0.9773,0.9786,0.9765,0.9779],
[0.9832,0.9836,0.9827,0.984,0.9819]],
'original':0.8064
}


dict_bimb = {'my':[[0.8758,0.8751,0.8742,0.8752,0.8748],
[0.8757,0.8758,0.8753,0.8759,0.8762],
[0.8757,0.8757,0.8761,0.8757,0.8761],
[0.8809,0.8802,0.8799,0.8807,0.881]] ,         
            'my_optimize':[[0.8082,0.8077,0.8082,0.8084,0.8086],
[0.8089,0.8088,0.8083,0.8084,0.8089],
[0.816,0.8189,0.8107,0.8081,0.8109],
[0.8668,0.88,0.8557,0.8753,0.8703]],  
             'lsa':[[0.8247,0.806,0.8231,0.8104,0.8058],
[0.1267,0.721,0.1448,0.1488,0.2039],
[0.1491,0.1861,0.1719,0.159,0.133],
[0.2462,0.2484,0.3059,0.3318,0.2862]] , 
            'dsa':[[0.8742,0.8739,0.872,0.8739,0.8747],
[0.8744,0.8705,0.874,0.8735,0.8737],
[0.8693,0.8752,0.8706,0.8729,0.8745],
[0.9121,0.8873,0.9297,0.8767,0.9127]     
                    ],
            'conditional':[[0.8702,0.8661,0.8677,0.8629,0.8483],
[0.8718,0.8727,0.8737,0.8737,0.874],
[0.8738,0.872,0.8757,0.8743,0.8748],
[0.8752,0.8756,0.8753,0.8702,0.8747]
                    ],
             'random':[[0.8743,0.8625,0.8706,0.8721,0.8075],
[0.8748,0.876,0.8752,0.8735,0.8746],
[0.8761,0.8755,0.8753,0.874,0.8749],
[0.8759,0.8759,0.8766,0.8759,0.8763]] ,
             'adaptive':[[0.8697,0.8698,0.8699,0.8704,0.8696],
[0.8742,0.8742,0.8737,0.8739,0.8733],
[0.8746,0.8754,0.8754,0.8749,0.8757],
[0.881,0.8804,0.8811,0.8805,0.8803]],
'original':0.8063
}


dict_translation= {'my':[[0.9161,0.9148,0.9159,0.9119,0.9156],
[0.9511,0.9489,0.9544,0.9511,0.9525],
[0.957,0.9604,0.96,0.9551,0.9633],
[0.9717,0.9757,0.9726,0.9709,0.9743]] ,         
            'my_optimize':[[0.9143,0.9137,0.915,0.9182,0.9159],
[0.9388,0.9373,0.9453,0.9369,0.9358],
[0.9473,0.9583,0.9501,0.9487,0.957],
[0.9724,0.9712,0.9713,0.9716,0.9755]],  
             'lsa':[[0.9087,0.9109,0.9098,0.9112,0.9022],
[0.9259,0.9354,0.9269,0.9331,0.9267],
[0.9569,0.9475,0.9546,0.9508,0.9483],
[0.9682,0.9677,0.97,0.9666,0.9692]] , 
            'dsa':[[0.9169,0.9231,0.9226,0.9197,0.9228],
[0.9411,0.9418,0.9419,0.945,0.9385],
[0.9538,0.9565,0.9521,0.9534,0.9578],
[0.9687,0.9684,0.974,0.973,0.9714]      
                    ],
            'conditional':[[0.9109,0.9011,0.9059,0.9064,0.8947],
[0.9145,0.9274,0.9312,0.9274,0.9294],
[0.9439,0.9424,0.9446,0.9472,0.9446],
[0.9608,0.9611,0.9564,0.9582,0.9542]
                    ],
             'random':[[0.8988,0.9167,0.9023,0.9171,0.9052],
[0.9343,0.9314,0.9185,0.9266,0.923],
[0.9468,0.9441,0.9408,0.9487,0.9458],
[0.9528,0.9573,0.9596,0.9577,0.9555]] ,
             'adaptive':[[0.9211,0.9187,0.9209,0.9205,0.9193],
[0.9532,0.9488,0.9513,0.9478,0.9485],
[0.9613,0.9559,0.9563,0.9553,0.9609],
[0.9722,0.9712,0.9719,0.969,0.9686]],
'original':0.8784
}



dict_brightness= {'my':[[0.969,0.9679,0.9681,0.9678,0.9662],
[0.9775,0.983,0.9803,0.981,0.9808],
[0.9842,0.985,0.9837,0.9843,0.9817],
[0.9894,0.9882,0.9905,0.9907,0.9892]] ,         
            'my_optimize':[[0.9762,0.9753,0.9767,0.9764,0.9744],
[0.9842,0.9852,0.983,0.9847,0.9851],
[0.9877,0.9883,0.9875,0.986,0.9874],
[0.9912,0.9914,0.9919,0.9918,0.9913]],  
             'lsa':[[0.9721,0.9723,0.9743,0.9747,0.9753],
[0.9781,0.9786,0.9786,0.9785,0.9786],
[0.9794,0.9767,0.9794,0.9801,0.9795],
[0.985,0.9876,0.9866,0.9845,0.9815]] , 
            'dsa':[[0.9655,0.9623,0.9643,0.9658,0.9661],
[0.9774,0.9803,0.9753,0.9775,0.9781],
[0.9857,0.9855,0.9831,0.9851,0.9843],
[0.9879,0.9884,0.9887,0.9894,0.9877]      
                    ],
            'conditional':[[0.9653,0.9564,0.9684,0.9573,0.9653],
[0.9746,0.9742,0.97,0.9774,0.9732],
[0.9765,0.9748,0.9776,0.9753,0.9786],
[0.9829,0.9822,0.9832,0.9834,0.9822]
                    ],
             'random':[[0.9641,0.947,0.9649,0.96,0.9673],
[0.9724,0.971,0.9749,0.9757,0.9725],
[0.9779,0.9786,0.9759,0.9752,0.9781],
[0.9821,0.984,0.9834,0.9834,0.9809]] ,
             'adaptive':[[0.9613,0.9595,0.9579,0.9577,0.9583],
[0.9769,0.9767,0.9794,0.9798,0.9782],
[0.9807,0.981,0.9795,0.9821,0.983],
[0.99,0.9897,0.9897,0.9899,0.9884]],
'original':0.9419
}



dict_shear= {'my':[[0.9312,0.9357,0.9349,0.9349,0.9361],
[0.963,0.9622,0.96,0.9628,0.9619],
[0.9721,0.9733,0.9721,0.9693,0.974],
[0.9843,0.9844,0.9848,0.9851,0.9834]] ,         
            'my_optimize':[[0.9299,0.9336,0.9341,0.93,0.9248],
[0.9565,0.9559,0.9563,0.9495,0.9556],
[0.9689,0.9667,0.9693,0.9712,0.9672],
[0.9828,0.9824,0.9825,0.9811,0.9832]],  
             'lsa':[[0.9024,0.907,0.9004,0.903,0.9085],
[0.9388,0.9323,0.9373,0.9398,0.9389],
[0.9585,0.9601,0.9575,0.9562,0.9584],
[0.9784,0.978,0.9787,0.9784,0.9763]] , 
            'dsa':[[0.9041,0.9034,0.902,0.903,0.9054],
[0.9354,0.9343,0.931,0.9318,0.9338],
[0.9644,0.9553,0.9549,0.9541,0.9546],
[0.9758,0.9812,0.9816,0.9789,0.9807]      
                    ],
            'conditional':[[0.9048,0.905,0.8915,0.8965,0.9002],
[0.9291,0.9228,0.9335,0.9253,0.9382],
[0.9488,0.9425,0.9407,0.9395,0.9463],
[0.9578,0.9599,0.9631,0.9641,0.9658]
                    ],
             'random':[[0.8878,0.9005,0.8934,0.9043,0.9034],
[0.9315,0.9194,0.9301,0.9323,0.9372],
[0.9456,0.9484,0.9463,0.948,0.9519],
[0.967,0.9584,0.9666,0.9634,0.9618]] ,
             'adaptive':[[0.9016,0.9063,0.9028,0.901,0.8989],
[0.9349,0.9408,0.9387,0.9366,0.9436],
[0.964,0.9599,0.961,0.9637,0.9582],
[0.981,0.981,0.9794,0.9811,0.9809]],
'original':0.8859
}



dict_scale= {'my':[[0.9305,0.9197,0.9318,0.9294,0.9259],
[0.9544,0.9529,0.9534,0.952,0.9519],
[0.962,0.9636,0.9578,0.9601,0.964],
[0.9767,0.9791,0.9766,0.9823,0.9789]] ,         
            'my_optimize':[[0.9156,0.9185,0.9191,0.92,0.9197],
[0.943,0.9467,0.9475,0.943,0.9447],
[0.9596,0.9573,0.9633,0.9587,0.9607],
[0.9801,0.9782,0.9777,0.9805,0.9805]],  
             'lsa':[[0.8837,0.8798,0.8806,0.8804,0.8818],
[0.9222,0.9289,0.9273,0.9292,0.9239],
[0.963,0.9665,0.966,0.9648,0.9657],
[0.9811,0.979,0.981,0.9803,0.9798]] , 
            'dsa':[[0.8907,0.8932,0.8948,0.8903,0.8905],
[0.9302,0.924,0.9306,0.9269,0.9315],
[0.9525,0.9631,0.9599,0.9597,0.9602],
[0.9811,0.9798,0.9809,0.98,0.9815]     
                    ],
            'conditional':[[0.8894,0.8861,0.8957,0.8916,0.8938],
[0.9427,0.9276,0.9278,0.9323,0.9286],
[0.9513,0.9476,0.9461,0.9516,0.9489],
[0.9702,0.9654,0.9705,0.9722,0.9678]
                    ],
             'random':[[0.8962,0.8992,0.9005,0.8991,0.9079],
[0.9378,0.9321,0.9246,0.9281,0.943],
[0.9498,0.9461,0.9458,0.9557,0.9501],
[0.964,0.9705,0.9688,0.9703,0.9649]] ,
             'adaptive':[[0.884,0.8825,0.8865,0.8859,0.8859],
[0.9228,0.9233,0.9247,0.9184,0.9234],
[0.9447,0.9442,0.9465,0.9438,0.9434],
[0.9715,0.9722,0.9732,0.9722,0.972]],
'original':0.8747
}



dict_contrast= {'my':[[0.9126,0.9178,0.917,0.9158,0.9222],
[0.9544,0.9551,0.9542,0.955,0.9537],
[0.957,0.9574,0.9577,0.962,0.9628],
[0.9744,0.9711,0.9707,0.9736,0.9752]] ,         
            'my_optimize':[[0.9236,0.9192,0.9283,0.918,0.9187],
[0.9473,0.9505,0.9518,0.953,0.9521],
[0.9611,0.96,0.9608,0.9624,0.9564],
[0.9716,0.972,0.9771,0.9743,0.9762]],   
            'lsa':[[0.9142,0.9135,0.9072,0.9067,0.9052],
[0.933,0.9321,0.9351,0.9358,0.93],
[0.9436,0.9331,0.9308,0.9486,0.9491],
[0.9663,0.9576,0.966,0.9638,0.9614]] , 
            'dsa':[[0.9212,0.922,0.9231,0.9236,0.9232],
[0.9388,0.9418,0.9454,0.9432,0.9386],
[0.9592,0.9592,0.9599,0.959,0.9576],
[0.967,0.9682,0.9705,0.9712,0.973]      
                    ],
            'conditional':[[0.9094,0.9087,0.913,0.9129,0.9012],
[0.9199,0.9282,0.9321,0.9332,0.9328],
[0.9421,0.9494,0.9447,0.9347,0.9434],
[0.9541,0.9527,0.9552,0.9569,0.9544]
                    ],
             'random':[[0.9092,0.9113,0.9072,0.9012,0.9077],
[0.9355,0.9278,0.9271,0.931,0.9321],
[0.9436,0.9381,0.9382,0.9407,0.9437],
[0.9579,0.9543,0.9559,0.9544,0.9594]] ,
             'adaptive':[[0.9294,0.9292,0.9275,0.9264,0.9279],
[0.947,0.9529,0.9471,0.9522,0.9513],
[0.9523,0.9604,0.9542,0.9591,0.9594],
[0.9706,0.9706,0.9692,0.9718,0.9691]],
'original':0.8791
}


dict_rotation= {'my':[[0.9414,0.9413,0.9425,0.9422,0.9419],
[0.9629,0.9605,0.9619,0.9627,0.9614],
[0.9656,0.9656,0.9666,0.9698,0.9676],
[0.9718,0.9744,0.9715,0.9706,0.9701]] ,         
            'my_optimize':[[0.9461,0.9381,0.9401,0.9461,0.9447],
[0.9634,0.96,0.9629,0.9593,0.9601],
[0.9696,0.9673,0.9677,0.9679,0.9683],
[0.972,0.9776,0.9738,0.9756,0.9765]],   
            'lsa':[[0.9352,0.9355,0.9359,0.9337,0.9347],
[0.9579,0.9503,0.9534,0.9525,0.9551],
[0.9628,0.9608,0.9638,0.9625,0.9611],
[0.9785,0.9777,0.977,0.9782,0.9772]] , 
            'dsa':[[0.9289,0.9236,0.9252,0.925,0.9288],
[0.9598,0.9595,0.9615,0.9588,0.9589],
[0.9683,0.9652,0.966,0.967,0.9676],
[0.9766,0.9762,0.9746,0.9723,0.9739]     
                    ],
            'conditional':[[0.9305,0.9285,0.9321,0.9322,0.9288],
[0.9383,0.9442,0.9456,0.9465,0.9437],
[0.949,0.9531,0.9475,0.9561,0.9543],
[0.9644,0.9617,0.963,0.9621,0.961]
                    ],
             'random':[[0.9376,0.9257,0.9313,0.9289,0.9243],
[0.943,0.9441,0.9502,0.9438,0.9433],
[0.9553,0.9518,0.9493,0.9568,0.9505],
[0.9589,0.9647,0.9604,0.9605,0.9624]] ,
             'adaptive':[[0.9187,0.9219,0.9195,0.9184,0.9218],
[0.9475,0.9491,0.9501,0.9477,0.9499],
[0.9592,0.9552,0.961,0.9586,0.9596],
[0.9699,0.9621,0.9683,0.969,0.9631]],
'original':0.9112
}