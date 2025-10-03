import pymysql

con = pymysql.connect(host="localhost", user = "root", passwd="mvn123", database="music", autocommit=True)

cur = con.cursor()
# id = input("Id: ")
# name = input("Name: ")
# sal = input("Sal: ")
# dep = input("Dept: ")
# des = input("Desig: ")
# doj = input("Doj: ")

# q = f"insert into emp values({id}, '{name}', {sal}, '{dep}', '{des}', '{doj}')"
# cur.execute(q)
# con.commit()
# Genre-to-mood mapping
genre_mood_map = {
    # Happy / Energetic
    "pop": "Happy",
    "dance pop": "Happy",
    "electropop": "Happy",
    "k-pop": "Happy",
    "latin pop": "Happy",
    "edm": "Energetic",
    "house": "Energetic",
    "techno": "Energetic",
    "trance": "Energetic",
    "hip hop": "Energetic",
    "rap": "Energetic",

    # Calm / Chill
    "lo-fi": "Calm",
    "chillhop": "Calm",
    "ambient": "Calm",
    "new age": "Calm",
    "acoustic": "Calm",
    "folk": "Calm",
    "jazz": "Calm",
    "r&b": "Calm",

    # Sad / Emotional
    "indie": "Sad",
    "indie pop": "Sad",
    "indie folk": "Sad",
    "emo": "Sad",
    "blues": "Sad",
    "classical": "Sad",
    "piano": "Sad",

    # Romantic / Soft
    "soul": "Romantic",
    "romantic": "Romantic",
    "soft rock": "Romantic",
    "love songs": "Romantic",
    "smooth jazz": "Romantic",

    # Angry / Intense
    "metal": "Angry",
    "heavy metal": "Angry",
    "punk": "Angry",
    "hard rock": "Angry",
    "industrial": "Angry"
}
for k,v in genre_mood_map.items():
    print(k,v)
    cur.execute(f"insert into gen_mood values('{k}', '{v}')")
