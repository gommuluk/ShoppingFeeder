### 개발환경
OS: Windows 10  
서버: CentosOS 7.3  
언어: Python  

### 소스코드
메인코드: get_ep.py  
실행환경: Python3  
실행방법: python3 get_ep.py  

### 실행 전 설치할 것
0. python
1. pymongo: pip install pymongo
2. MongoDB: 하단 참고

### 실행 전 설정할 것
> vi ~/.bash_profile

/* ~/.bash_profile에 추가 */  
export PRODUCTS_USER=mongodb://hyom:0418@localhost:27017/  
export OUT_PATH=/root/ep_data/

> source ~/.bash_profile

### 참고) MongoDB  설치하기
> wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-rhel70-3.6.4.tgz  
> tar zxvf mongodb-linux-x86_64-rhel70-3.6.4.tgz  

> mv mongodb-linux-x86_64-rhel70-3.6.4/ /usr/local/mongodb/  
> rm mongodb-linux-x86_64-rhel70-3.6.4.tgz  

> nano ~/.bash_profile

/* ~/.bash_profile에 추가 */  
export MONGODB_HOME=/usr/local/mongodb  
PATH=$MONGODB_HOME/bin:$PATH:$HOME/bin

> source ~/.bash_profile







