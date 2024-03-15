def midpoint(point1, point2):
    x_mid = (point1[0] + point2[0]) / 2
    y_mid = (point1[1] + point2[1]) / 2
    return (x_mid, y_mid)

def main():
    try:
        # Nhập tọa độ của các đỉnh
        M = tuple(map(float, input("Nhập tọa độ của điểm M (x, y): ").split()))
        N = tuple(map(float, input("Nhập tọa độ của điểm N (x, y): ").split()))
        P = tuple(map(float, input("Nhập tọa độ của điểm P (x, y): ").split()))
        Q = tuple(map(float, input("Nhập tọa độ của điểm Q (x, y): ").split()))

        # Tính toán và in ra tọa độ trung điểm của mỗi cạnh
        MN_midpoint = midpoint(M, N)
        NP_midpoint = midpoint(N, P)
        PQ_midpoint = midpoint(P, Q)
        QM_midpoint = midpoint(Q, M)

        print("Tọa độ trung điểm của cạnh MN:", MN_midpoint)
        print("Tọa độ trung điểm của cạnh NP:", NP_midpoint)
        print("Tọa độ trung điểm của cạnh PQ:", PQ_midpoint)
        print("Tọa độ trung điểm của cạnh QM:", QM_midpoint)
    except ValueError:
        print("Vui lòng nhập tọa độ là các số thực.")

if __name__ == "__main__":
    main()
