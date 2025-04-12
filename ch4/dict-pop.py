#今回集計するデータ
s = """
マグロ,カツオ,サンマ,フグ,ニシン,イワシ,マグロ,マグロ,カツオ,サンマ,イワシ,イワシ,イワシ,マグロ,カツオ,サンマ,マグロ,カツオ,イワシ,マグロ,イワシ,イワシ
"""

s = s.strip()
s_list = s.split(",")

result ={}
for name in s_list:
    name = name.strip()
    if not name in result:
        result[name] =0
    result[name] = result[name] + 1

for name, v in result.items():
    print(name + " = " + str(v))
