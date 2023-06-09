import hashlib
def increase_length(data):
  n = 0
  while 2 ** n < len(data):
    n += 1
  new_len = 2 ** n
  if new_len == len(data):
    return data
  else:
    last = data[-1]
    data.extend([last] * (new_len - len(data)))
    return data

def merkel_root(transactions):
  if len(transactions) == 1:
    return transactions[0]
  
  hashed_data = list(map(lambda x :hashlib.sha1(x.encode()).hexdigest() , transactions))
  print(len(transactions))
  
  merged_list = [hashed_data[i] + hashed_data[i+1] for i in
  
  range(0 , len(transactions) , 2)]
  
  return merkel_root(merged_list)

if __name__ == "__main__":
  transactions = ["t1","t2","t3","t4","t5"]
  transactions = increase_length(transactions)
  print(transactions)
  print(merkel_root(transactions))