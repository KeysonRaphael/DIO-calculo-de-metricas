def acuracia(vp, fn, fp, vn):
    return (vp + vn) / (vp + fn + fp + vn)

def sensibilidade(vp, fn):
    return vp / (vp + fn)

def especificidade(vn, fp):
    return vn / (vn + fp)

def precisao(vp, fp):
    return vp / (vp + fp)

def f_score(precisão, sensibilidade, beta=1):
    return (1 + (beta ** 2)) * precisão * sensibilidade / (beta ** 2 * precisão + sensibilidade)

# Matriz de confusão
matriz_confusao = [[10, 2], [1, 9]]

# Valores de VP, FN, FP e VN
vp = matriz_confusao[0][0]
fn = matriz_confusao[0][1]
fp = matriz_confusao[1][0]
vn = matriz_confusao[1][1]

# Cálculo das métricas
acuracia = acuracia(vp, fn, fp, vn)
sensibilidade = sensibilidade(vp, fn)
especificidade = especificidade(vn, fp)
precisao = precisao(vp, fp)
f_score = f_score(precisao, sensibilidade)

# Impressão dos resultados
print("Acurácia:", acuracia)
print("Sensibilidade:", sensibilidade)
print("Especificidade:", especificidade)
print("Precisão:", precisao)
print("F-score:", f_score)
