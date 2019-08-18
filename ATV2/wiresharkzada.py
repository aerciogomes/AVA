# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 12:26:49 2019

@author: aerci
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

base1 = pd.read_csv('teste1-song.csv')
base2 = pd.read_csv('teste2-song.csv')
base3 = pd.read_csv('teste3-song.csv')
base4 = pd.read_csv('teste4.csv')
base5 = pd.read_csv('teste5.csv')

#remove elementos da coluna Protocol diferentes de UDP, inplace=false não altera a base que esta sendo removida
base1_udp = base1.drop(base1[base1.Protocol != 'UDP'].index, inplace=False)
base2_udp = base2.drop(base2[base2.Protocol != 'UDP'].index, inplace=False)
base3_udp = base3.drop(base3[base3.Protocol != 'UDP'].index, inplace=False)
base4_udp = base4.drop(base4[base4.Protocol != 'UDP'].index, inplace=False)
base5_udp = base5.drop(base5[base5.Protocol != 'UDP'].index, inplace=False)

base2_servidor = base2_udp.drop(base2_udp[base2_udp.Source != '187.19.145.48'].index, inplace=False)
base2_cliente = base2_udp.drop(base2_udp[base2_udp.Destination != '187.19.145.48'].index, inplace=False)

base3_servidor = base3_udp.drop(base3_udp[base3_udp.Source != '187.19.145.48'].index, inplace=False)
base3_cliente = base3_udp.drop(base3_udp[base3_udp.Destination != '187.19.145.48'].index, inplace=False)

base4_servidor = base4_udp.drop(base4_udp[base4_udp.Source != '187.19.145.48'].index, inplace=False)
base4_cliente = base4_udp.drop(base4_udp[base4_udp.Destination != '187.19.145.48'].index, inplace=False)

base5_servidor = base5_udp.drop(base5_udp[base5_udp.Source != '187.19.145.48'].index, inplace=False)
base5_cliente = base5_udp.drop(base5_udp[base5_udp.Destination != '187.19.145.48'].index, inplace=False)

Megabytes_2 = base2_servidor['Length'].sum()/(1024)**2
Megabytes_3 = base3_servidor['Length'].sum()/(1024)**2
Megabytes_4 = base4_servidor['Length'].sum()/(1024)**2
Megabytes_5 = base5_servidor['Length'].sum()/(1024)**2

Kbytes_2C = base2_cliente['Length'].sum()/1024
Kbytes_3C = base3_cliente['Length'].sum()/1024
Kbytes_4C = base4_cliente['Length'].sum()/1024
Kbytes_5C = base5_cliente['Length'].sum()/1024

server = [Megabytes_3,Megabytes_5,Megabytes_4,Megabytes_2]
bars = ['360p','480p','720p','1080p']
y_pos = np.arange(len(bars))
plt.bar(y_pos, server, color=['#97FF33', '#65FF33', '#33FF38', '#33FF63'])
plt.xticks(y_pos, bars)
plt.title('Representando os Megabytes enviados do Servidor')
plt.xlabel('Resolução')
plt.ylabel('Megabytes')
plt.legend()
plt.show()

server = [Kbytes_3C,Kbytes_5C,Kbytes_4C,Kbytes_2C]
bars = ['360p','480p','720p','1080p']
y_pos = np.arange(len(bars))
plt.bar(y_pos, server, color=['#97FF33', '#65FF33', '#33FF38', '#33FF63'])
plt.xticks(y_pos, bars)
plt.title('Representando os Kilobytes enviados para o Servidor')
plt.xlabel('Resolução')
plt.ylabel('Kilobytes')
plt.legend()
plt.show()

server = [len(base3_servidor),len(base5_servidor),len(base4_servidor), len(base2_servidor)]
bars = ['360p','480p','720p','1080p']
y_pos = np.arange(len(bars))
plt.bar(y_pos, server, color=['black', 'red', 'green', 'orange'])
plt.xticks(y_pos, bars)
plt.title('Representando o numero de dados enviados do Servidor')
plt.xlabel('Resolução')
plt.ylabel('Dados UDP')
plt.legend()
plt.show()

server = [len(base3_cliente),len(base5_cliente),len(base4_cliente), len(base2_cliente)]
bars = ['360p','480p','720p','1080p']
y_pos = np.arange(len(bars))
plt.bar(y_pos, server, color=['black', 'red', 'green', 'orange'])
plt.xticks(y_pos, bars)
plt.title('Representando o numero de dados enviados para o Servidor')
plt.xlabel('Resolução')
plt.ylabel('Dados UDP')
plt.legend()
plt.show()










