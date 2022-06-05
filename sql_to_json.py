import json
import pprint
variable_name = "client"
sql_fields = """clicod,clicpfcgc,clirgcgf, clides, clifan, cliend, clinum,clicmp, clibai,
clicep, clicid, cliest, stacod, clitel, clitel2, clifax, clicon, cliemail,
sysserie, sysctrl, sysver"""

list_fields = sql_fields.split(',')

result_dict = {}
for index, field in zip(range(len(list_fields)), list_fields):
    variable_index = variable_name+"[{}]".format(index)
    result_dict[field.replace('\n','')] = variable_index

print(result_dict, sep=',')
json_result = json.dumps(result_dict)

pprint.pprint(json_result)


