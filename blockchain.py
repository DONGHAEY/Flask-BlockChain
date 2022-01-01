#블럭체인은 해쉬를 통하여 다같이 연결되어져있다
#해쉬란 간단하게 말하자면, 단순히 입력값을 취하는 함수이며 입력으로부터 그 입력을 결정하는 출력 값을 생성한다
#A hash function is simply a function that takes in input value, and from that input creates an output value deterministic of the input value. For any x input value, you will always receive the same y output value whenever the hash function is run. In this way, every input has a determined output.
#https://privacycanada.net/hash-functions/what-are-hash-functions/

class Blockchain(object) :
    def __init__(self) :
        self.chain=[]
        self.current_transactions=[]
    def new_block(self) :
        #새로은 블럭을 생성하고 체인에 넣는 함수
        pass
    @staticmethod
    def hash(block):
        #블록의 해쉬함수
        pass
    @property
    def last_block(self) :
        #체인의 가장 블록을 반환
        pass

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
