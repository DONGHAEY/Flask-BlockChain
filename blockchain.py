import hashlib
import json
from time import time


#블럭체인은 해쉬를 통하여 다같이 연결되어져있다
#해쉬란 간단하게 말하자면, 단순히 입력값을 취하는 함수이며 입력으로부터 그 입력을 결정하는 출력 값을 생성한다
#A hash function is simply a function that takes in input value, and from that input creates an output value deterministic of the input value. For any x input value, you will always receive the same y output value whenever the hash function is run. In this way, every input has a determined output.
#https://privacycanada.net/hash-functions/what-are-hash-functions/

class Blockchain(object) :
    def __init__(self) :
        self.chain=[]
        self.current_transactions=[]
        #새로운 제네시스 블록 만들기##
        self.new_block(previous_hash=1, proof=100)

    def new_block(self) :
        #새로은 블럭을 생성하고 체인에 넣는 함수

        """블럭체인에 들어갈 새로운 블럭을 만드는 곳"""
        """index는 블록의 번호, timestamp는 블럭이 만들어진 시간이다."""
        """transaction은 블록에 포함될 거래이다."""
        """proof는 논스값이고, previous_hash는 이전 블록의 해시값이다"""

        block = {
            'index':len(self.chain)+1,
            'timestamp' : time(),
            'transaction' : self.current_transactions,
            'proof' : proof,
            'previous_hash' : previous_hash or self.hash(self.chain[-1])
        }

        #거래 리스트 초기화#
        self.current_transactions = []
        #추가
        self.chain.append(block)
        return block

    #새로운 블럭을 만드는 함수이다#
    def new_transaction(self, sender, recipient, amount) :
        """새로운 거래는 다음으로 채굴될 블록에 포함되게 된다"""
        """거래는 3개의 인자로 구성되어있다"""
        """sender은 수신자, recipient는 string으로 각각 수신자와 송신자의 주소이다"""
        """amount는 전송되는 양을 의미한다. 이 함수의 반환 값은 해당 거래가 속해질 블록의 숫자를 의미한다."""
        self.current_transactions.append({ #dictionary 형태?
            'sender' : sender,
            'recipient' : recipient,
            'amount' : amount,
        })
        return self.last_block['index'] + 1
    
    @property
    def last_block(self) :
        #체인의 가장 블록을 반환
        return self.chain[-1]

    @staticmethod
    def hash(block):
        #블록의 해쉬함수
        def hash(block):
            """
            암호화는 SHA-256을 이용한다ㅎㅎ
            해시값을 만드는데 hash함수는 block이 입력값으로 받는다ㅎㅎ
            """
            block_string = json.dumps(block, sort_key=True).encode()
            return hashlib.sha256(block_string).hexdigest()