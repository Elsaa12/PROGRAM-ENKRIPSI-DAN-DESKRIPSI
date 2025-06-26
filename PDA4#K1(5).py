"""
PDA 4 - LARIK (ARRAY)
Nama : Elsa Aiziyah
NIM  : 21305144025
Kelas: Matematika E
"""
print('='*50)
print('PROGRAM ENKRIPSI DAN DESKRIPSI'.center(50))
print('='*50)
def pad_key(teks, kunci):
    padded_kunci = ''
    i = 0
    for char in teks:
        if char.isalpha():
            padded_kunci += kunci[i % len(kunci)]
            i += 1
        else:
            padded_kunci += ' '
    return padded_kunci

def enkripsi_deskripsi_char(teks_char, kunci_char, mode='encrypt'):
    posisi_huruf_pertama = 'a'
    if teks_char.isalpha():
        if teks_char.isupper():
            posisi_huruf_pertama = ''

        posisi_akhir_char = ord(teks_char) - ord(posisi_huruf_pertama)
        posisi_kunci_char = ord(kunci_char.lower()) - ord('a')

        if mode == 'encrypt':
            posisi_baru_char = (posisi_akhir_char + posisi_kunci_char) % 26
        else:
            posisi_baru_char = (posisi_akhir_char - posisi_kunci_char + 26) % 26
        return chr(posisi_baru_char + ord(posisi_huruf_pertama))
    return teks_char

def enkripsi(teks, kunci):
    sandi = ''
    for plaintext_char, key_char in zip(teks, pad_key(teks, kunci)):
        sandi += enkripsi_deskripsi_char(plaintext_char, key_char)
    return sandi

def deskripsi(sandi, kunci):
    teks = ''
    for sandi_char, key_char in zip(sandi, pad_key(sandi, kunci)):
        teks += enkripsi_deskripsi_char(sandi_char, key_char, mode ='decrypt')
    return teks

teks = input('Masukan pesan : ')
kunci = input('Masukan kunci: ')

sandi = enkripsi(teks, kunci)
deskripsi = deskripsi(sandi, kunci)

print(f'Enkripsi : {sandi}')
print(f'Deskripsi: {deskripsi}')


