from Products.models import ProductsScores

def specialProducts():
    scores = ProductsScores.objects.all()
    List1 = [x.total_score for x in scores]
    List2 = []

    for _ in range(len(List1)):
        if len(List2) == 6:
            break
        result = max(List1)
        List2.append(result)
        List1.remove(result)

    result = [ProductsScores.objects.filter(total_score=L).first().id for L in List2]
    return result