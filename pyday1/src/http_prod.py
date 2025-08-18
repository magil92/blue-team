# بيانات البداية
ip_string = "192.168.1.1"
port = "443"
int_port = int(port)
is_secure = (int_port == 443)
#print(is_secure)

# تمثيل السجل
log_tokens = "Aug 12 10:06:01 sshd[1234]: Failed password for guest from 192.0.2.15 port 22 ssh2".split()


month, day, time, host, *message_ports = log_tokens

# استخراج عنوان الـ IP من السجل
ip = log_tokens[7]  # عنوان الـ IP في الموضع السابع بعد "from"

# تحديد عدد المحاولات الفاشلة
failed_attempts = 0

# جملة if للتحقق من فشل محاولة الدخول
if 'Failed' in message_ports:
    failed_attempts += 1
    print("[ALERT] Failed login attempt detected!")

# عرض البيانات المفصلة
print(log_tokens)  # طباعة السجل بالكامل
print(f"[PARSED] Data: {month} {day} {time}, Host: {host}")
print(f"[MESSAGE]: {' '.join(message_ports)}")
print(f"[PARSED] Data: IP: {ip}")
print(f"[INFO] Failed login attempts: {failed_attempts}")





