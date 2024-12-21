from itsdangerous import URLSafeTimedSerializer
from key import salt
def endata(data):
    serializer=URLSafeTimedSerializer('Anitha@123')
    return serializer.dumps(data,salt=salt)

def dedata(data):
    serializer=URLSafeTimedSerializer('Anitha@123')
    return serializer.loads(data,salt=salt)