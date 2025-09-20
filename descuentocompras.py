# Archivo: calculo_descuento.py

def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento de una compra.

    Parámetros:
        monto_total (float): Monto total de la compra.
        porcentaje_descuento (float, opcional): Porcentaje de descuento a aplicar (default 10%).

    Retorna:
        float: Monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal
if __name__ == "__main__":
    # Llamada solo con monto total (usa el descuento por defecto del 10%)
    monto1 = 1000
    descuento1 = calcular_descuento(monto1)
    monto_final1 = monto1 - descuento1
    print(f"Compra: ${monto1}")
    print(f"Descuento aplicado: ${descuento1}")
    print(f"Monto final a pagar: ${monto_final1}")
    print("--------------------------------------------------")

    # Llamada con monto total y porcentaje de descuento específico
    monto2 = 2000
    descuento2 = calcular_descuento(monto2, 20)  # 20% de descuento
    monto_final2 = monto2 - descuento2
    print(f"Compra: ${monto2}")
    print(f"Descuento aplicado: ${descuento2}")
    print(f"Monto final a pagar: ${monto_final2}")
