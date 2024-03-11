def is_plusone_dictionary(d) :
    for k, v in d.items() :
        if (k - 1 not in d.values() and k != min(d)) or v - 1 not in d :
            return False
    return True

print(is_plusone_dictionary({1:2, 3:4, 5:6, 7:8}))
print(is_plusone_dictionary({1:2, 3:4, 5:6, 8:9}))

'''def is_plusone_dictionary(d):
  for k, v in d.items():
        if k + 1 not in d.values() or (v + 1 not in d and v != max(d.values())) :
            return False
  return True'''