import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta


num_clients = 100
products = ['Produto A', 'Produto B', 'Produto C', 'Produto D', 'Produto E']
payment_methods = ['Cartão de Crédito', 'Boleto', 'Pix']


client_ids = [f"CLI{str(i).zfill(3)}" for i in range(1, num_clients + 1)]


base_date = datetime.today()
date_list = [base_date - timedelta(days=random.randint(0, 365)) for _ in range(num_clients)]


product_list = [random.choice(products) for _ in range(num_clients)]
quantity_list = [random.randint(1, 5) for _ in range(num_clients)]  
price_per_unit_list = [random.uniform(10, 200) for _ in range(num_clients)]  
payment_method_list = [random.choice(payment_methods) for _ in range(num_clients)]

# 
total_spent_list = [quantity * price for quantity, price in zip(quantity_list, price_per_unit_list)]


df = pd.DataFrame({
    'ID Cliente': client_ids,
    'Data da Compra': date_list,
    'Produto': product_list,
    'Quantidade': quantity_list,
    'Preço Unitário': price_per_unit_list,
    'Valor Total': total_spent_list,
    'Forma de Pagamento': payment_method_list
})


print(df.head())

# Salvar o DataFrame em um arquivo CSV (opcional)
df.to_csv('vendas_loja.csv', index=False)
