import json
import os

# 業種の一覧・JSONデータを読み込む
industry_json_path = f'{os.getcwd()}/industry.json'
industry_json_file = open(industry_json_path, 'r', encoding="utf-8")
industry_json_data = json.load(industry_json_file)

print('JSONデータを読み込みました。')
print(industry_json_data)

# 新しいJSONデータを作成するためのリスト
new_industry_json_data = []

# JSONデータ取り出して、新しいJSON・元データを作成する
for value in industry_json_data:
    # フォーマットを変更する
    new_industry_json_data.append({
        'industry_id': value['業種番号'],
        'industry': value['業種']
    })
print('新しい元データを作成しました。')
print(new_industry_json_data)

# 8json.dumps() で、辞書型をJSON-文字列に変換する => JSON-encoding
jsonEncode = json.dumps(new_industry_json_data, ensure_ascii=False, indent=2)
print('JSON-encoding しました。')
print(jsonEncode)

# JSONデータをファイルに保存する
with open('result.json', 'w') as json_file:
    json_file.write(jsonEncode)
