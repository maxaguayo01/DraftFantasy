import streamlit as st
import pandas as pd
import os

st.title("Fantasy Football Lineup Selector   . 🧙🏻‍♂️🏈")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "../../data/processed/df_draft_players.csv")

df = pd.read_csv(CSV_PATH)

st.subheader("Possible Draft Elections")
st.dataframe(df)

def choose_players(positions, label, max_count=1):
    subset = df[df["Position"].isin(positions)]
    return st.multiselect(label, subset["Player"].unique(), max_selections=max_count)

st.header("Select your Headline")

qb = choose_players(["QB"], "Quarterback (QB)")
rb = choose_players(["RB"], "Running Backs (RB) - 2 titulares", max_count=2)
wr = choose_players(["WR"], "Wide Receivers (WR) - 2 titulares", max_count=2)
te = choose_players(["TE"], "Tight End (TE)")
flex = choose_players(["RB", "WR", "TE"], "FLEX (RB/WR/TE)")
k = choose_players(["K"], "Kicker (K)")
defense = choose_players(["DEF"], "Defense / Special Teams (DEF)")

st.header("Select your bench - Up to 7 players")
bench = choose_players(["QB", "RB", "WR", "TE", "K", "DEF"], "Bench (7)", max_count=7)

st.header("Optimize your allineation")
st.button("Optimize")

st.header("Draft Assistant")

st.write("### Mock Draft")
st.write("#### Type of Order")
draft_order = st.multiselect(
    "Choose options:",
    ["Snake", "Auction"]
)

st.write("#### Number of Players")
num_players = st.number_input(
    "Total players in the league:",
    min_value=2, max_value=32, step=1
)

st.write("#### Initial Pick")
initial_pick = st.number_input(
    "Your initial pick:",
    min_value=1, max_value=int(num_players), step=1
)

st.write("### Real Draft")
st.write("#### Type of Order")

draft_order_real = st.multiselect(
    "Choose options:",
    ["Snake", "Auction"]
)

num_players_real = st.number_input(
    "Número total de jugadores en la liga:",
    min_value=2, max_value=32, step=1,
    key="num_players_real"
)

initial_pick_real = st.number_input(
    "Tu pick inicial:",
    min_value=1, max_value=num_players, step=1,
    key="initial_pick_real"
)

st.write("---")


# Estado persistente
if "drafted" not in st.session_state:
    st.session_state.drafted = []

# Quitar los jugadores ya drafteados
available_df = df[
    ~df["name"].isin(st.session_state.drafted)
].reset_index(drop=True)



st.write("### Registrar picks de otros equipos")

pick_other = st.selectbox(
    "Selecciona un jugador que ya fue drafteado por otro equipo:",
    available_df["name"] if not available_df.empty else ["(No hay disponibles)"],
    key="pick_other_real"
)

if st.button("Agregar pick de otro equipo"):
    st.session_state.drafted.append(pick_other)
    st.success(f"{pick_other} marcado como drafteado por otro equipo.")


# ===========================
# 4. PREDICCIÓN DEL MEJOR PICK
# ===========================
st.write("---")
st.write("### Mejor pick recomendado para ti")

available_df = df[
    ~df["name"].isin(st.session_state.drafted)
].reset_index(drop=True)

if available_df.empty:
    st.warning("Ya no quedan jugadores disponibles.")
else:
    # ⭐ Predicción básica: mayor proyección
    best_pick = available_df.sort_values("projection", ascending=False).iloc[0]

    st.success(
        f"**Recomendación:** {best_pick['name']} — {best_pick['pos']} "
        f"(Proyección: {best_pick['projection']})"
    )

# ===========================
# 5. TABLAS
# ===========================
st.write("### Jugadores disponibles")
st.dataframe(available_df, hide_index=True)

st.write("### Jugadores drafteados")
st.table(pd.DataFrame(st.session_state.drafted, columns=["name"]))



