# todo: добавьте во Flask маршруты для страниц (endpoint)
- О компании
- Контакты
- Список постов


from flask import Flask, render_template

app = Flask(__name__)

# 1. Главная страница для удобства
@app.route('/')
def index():
    return "Добро пожаловать на главную страницу!"

# 2. Страница "О компании"
@app.route('/about')
def about():
    # Можно возвращать строку или HTML-шаблон: return render_template('about.html')
    return "<h1>О компании</h1><p>Информация о нашей компании...</p>"

# 3. Страница "Контакты"
@app.route('/contacts')
def contacts():
    return "<h1>Контакты</h1><p>Телефон: +7 (000) 000-00-00<br>Email: info@example.com</p>"

# 4. Страница "Список постов"
@app.route('/posts')
def posts():
    # Пример вывода простого списка. В реальном приложении данные брались бы из БД.
    dummy_posts = [
        "Пост 1: Изучаем Flask",
        "Пост 2: Настройка маршрутов",
        "Пост 3: Работа с шаблонами"
    ]
    posts_html = "".join(f"<li>{post}</li>" for post in dummy_posts)
    return f"<h1>Список постов</h1><ul>{posts_html}</ul>"

if __name__ == '__main__':
    app.run(debug=True)

