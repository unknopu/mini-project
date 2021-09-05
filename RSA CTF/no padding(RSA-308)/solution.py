import pwn
# Unpadded RSA is,
# encrypt(m1) * encrypt(m2) = ((m1**e) * (m2**e)) mod n 
# = (m1 * m2)**e mod n = encrypt(m1 * m2)
# So that c * x = encrypt(m) * encrypt(2) = encrypt(m * 2)

# n:    74328928701434133843613199552153335948969725158873148818821490630306533215467981357133154190848383245734980356357695020090268171953736307142974366655100426569230497974657735258687102423776418637379677627065663827007754110865433997196392909544703906346106269557483283529072472139777043185497349938657284290407
# e:    65537
# ciphertext:    15538504217552650449568474751154105746300253791569013054294031624821418686070390168799835650859792026448548686222131341280148447312090696985730868350840906567565107007737301649934318522124630105229158289501957405149799767190021902868540189964740834124701448362082855044172101741331170546332683493973401286652
# +========RECV=========+ after sent pow(2, e, n)
# Here you go:    580550060391700078946913236734911770139931497702556153513487440893406629034802718534645538074938502890768853279675297196794

host, port = 'mercury.picoctf.net', 10333
con = pwn.remote(host, port)
# Display()
print(str(con.recvuntil("n:")).replace("\\n", '\n'), end="\t")
n = int(con.recvline())
print(n)

print(str(con.recvuntil("e:")).replace("\\n", '\n'), end="\t")
e = int(con.recvline())
print(e)

print(str(con.recvuntil("ciphertext:")).replace("\\n", '\n'), end="\t")
ciphertext = int(con.recvline())
print(ciphertext)

send_msg = pow(2, e, n)*ciphertext

con.sendline(str(send_msg))
print("+========RECV=========+\n"+str(con.recvuntil("Here you go:")).replace("\\n", '\n'), end="\t")
p = int(con.recvline())
print(p)
st = str(hex(p//2)[2:])
print(bytes.fromhex(st).decode())
con.close()