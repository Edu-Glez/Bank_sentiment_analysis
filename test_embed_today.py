import os
import sys
arg=sys.argv
banco=arg[1]
fecha_inicio=arg[2]
fecha_fin=arg[3]
os.system("python bueno_por_ahora_today.py"+" "+banco+" "+fecha_inicio+" "+fecha_fin)
os.system("python load_classifier_today.py"+" "+banco+"_"+fecha_inicio)
os.system("python subida_predi.py"+" "+banco+" "+banco+"_"+fecha_inicio+"_resultados")
