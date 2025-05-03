def calculate_average(numbers):
    """
    Calcula a média de uma lista de números.
    
    Args:
        numbers (list): Lista de números
        
    Returns:
        float: Média dos números
        
    Raises:
        ValueError: Se algum elemento da lista não for um número
    """
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError('Todos os elementos da lista devem ser números')
        
    return sum(numbers) / len(numbers) 