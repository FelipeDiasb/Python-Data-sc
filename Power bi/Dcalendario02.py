import pandas as pd
import calendar
from datetime import datetime

# Carregar a planilha de feriados
feriados_df = pd.read_excel('Power bi/Feriados/feriados_nacionais.xls')

# Garantir que a coluna 'Data' esteja no formato datetime
feriados_df['Data'] = pd.to_datetime(feriados_df['Data'], errors='coerce')

# Verificar se há valores inválidos (NaT) após a conversão
feriados_df = feriados_df.dropna(subset=['Data'])  # Remover valores inválidos

# Converter as datas para o formato dd/mm
feriados_data = feriados_df['Data'].dt.strftime('%d/%m').tolist()

# Definir as metas para cada turno
metas = {
    1: 200,  # Turno 1
    2: 180,  # Turno 2
    3: 250   # Turno 3
}

# Função para criar o calendário
def gerar_calendario(ano_inicial, ano_final):
    dias = []
    turnos = []
    metas_col = []
    feriados_col = []

    # Gerar o calendário para todos os meses entre ano_inicial e ano_final
    for ano in range(ano_inicial, ano_final + 1):
        for mes in range(1, 13):  # Para todos os meses de 1 a 12
            mes_calendario = calendar.monthcalendar(ano, mes)
            
            for semana in mes_calendario:
                for dia in semana:
                    if dia != 0:  # Se o dia for diferente de 0 (dias em branco no mês)
                        data = f"{dia:02d}/{mes:02d}/{ano}"
                        for turno in range(1, 4):  # Para cada turno (1, 2, 3)
                            dias.append(data)
                            turnos.append(turno)
                            metas_col.append(metas[turno])
                            
                            # Verificar se é feriado
                            data_dia = f"{dia:02d}/{mes:02d}"
                            if data_dia in feriados_data:
                                feriados_col.append("Sim")
                            else:
                                feriados_col.append("")  # Deixar a célula em branco

    # Criar o DataFrame
    calendario_df = pd.DataFrame({
        'Data': dias,
        'Turno': turnos,
        'Meta': metas_col,
        'Feriado': feriados_col
    })
    
    return calendario_df

# Gerar o calendário para o período de 2025 a 2026
calendario_df = gerar_calendario(2025, 2026)

# Salvar o calendário em um arquivo Excel
calendario_df.to_excel('Calendário_2025_2026_com_turnos_metas_feriados.xlsx', index=False)

print("Calendário de 2025 e 2026 com turnos, metas e feriados gerado com sucesso!")
