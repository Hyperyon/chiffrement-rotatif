def cipher(msg):
  alpha = 'abcdefghijklmnopqrstuvwxyz'
  beta = alpha

  delta = [beta.find(x) for x in msg]
  for i, index in enumerate(delta):
    if index != -1:
      delta[i] = alpha[index]
    else:
      delta[i] = ' '

    alpha = alpha[-1] + alpha[:-1]

  return ''.join(delta)


def decipher(cipher_msg):
  alpha = 'abcdefghijklmnopqrstuvwxyz'
  beta = alpha
  msg_decoded = ''
  for index in cipher_msg:
    if index != ' ':
      msg_decoded += beta[alpha.find(index)]
    else:
      msg_decoded += ' '

    alpha = alpha[-1] + alpha[:-1]

  return msg_decoded

cipher_msg = cipher("toto a dit que c'etait top secret")

print(cipher_msg)

# tnrl v wak fir n nbhoy wqq rcznzn
print(decipher(cipher_msg))
