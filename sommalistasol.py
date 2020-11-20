def list_sum(the_list):
 sum=0
 for item in the_list:
  sum = sum + item
  print("Somma: {}".format(sum))
list_sum([1,4,10])