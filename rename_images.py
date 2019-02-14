import os

path = os.getcwd() + '/vada_pav'
files = os.listdir(path)
print(len(files))

i=1

for file in files :
      os.rename(os.path.join(path,file),os.path.join(os.getcwd() + '/vada_pav_rename',str(i)+'.png'))
      i = i+1
