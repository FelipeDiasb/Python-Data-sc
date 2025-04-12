# estatisticas.py
import statistics

def calcular_estatisticas(notas):
    estatisticas_dict = {}
    
    if notas:
        estatisticas_dict["media"] = statistics.mean(notas)
        estatisticas_dict["mediana"] = statistics.median(notas)
        estatisticas_dict["moda"] = statistics.mode(notas) if len(set(notas)) < len(notas) else "Sem moda"
        estatisticas_dict["amplitude"] = max(notas) - min(notas)
        estatisticas_dict["desvio_padrao"] = statistics.stdev(notas) if len(notas) > 1 else 0.0
        estatisticas_dict["maior_nota"] = max(notas)
        estatisticas_dict["menor_nota"] = min(notas)
    else:
        estatisticas_dict = {
            "media": 0, "mediana": 0, "moda": 0,
            "amplitude": 0, "desvio_padrao": 0,
            "maior_nota": 0, "menor_nota": 0
        }

    return estatisticas_dict
