import sys
import os

# Adiciona o diretório pai ao sys.path para garantir que o módulo 'app' seja encontrado,
# independente da pasta de onde o aluno rode o pytest.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.pagamentos import (
    calcular_desconto,
    aplicar_juros_atraso,
    validar_metodo_pagamento,
    processar_reembolso
)

# ====================================================================
# ÁREA DO ALUNO
# ====================================================================

# TODO: Crie do zero a função `test_calcular_desconto()`
# Implemente nela pelo menos 2 asserções (assert):
# 1 - Teste um cálculo de desconto válido.
# 2 - Teste outro cálculo de desconto válido.

# TODO: Crie do zero a função `test_aplicar_juros_atraso()`
# Implemente nela pelo menos 2 asserções (assert):
# 1 - Teste a aplicação de juros com dias de atraso.
# 2 - Teste o caso sem atraso (0 dias).

# TODO: Crie do zero a função `test_validar_metodo_pagamento()`
# Implemente nela pelo menos 2 asserções (assert):
# 1 - Teste um método de pagamento aceito.
# 2 - Teste um método rejeitado.

# TODO: Crie do zero a função `test_processar_reembolso()`
# Implemente nela pelo menos 2 asserções (assert):
# 1 - Teste um reembolso válido (valor reembolsado menor ou igual ao pago).
# 2 - Teste um caso de erro, simulando uma regra de negócio que restringe o reembolso (deve retornar -1).
