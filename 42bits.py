def permutation(plain_text):
  p = ""
  IP = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
  for x in IP :
    p += plain_text[x-1]
  return p

def inv_per(text):
  final = ""
  IP = [40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]
  for x in IP:
    final += text[x-1]
  return final


def expand(text):
  temp = ""
  EXPANSION_TABLE = [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]
  for x in EXPANSION_TABLE :
    temp += text[x-1]
  return temp

def inv_per_func(text):
    temp = ""
    inv = [9,17,23,31,13,28,2,18,24,16,30,6,26,20,10,1,8,14,25,3,4,29,11,19,32,12,22,7,5,27,15,21]
    for x in inv:
        temp += text[x-1]
    return temp


def s_box(text, i):
     S = [
             # Box-2
             [
                 [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
                 [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
                 [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
                 [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
                 ],

             # Box-3

             [
                 [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
                 [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
                 [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
                 [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]

                 ],

             # Box-4
             [
                 [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
                 [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
                 [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
                 [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
                 ],

             # Box-5
             [
                 [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
                 [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
                 [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
                 [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
                 ],
             # Box-6

             [
                 [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
                 [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
                 [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
                 [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]

                 ],
             # Box-7
             [
                 [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
                 [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
                 [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
                 [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
                 ],
             # Box-8

     [
             [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
             [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
             [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
             [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
             ]

     ]
     s_out = ""
     row = int(text[0] + text[5], base = 2)
     column = int(text[1] + text[2] + text[3] + text[4], base = 2)
     s_out += '{0:04b}'.format(S[i][row][column])
     return s_out



from bs4 import BeautifulSoup
import requests


P = ['0000000000000000', '1100000000000000', '0000000000000001', '0011000000000000', '1111000000000000']
P_star = ['0000000000400000', '1100000000400000', '0000000000400001', '0011000000400000', '1111000000400000']
Pxor = '0000000000400000'
T = list()
T_star = list()
Txor = list()


for plain_text in P:
  page_url = 'https://fast-beyond-10656.herokuapp.com/?utf8=✓&input=' + plain_text + '&commit=Encrypt'
  page_response = requests.get(page_url)
  soup = BeautifulSoup(page_response.content, 'html.parser')
  text = soup.span.text
  x   = ""
  for i in range(16):
      x += ('{0:04b}'.format(int(text[i], base = 16)))
  T.append(x)

for plain_text_star in P_star:
  page_url = 'https://fast-beyond-10656.herokuapp.com/?utf8=✓&input=' + plain_text_star + '&commit=Encrypt'
  page_response = requests.get(page_url)
  soup = BeautifulSoup(page_response.content, 'html.parser')
  text = soup.span.text
  x = ""
  for i in range(16):
    x += ('{0:04b}'.format(int(text[i], base = 16)))
  T_star.append(x)


for i in range(5):
  Txor.append('{0:064b}'.format(int(T[i], base = 2) ^ int(T_star[i], base = 2)))


keys = [ 1, 2, 3, 4, 5, 6, 7]


for i in range(7):
    for key in range(64):
      flag = 1
      for x in range(5):
          rem_per_T = permutation(T[x])
          rem_per_T_star = permutation(T_star[x])
          d = rem_per_T[32:]
          d_star = rem_per_T_star[32:]
          d_expanded = expand(d)
          d_star_expanded = expand(d_star)

          temp = (permutation(Txor[x]))[:32]
          d_out_xor = inv_per_func(temp)
          out = int(d_out_xor[(i+1)*4:(i+2)*4], base = 2)

          if (out != (int(s_box('{0:06b}'.format(int(d_expanded[(i+1)*6:(i+2)*6], base =2) ^ key), i), base = 2) ^ int(s_box('{0:06b}'.format(int(d_star_expanded[(i+1)*6:(i+2)*6], base =2) ^ key), i), base = 2))):
              flag = -1
              break

      if flag == 1:
            if keys[i] != i+1:
                print("More than one key for " + str(i+2))
            keys[i] = key
key_bin_42 = ""
key_bin_42 += '222222'
for i in range(7):
      key_bin_42 += '{0:06b}'.format(keys[i])
print(key_bin_42)
