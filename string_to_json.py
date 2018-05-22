# python
# 실행되지 않는 코드입니다.


# header과 row에는 원하는 string데이터가 저장되어 있는 상태

for i in range (0, 10):
    # tmp에 a:b 형식으로 된 string을 저장
    tmp = headers[i] + ':\"' + row[i] + '\",'

    # get 변수에 tmp를 이어붙임
    get= get+ tmp

# 가장 마지막에 입력된 콤마가 있음. 그걸 제거.
get= get[:-1]

# 앞뒤로 중괄호 넣기
get= '{' + get+ '}'

# 마지막 단계!
string_to_json = json.loads(get)


