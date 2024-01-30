import requests

def send_data():
    data = {"message": "Hello from the transmitter!"}
    response = requests.post("http://10.244.0.58:5000/receive", json=data)
    print("Transmitter Response:", response.text)

if __name__ == "__main__":
    send_data()
