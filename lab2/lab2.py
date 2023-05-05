from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/')
def he():
    user_data={
        "name":"Клод Моне",
        "link":"https://gallerix.ru/album/Claude-Monet",
        "img":"https://sr.gallerix.ru/_EX/442966767/1524422414.jpg",
        "poroda":"Водяные лилии",
        "char":"Импрессионизм",
        "description":"Попробуем давай слова найти. Надёжные. Их надо б наскрести на остановки три или четыре. Там и сойдём, в их оставаясь в мире.",
        "description1":"Применим все, чтоб выход обрести, где входа не было. Пути не по путиуже нашлись. Но и иных полно. Известны способы - кино про них в кино."
        }
    return render_template("sam.html", user=user_data)
app.run(debug=True)