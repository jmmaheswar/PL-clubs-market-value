

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

import os
for dirname, _, filenames in os.walk('/content/sample_data'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

appearances_df = pd.read_csv("/content/sample_data/appearances.csv")

clubs_df= pd.read_csv("/content/sample_data/clubs.csv")

game_events_df=pd.read_csv("/content/sample_data/game_events.csv")
games_df=pd.read_csv("/content/sample_data/games.csv")
club_games_df=pd.read_csv("/content/sample_data/club_games.csv")

epl_teams=clubs_df[(clubs_df['domestic_competition_id'] == 'GB1') & (clubs_df['last_season'] == 2024)]
epl_teams

fav_club_df = clubs_df[clubs_df['name'] == 'Manchester United Football Club']
fav_club_df

players_df = pd.read_csv("/content/sample_data/players.csv")
players_df[(players_df['current_club_domestic_competition_id'] == 'GB1') & (players_df['last_season'] == 2024)]

players_df[(players_df["player_id"] == 16306)]

players_df[(players_df['current_club_domestic_competition_id'] == 'GB1') & (players_df['last_season'] == 2024)]

filtered_teams = players_df[(players_df['current_club_domestic_competition_id'] == 'GB1') & (players_df['last_season'] == 2024)]

filtered_teams_list = filtered_teams['current_club_name'].drop_duplicates().tolist()

print(filtered_teams_list)

selected_clubs = ['Brighton and Hove Albion Football Club', 'Everton Football Club', 'Manchester City Football Club', 'Manchester United Football Club', 'West Ham United Football Club', 'Newcastle United Football Club', 'Southampton Football Club', 'Tottenham Hotspur Football Club', 'Association Football Club Bournemouth', 'Fulham Football Club', 'Wolverhampton Wanderers Football Club', 'Brentford Football Club', 'Aston Villa Football Club', 'Crystal Palace Football Club', 'Leicester City Football Club', 'Arsenal Football Club', 'Liverpool Football Club', 'Nottingham Forest Football Club', 'Chelsea Football Club', 'Ipswich Town Football Club']

pl_players = players_df[(players_df['current_club_name'].isin(selected_clubs)) & (players_df['last_season'] == 2024)]

pl_players

squad_size = pl_players.groupby('current_club_name').size().reset_index(name='squad_size')
squad_size = squad_size.sort_values(by='squad_size', ascending=False)
squad_size.head(3)

club_total_value = pl_players.groupby('current_club_name')['market_value_in_eur'].sum().reset_index()
club_total_value.columns = ['Club', 'Total Market Value (EUR)'] # Renaming the columns for clarity

club_total_value = club_total_value.sort_values(by='Total Market Value (EUR)', ascending=False)
club_total_value['Market Value'] = club_total_value['Total Market Value (EUR)'].apply(lambda x: '{:,.2f} EUR'.format(x))

# Merge "club_total_value" and "squad_size"
club_total_value_merged = club_total_value.merge(squad_size[['current_club_name', 'squad_size']], left_on='Club', right_on='current_club_name', how='left')

club_total_value_merged = club_total_value_merged.drop(columns='current_club_name')
club_total_value_merged[["Club", "Market Value", "squad_size"]]

fig = px.bar(club_total_value_merged, x='Club', y='squad_size', title='Premier League Squad Sizes',
             labels={'name': 'Club Name', 'squad_size': 'Squad Size'},
            color="squad_size",
            hover_data = "Market Value")
fig.update_layout(xaxis_title='Club Name', yaxis_title='Squad Size')
fig.update_xaxes(categoryorder='total descending', tickangle=-45)
fig.show()

