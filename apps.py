import streamlit as st
import socket
import ssl
import urllib.parse

st.title("🛡️ Website Security & Info Scanner")
st.write("أداة مخصصة لفحص معلومات المواقع، عناوين الـ IP، وشهادات الحماية أمنياً.")

target = st.text_input("أدخل رابط الموقع للفحص (مثال: google.com):", "")

if st.button("بدء الفحص"):
    if target:
        try:
            if not target.startswith("http"):
                target = "https://" + target
                
            parsed_url = urllib.parse.urlparse(target)
            hostname = parsed_url.hostname
            
            with st.spinner(f"جاري فحص الموقع: {hostname}..."):
                # استخراج الـ IP
                ip_address = socket.gethostbyname(hostname)
                
                # فحص الـ SSL
                context = ssl.create_default_context()
                with socket.create_connection((hostname, 443)) as sock:
                    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                        cert = ssock.getpeercert()
                        issuer = cert.get('issuer')
                
                st.success("تم الفحص بنجاح!")
                st.write(f"**عنوان الـ IP:** `{ip_address}`")
                st.write("**شهادة الحماية (SSL):** فعالة وموثوقة ✅")
                st.json(issuer)
                
        except Exception as e:
            st.error(f"حدث خطأ أو الموقع غير آمن: {e}")
    else:
            st.warning("الرجاء إدخال رابط صالح أولاً!")
