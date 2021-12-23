import numpy as np

Ip = 9 * 0.001
Up = 0.1
Iv = 0.3 * 0.001
Uv = 0.7
Uf = 1.2

d_Ip = 0.3 * 0.001
d_Up = 0.01
d_Iv = 0.3 * 0.001
d_Uv = 0.02
d_Uf = 0.1

Ip_Iv_2 = (Ip-Iv)*(Ip-Iv)
Uv_Up_2 = (Uv-Up)*(Uv-Up)
dUv_dUp = d_Uv*d_Uv + d_Up*d_Up
dIv_dIp = d_Iv*d_Iv + d_Ip*d_Ip

print(np.sqrt(d_Uf*d_Uf+d_Up*d_Up))
print(np.sqrt(Ip_Iv_2*dUv_dUp+Uv_Up_2*dIv_dIp)/Ip_Iv_2)
print(np.sqrt((Iv*d_Ip)*(Iv*d_Ip) + (Ip*d_Iv)*(Ip*d_Iv))/Iv/Iv)
print((Up-Uv)/(Iv-Ip))
