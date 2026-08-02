import socket
import ssl
import urllib.parse

def check_website(url):
    try:
        if not url.startswith("http"):
            url = "https://" + url
            
        parsed_url = urllib.parse.urlparse(url)
        hostname = parsed_url.hostname
        
        print(f"[*] جاري فحص الموقع: {hostname}\n")
        
        ip_address = socket.gethostbyname(hostname)
        print(f"[+] عنوان الـ IP: {ip_address}")
        
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                print("[+] شهادة الحماية (SSL): فعالة وموثوقة")
                print(f"[+] الجهة المصدرة: {cert.get('issuer')}")
                
    except Exception as e:
        print(f"[-] حدث خطأ أو الموقع غير آمن: {e}")

if __name__ == "__main__":
    target = input("أدخل رابط الموقع للفحص (مثال: example.com): ")
    check_website(target)
