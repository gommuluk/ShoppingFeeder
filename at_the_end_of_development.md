### 알게된 사실
	1. Python은 PyCharm이 편하다
	2. 파이썬을 설치하면 pip 명령어를 실행할 수 있다!
	3. MongoDB설치 시 MongoDB Compass 체크는 해제한다.
	4. MongoDB사용 전에는 mongod를 실행해준다~
	5. yum은 python2를 쓴다. 하지만 pymongo를 위해 python3도 
설치해주자.ㅇunlink /bin/pythonㅇln -s /bin/python2 /bin/python
	6. 갑자기 ls나 cd같은 기본 명령어가 안 먹을 때: export 
PATH=/usr/bin:/bin
	7. pymongo는 python3에서 돌아간다
	8. Python ~ MongoDB연결(connection = 
pymongo.MongoClient(os.environ['PRODUCT_INFO_USER'])) << user, pwd, ip, 
port까지만!
	9. CSV파일 헤더 설정에 대한 코드가 따로 있다.
	10. 파일을 읽을 때 인코딩에 주의하자. (open('파일경로.txt', 
'rt', encoding='UTF8'))
	11. 서버에 파이썬 설치하는 법 (http://depository.tistory.com/2)
	12. id앞에 \ufeffid 추가되는 것: 인코딩 타입이 unicode 또는 
UTF-8인 문서를 읽을 때 파일의 처음에 추가되는 사항
	13. Cursor Instance는 인덱스로.. .next()같은 걸로도 접근이 
가능하다고 함. 2차원 배열로도 접근이 가능함. 
cur=db.products.find({"id":"393939"})한 다음 cur[0][2] 이렇게 쓰면 id가 
겹치는 여러 개의 데이터들 중에 0번째를 택하고, 그 중에 두 번째에 있는 
JSON값을 택한다는 의미임.
	14. thread를 적용할 수 있음: txt로의 저장은, 개수를 모르니까 
딱히. 하지만 저장 후 compare할 땐 2개로 쪼개서 작업할 수 있음









