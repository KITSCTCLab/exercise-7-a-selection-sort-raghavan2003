from typing import List

def selectionSort(array, size) -> List[int]:
  for i in range(len(array)):
    mini = i
    for j in range(i+1,len(array)):
      if array[mini] > array[j]:
          mini = j
                             
    array[i],array[mini] = array[mini],array[i]
    
  return array
  
  
                 
# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
