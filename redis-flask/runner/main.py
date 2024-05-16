import redis
from flask import Flask, request
from faker import Faker

app = Flask(__name__)
fake = Faker()

r = redis.Redis(host='redis-app-service.ignashov.svc.cluster.local', port=6379, decode_responses=True)


@app.route("/", methods=['POST', 'GET'])
def start():
    if request.method == 'POST':
        r.set(fake.email(), fake.user_name())
    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <body>
        <form action="/" method="post">
        <button type="submit">Submit</button>
        <h1>{str([(key, r.get(key)) for key in r.scan_iter()])}</h1>
    </form>
    </body>
    </html>
    '''


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)