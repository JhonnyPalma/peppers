SIZE = 512
BATCH_SIZE = 300

ENVIROMENT = 'LENNIN-TOSHIBAPC'

if ENVIROMENT == 'LENNIN-TOSHIBAPC':
    BASE_PATH = 'E:/TESIS/dicom/'
    TMP_PNG_PATH = 'E:/TESIS/png/'

    CSV_PATH = 'E:/TESIS/csv/global.csv'
    CSV_TRAINPNG_PATH = 'E:/TESIS/csv/pngtrain.csv'
    CSV_TESTPNG_PATH = 'E:/TESIS/csv/pngtest.csv'

    H5_PATH = 'E:/TESIS/h5'

    LOG_FILE_PATH = 'E:/TESIS/log.txt'

    CAFFE_PATH = 'C:/Anaconda2/envs/peppers/Lib/site-packages/caffe'

    # MODEL_FILE = '/home/lennin92/dicom/caffe/deploy.prototxt'
    # PRETRAINED = '/home/lennin92/dicom/caffe/caffe_2_iter_3676.caffemodel'

else:
    TMP_PNG_PATH = '/run/media/lennin92/SAMSUNG/DICOM/png/'
    H5_PATH = ''

    CSV_PATH = '/run/media/lennin92/SAMSUNG/DICOM/csv/global.csv'
    CSV_TRAINPNG_PATH = '/run/media/lennin92/SAMSUNG/DICOM/csv/pngtrain.csv'
    CSV_TESTPNG_PATH = '/run/media/lennin92/SAMSUNG/DICOM/csv/pngtest.csv'

    TRAIN_PATH = '/run/media/lennin92/SAMSUNG/DICOM/h5/train.h5'
    TRAINLIST_PATH = '/run/media/lennin92/SAMSUNG/DICOM/h5/trainlist.h5.txt'
    TEST_PATH = '/run/media/lennin92/SAMSUNG/DICOM/h5/test.h5'
    TESTLIST_PATH = '/run/media/lennin92/SAMSUNG/DICOM/h5/testlist.h5.txt'

    BASE_PATH = '/run/media/lennin92/SAMSUNG/DICOM/'

    LOG_FILE_PATH = '/run/media/lennin92/SAMSUNG/DICOM/log.txt'

    CAFFE_PATH = '~/caffe/python'

    MODEL_FILE = '/home/lennin92/dicom/caffe/deploy.prototxt'
    PRETRAINED = '/home/lennin92/dicom/caffe/caffe_2_iter_3676.caffemodel'
