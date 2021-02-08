import time

tiempo = time.localtime()
año = tiempo[0]
mes = tiempo[1]
dia = tiempo[2]
print("hoy es {0}/{1}/{2}".format(dia, mes, año))
print("este programa tomó {0} segundos en completarse".format(time.perf_counter()))