start_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
{"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 

result_set = set()

for mini_dict in start_dict:
    result_set = result_set.union(set(mini_dict.values()))
print(result_set)