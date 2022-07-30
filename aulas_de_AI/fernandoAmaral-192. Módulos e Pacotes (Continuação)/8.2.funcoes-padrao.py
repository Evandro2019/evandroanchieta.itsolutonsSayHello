import numpy as np

print('valor absoluto ',abs(-200))

from statistics import mean, median
x = [10, 20, 30]
print(x)
print('Média', mean(x))

print("a = np.random.random((8,8)) var a eh uma matriz (8x8)")
a = np.random.random((8,8))
print(type(a))
print(a)
print("FIM DA Matriz")

#install "numpy-1.9.2rc1+mkl-cp34-none-win_amd64.whl" erro

#numpy.__version__)


# example from => http://www.estruturas.ufpr.br/disciplinas/pos-graduacao/introducao-a-computacao-cientifica-com-python/introducao-python/2-1-o-objeto-array-do-numpy/

a = np.array([0, 1, 2, 3])
print(a)

# example from => https://www.datacamp.com/community/tutorials/python-numpy-tutorial?utm_source=adwords_ppc&utm_medium=cpc&utm_campaignid=14989519638&utm_adgroupid=127836677279&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=278443377095&utm_targetid=dsa-473406585115&utm_loc_interest_ms=&utm_loc_physical_ms=1001773&gclid=CjwKCAiAp8iMBhAqEiwAJb94z2HiWZVQGXVfL5N80NDp4yxmwuMsYl850BQ5b6aGhyNF_IUy8OfVpxoCSmUQAvD_BwE
my_2d_array = np.array([2,4,8,16,32,64,128,256])
# Print out memory address
print(my_2d_array.data)

# Print out the shape of `my_array`
print(my_2d_array.shape)

# Print out the data type of `my_array`
print(my_2d_array.dtype)

# Print out the stride of `my_array`
print(my_2d_array.strides)


