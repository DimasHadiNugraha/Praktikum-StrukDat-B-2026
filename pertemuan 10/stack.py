


stack = []

stack.append(7)
stack.append(5)
stack.append(3)
stack.pop(1)


print(stack)

















print('  ')
print('==========================================================================')
class Kalkulator:
    def __init__(self, angka_awal):
        self.stack = [(angka_awal, f"{angka_awal}")]  # Stack menyimpan angka dan ekspresi operasinya

    def operasi(self, operator, angka):
        awal, _ = self.stack[-1]  # Ambil angka terakhir dari stack

        if operator == "+":
            hasil = awal + angka
        elif operator == "-":
            hasil = awal - angka
        elif operator == "*":
            hasil = awal * angka
        elif operator == "/":
            if angka == 0:
                print("Error: Pembagian dengan nol tidak diperbolehkan!")
                return
            hasil = awal / angka
        else:
            print("Operator tidak valid!")
            return
        
        operasi_str = f"{awal} {operator} {angka} = {hasil}"
        self.stack.append((hasil, operasi_str))  # Simpan hasil operasi ke stack
        print(f"Hasil sekarang: {operasi_str}")

    def undo(self):
        if len(self.stack) > 1:
            last_value, last_operation = self.stack.pop()  # Hapus operasi terakhir
            current_value, current_operation = self.stack[-1]  # Ambil nilai sebelumnya
            print(f"\nUndo berhasil! Operasi '{last_operation}' dibatalkan.")
            print(f"Hasil sekarang: {current_operation}")
        else:
            print("\nTidak ada operasi untuk dibatalkan.")

npm = 19  # Dua digit terakhir NPM saya sebagai angka awal
calc = Kalkulator(npm)

# operasi
calc.operasi("+", 4)  # 19 + 4 = 23
calc.operasi("-", 7)  # 23 - 7 = 16
calc.operasi("*", 5)  # 16 * 5 = 80

# Menguji fitur Undo dengan dua kali Undo
calc.undo()  # Kembali ke 23 - 7 = 16
calc.undo()  # Kembali ke 19 + 4 = 23