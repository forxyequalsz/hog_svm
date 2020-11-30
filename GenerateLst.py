import os
import pandas as pd
import numpy as np


def ReadSaveAddr(dir, lst_name):
    df = pd.DataFrame(np.arange(0).reshape(0, 1), columns=['Addr'])
    print(df)
    for dirpath, dirnames, filenames in os.walk(dir):
        filenames_len = filenames.__len__()
        for i in range(filenames_len):
            filenames[i] = filenames[i][:]
        # a_list = fnmatch.filter(os.listdir(dirpath),Strb)
        if filenames_len:
            dft = pd.DataFrame(np.arange(filenames_len).reshape((filenames_len, 1)), columns=['Addr'])
            dft.Addr = filenames
            # 此处以绝对路径存储
            dft.Addr = dirpath + '\\' + dft.Addr
            frames = [df, dft]
            df = pd.concat(frames)
            print(df.shape)
    df.to_csv(dir + '\\' + lst_name + '.lst', columns=['Addr'], index=False, header=False)
    print("Write To " + lst_name + ".lst !")


if __name__ == '__main__':
    # 待生成路径
    dir = input('dir:')
    # lst命名
    lst_name = input('lst name:')
    # 处理lst
    ReadSaveAddr(dir, lst_name)