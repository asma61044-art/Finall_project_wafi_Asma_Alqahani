import subprocess,sys,time,urllib.request
p=subprocess.Popen([sys.executable,"-m","uvicorn","wafi.api.app:app","--host","127.0.0.1","--port","8000"])
try:
    for _ in range(30):
        try:
            urllib.request.urlopen("http://127.0.0.1:8000/ready",timeout=1)
            print("smoke test passed"); break
        except Exception: time.sleep(.2)
    else: raise SystemExit("not ready")
finally:
    p.terminate(); p.wait(timeout=5)
