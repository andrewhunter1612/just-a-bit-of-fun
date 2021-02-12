from db.run_sql import run_sql


def add_new_history_setting_word(player):
    sql =  "INSERT INTO player_histories (word, wins, number_of_player_games) VALUES (%s, %s, %s) RETURNING *"
    values = [player.word, player.number_of_wins, player.number_of_games]
    results = run_sql(sql, values)
    
def update_history_with_win():
    

