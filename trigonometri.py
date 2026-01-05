import math

def calculate_sine(angle, is_radians=True):
    """
    Verilen açının sinüsünü hesaplar.
    
    Args:
        angle (float): Açı değeri.
        is_radians (bool): Eğer True ise açı radyan cinsinden, False ise derece cinsinden kabul edilir.
    
    Returns:
        float: Açının sinüs değeri.
    """
    if not is_radians:
        angle = math.radians(angle)
    return math.sin(angle)

def calculate_cosine(angle, is_radians=True):
    """
    Verilen açının kosinüsünü hesaplar.
    
    Args:
        angle (float): Açı değeri.
        is_radians (bool): Eğer True ise açı radyan cinsinden, False ise derece cinsinden kabul edilir.
    
    Returns:
        float: Açının kosinüs değeri.
    """
    if not is_radians:
        angle = math.radians(angle)
    return math.cos(angle)

def calculate_tangent(angle, is_radians=True):
    """
    Verilen açının tanjantını hesaplar.
    
    Args:
        angle (float): Açı değeri.
        is_radians (bool): Eğer True ise açı radyan cinsinden, False ise derece cinsinden kabul edilir.
    
    Returns:
        float: Açının tanjant değeri.
    """
    if not is_radians:
        angle = math.radians(angle)
    return math.tan(angle)

if __name__ == "__main__":
    print("Trigonometrik İşlemler Scripti")
    print("------------------------------")
    
    # Örnek: 30, 45, 60 derece için test
    angles = [30, 45, 60]
    
    for angle in angles:
        s = calculate_sine(angle, is_radians=False)
        c = calculate_cosine(angle, is_radians=False)
        t = calculate_tangent(angle, is_radians=False)
        print(f"Açı: {angle} derece")
        print(f"  Sinüs:   {s:.4f}")
        print(f"  Kosinüs: {c:.4f}")
        print(f"  Tanjant: {t:.4f}")
        print("-" * 30)
