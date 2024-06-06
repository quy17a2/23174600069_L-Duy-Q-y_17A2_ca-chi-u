import random
import csv
import os 

xac_suat_dict = {'Bang': 0.5, 'Click': 0.5}
cac_ket_qua_set = {'Bang', 'Click'}
danh_sach_ket_qua = []

def lac_sung():
    """Mô phỏng lắc súng và trả về kết quả."""
    ket_qua_lac = random.choices(list(xac_suat_dict.keys()), weights=list(xac_suat_dict.values()), k=1)[0]
    return ket_qua_lac

def tinh_xac_suat(ket_qua):
    return xac_suat_dict[ket_qua]
def choi_game(so_lan):
    for i in range(so_lan):
        ket_qua = lac_sung()
        danh_sach_ket_qua.append(ket_qua)
        if so_lan == 5:  
            print(f"Lần lắc {i+1}: {ket_qua}")

def tinh_tong_ket_qua():
    tong_so_bang = danh_sach_ket_qua.count('Bang')
    tong_so_click = danh_sach_ket_qua.count('Click')
    return tong_so_bang, tong_so_click

def tinh_xac_suat_ket_qua(tong_so_bang, tong_so_click):
    tong_so_lan_lac = len(danh_sach_ket_qua)
    xac_suat_bang = tong_so_bang / tong_so_lan_lac
    xac_suat_click = tong_so_click / tong_so_lan_lac
    return xac_suat_bang, xac_suat_click

def ghi_vao_csv(tong_so_bang, tong_so_click, xac_suat_bang, xac_suat_click, so_lan):
    file_moi = not os.path.isfile('ket_qua.csv')  
    
    with open('dap_an.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        if file_moi:  # Nếu file mới, thêm tiêu đề
            writer.writerow(["SoLanLac", "KetQua", "SoLan", "XacSuat"])
        writer.writerow([so_lan, "Bang", tong_so_bang, xac_suat_bang])
        writer.writerow([so_lan, "Click", tong_so_click, xac_suat_click])

def main():
    
    choi_game(5)
    tong_so_bang, tong_so_click = tinh_tong_ket_qua()
    xac_suat_bang, xac_suat_click = tinh_xac_suat_ket_qua(tong_so_bang, tong_so_click)
    print(f"Tổng số kết quả Bang: {tong_so_bang}")
    print(f"Tổng số kết quả Click: {tong_so_click}")
    print(f"Xác suất xuất hiện của Bang: {xac_suat_bang:.2f}")
    print(f"Xác suất xuất hiện của Click: {xac_suat_click:.2f}")
    ghi_vao_csv(tong_so_bang, tong_so_click, xac_suat_bang, xac_suat_click, 5)

    
    danh_sach_ket_qua.clear()  
    choi_game(500)
    tong_so_bang, tong_so_click = tinh_tong_ket_qua()
    print(f"\nKết quả sau 500 lần lắc súng:")
    print(f"Tổng số kết quả Bang: {tong_so_bang}")
    print(f"Tổng số kết quả Click: {tong_so_click}")
    xac_suat_bang, xac_suat_click = tinh_xac_suat_ket_qua(tong_so_bang, tong_so_click)
    print(f"Xác suất xuất hiện của Bang: {xac_suat_bang:.2f}")
    print(f"Xác suất xuất hiện của Click: {xac_suat_click:.2f}")
    ghi_vao_csv(tong_so_bang, tong_so_click, xac_suat_bang, xac_suat_click, 500)

if __name__ == "__main__":
    main()