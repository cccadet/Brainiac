import json

def clean_json(response):
    # Removendo as marcações extras como ```json e \n
    clean_content = response.content.strip('```json\n').strip('```')
    
    # Transformando em um dicionário
    result_dict = json.loads(clean_content)

    return result_dict