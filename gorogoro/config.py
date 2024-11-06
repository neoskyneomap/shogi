import os
import tensorflow as tf

def setup_gpu():
    # GPUの設定を確認する
    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        try:
            # 設定により、必要なメモリのみを確保するように設定
            #for gpu in gpus:
                #tf.config.experimental.set_memory_growth(gpu, True)
            logical_gpus = tf.config.experimental.list_logical_devices('GPU')
            print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
        except RuntimeError as e:
            # メモリ設定はプログラム開始前に行う必要があるため、エラーが発生する可能性があります。
            print(e)

    # TensorFlowのログレベルを設定
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 一般的なエラーのみ表示
