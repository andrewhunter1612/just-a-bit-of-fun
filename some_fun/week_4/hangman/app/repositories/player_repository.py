from db.run_sql  import run_sql
from models.player import Player


def get_all_players():
    players = []
    sql = "SELECT * FROM players"
    results = run_sql(sql)
    for result in results:
        player = Player(result["name"], result['id'])
        players.append(player)
    return players
    

def save_new_player(player):
    sql = "INSERT INTO players (name) VALUES (%s) RETURNING *"
    values = [player.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    player.id = id
    return player


def get_a_player(id):
    sql = "SELECT * FROM players WHERE id=%s"
    values = [id]
    results = run_sql(sql, values)[0]
    if results is not None:
        player = Player(results["name"], results["id"])
        return player
    return None