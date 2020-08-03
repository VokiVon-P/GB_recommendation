import numpy as np


def precision(recommended_list, bought_list):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(bought_list, recommended_list)

    precision = flags.sum() / len(recommended_list)

    return precision


def precision_at_k(recommended_list, bought_list, k=5):
  
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    

    bought_list = bought_list  # Тут нет [:k] !!
    
    if k < len(recommended_list):
        recommended_list = recommended_list[:k]

    flags = np.isin(bought_list, recommended_list)

    precision = flags.sum() / len(recommended_list)

    return precision


def money_precision_at_k(recommended_list, bought_list, prices_recommended, k=5) -> float:
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    
    recommended_list = recommended_list[:k]
    prices_recommended = np.array(prices_recommended[:k])
    
    # пойдем от обратного - проверим рекомендованный лист в покупках
    flags = np.isin(recommended_list, bought_list)
        
    # получим цены купленных товаров
    money_flags = flags*prices_recommended
    
    # отнесем сумму купленных к сумме рекомендованных (не учитывает количество)
    money_precision = money_flags.sum() / prices_recommended.sum()
    
    return money_precision


def recall(recommended_list, bought_list):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(bought_list, recommended_list)

    recall = flags.sum() / len(bought_list)

    return recall


def recall_at_k(recommended_list, bought_list, k=5):

    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    if k < len(recommended_list):
        recommended_list = recommended_list[:k]

    flags = np.isin(bought_list, recommended_list)
    recall = flags.sum() / len(bought_list)

    return recall


def money_recall_at_k(recommended_list : list, bought_list : list, \
                    prices_recommended : list, prices_bought : list, k:int = 5) -> float:
    """Точность взвешенная на цену товара

    Args:
        recommended_list (list): Список рекомендаций
        bought_list (list): Список реальных покупок
        prices_bought (list): Цены реальных покупок
        k (int, optional): Количество рекомендаций. Defaults to 5.

    Returns:
        float: Значение метрики точности 
    """
    bought_list = np.array(bought_list)
    prices_bought = np.array(prices_bought)
    
    recommended_list = np.array(recommended_list[:k])
    prices_recommended = np.array(prices_recommended[:k])
    
    flags = np.isin(bought_list, recommended_list) 
    # флаги взвешенные на цену
    money_flags = flags*prices_bought
    
    money_recall = money_flags.sum() / prices_recommended.sum()
    
    return money_recall
