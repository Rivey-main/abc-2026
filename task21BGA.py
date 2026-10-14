config_values = {
    'app_name': 'NextGen', 'version': '1.0.0', 'debug': True,
    'db_host': 'localhost', 'db_port': 5432, 'db_name': 'my_database',
    'db_user': 'admin', 'db_password': 'secret123', 'api_key': 'ak_123456789',
    'api_secret': 'sk_987654321', 'base_url': 'https://example.com',
    'log_file': '/var/log/app.log', 'data_dir': '/opt/app/data', 'temp_dir': '/tmp/app'
}

# Читаем шаблон и формируем новые строки
new_lines = []
with open('config_default.txt', 'r', encoding='utf-8') as f:
    for line in f:
        # Проверяем, есть ли в строке параметр для подстановки
        if '=' in line and '?' in line:
            param_name = line.split('=')[0].strip()
            if param_name in config_values:
                val = config_values[param_name]
                # Оборачиваем строковые значения в кавычки для конфига
                formatted_val = f'"{val}"' if isinstance(val, str) else str(val)
                # Сохраняем исходное имя параметра и отступы, меняя только "?"
                line = f"{line.split('=')[0]}=  {formatted_val}\n"
        new_lines.append(line)

# Записываем готовый результат в новый файл config.txt
with open('config.txt', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
