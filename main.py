'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
from scipy.optimize import linprog

# Koefisien fungsi tujuan (biaya)
c = [10, 8]  # Harga bahan pakan A dan B

# Koefisien kendala ketidaksetaraan (protein dan energi)
A = [[-3, -2], [-2, -4]]  # Perubahan dalam protein dan energi untuk masing-masing bahan
b = [-18, -24]  # Kebutuhan minimum protein dan energi

# Batasan variabel (kg bahan pakan A dan B yang digunakan)
x_bounds = (0, None)  # x >= 0
y_bounds = (0, None)  # y >= 0

# Menyelesaikan masalah program linear
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

if result.success:
    kg_bahan_pakan_A = result.x[0]
    kg_bahan_pakan_B = result.x[1]
    biaya_total = result.fun  # Biaya minimal
    
    print("Hasil Optimasi:")
    print(f"Jumlah kg bahan pakan A yang harus digunakan: {kg_bahan_pakan_A} kg")
    print(f"Jumlah kg bahan pakan B yang harus digunakan: {kg_bahan_pakan_B} kg")
    print(f"Biaya minimal yang diperlukan: {biaya_total} ribu rupiah")
else:
    print("Tidak ada solusi yang memenuhi batasan yang diberikan.")
    