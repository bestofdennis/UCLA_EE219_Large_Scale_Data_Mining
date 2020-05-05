import wget, tarfile
import os
 

DATA_URL = 'https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz'

 
out_fname = 'cifar-10-python.tar.gz'
 
wget.download(DATA_URL, out=out_fname)
# 提取压缩包
#tar = tarfile.open(out_fname)
#tar.extractall()
#tar.close()
# 删除下载文件
#os.remove(out_fname)

