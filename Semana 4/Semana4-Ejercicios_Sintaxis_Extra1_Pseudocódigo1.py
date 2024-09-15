# Cree un psedocódigo que le pida un precio de producto al usuari, calcule su descuento y muestre el precio final tomando en cuenta que:
# Si el precio es menor a 100, el descuento es del 25%
# Si el precio es mayor o igual a 100, el descuento es del 10%
# ej:
# 120 -> 108
# 40 -> 39.2

descuento = 0
precio_final = 0
precio_de_producto = int(input("Favor introduzca el precio del producto: "))
if precio_de_producto >= 100:
    descuento = (precio_de_producto * 10 / 100)
    precio_final =  precio_de_producto - descuento
else:
    descuento = (precio_de_producto * 2 / 100)
    precio_final = precio_de_producto - descuento
print(f"El precio final del producto es de: {precio_final}")