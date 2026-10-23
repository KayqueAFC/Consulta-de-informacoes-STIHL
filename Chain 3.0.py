from pathlib import Path
import tkinter as tk
from tkinter import ttk

import pandas as pd
import pygame


# Arquivo de som (Na mesma pasta)
PASTA_APP = Path(__file__).resolve().parent
ARQUIVO_SOM = PASTA_APP / "motosserra.wav"
ARQUIVO_ICONE = PASTA_APP / "motosserra.png"


# Base de dados 
dados = [
    {"MODELO": "GTA 26", "SABRE": 10, "SABRE COD": "3007-003-0101", "ESPESSURA E PASSO": "1.1 - 1/4", "CORRENTE COD": "3670-000-0028", "CORRENTE": "27656", "METRO": "0,36", "DENTES": 14, "LIMA": 4.0, "LIMA COD": 14767, "ELOS": 28},
    {"MODELO": "MSA 120", "SABRE": 30, "SABRE COD": "3005-008-3405", "ESPESSURA E PASSO": "1.1 - 1/4", "CORRENTE COD": "3670-000-0064", "CORRENTE": "27656", "METRO": "0,81", "DENTES": 32, "LIMA": 4.0, "LIMA COD": 14767, "ELOS": 64},
    {"MODELO": "MSA 140", "SABRE": 30, "SABRE COD": "3005-008-3405", "ESPESSURA E PASSO": "1.1 - 1/4", "CORRENTE COD": "3670-000-0064", "CORRENTE": "27656", "METRO": "0,81", "DENTES": 32, "LIMA": 4.0, "LIMA COD": 14767, "ELOS": 64},
    {"MODELO": "MSA 160", "SABRE": 30, "SABRE COD": "3005-008-3405", "ESPESSURA E PASSO": "1.1 - 1/4", "CORRENTE COD": "3670-000-0064", "CORRENTE": "27656", "METRO": "0,81", "DENTES": 32, "LIMA": 4.0, "LIMA COD": 14767, "ELOS": 64},
    {"MODELO": "MSA 200", "SABRE": 35, "SABRE COD": "3005-008-3409", "ESPESSURA E PASSO": "1.1 - 1/4", "CORRENTE COD": "3670-000-0072", "CORRENTE": "27656", "METRO": "0,91", "DENTES": 36, "LIMA": 4.0, "LIMA COD": 14767, "ELOS": 72},
    {"MODELO": "HT 75", "SABRE": 30, "SABRE COD": "3005-008-3405", "ESPESSURA E PASSO": "1.1 - 1/4", "CORRENTE COD": "3670-000-0064", "CORRENTE": "27656", "METRO": "0,81", "DENTES": 32, "LIMA": 4.0, "LIMA COD": 14767, "ELOS": 64},
    {"MODELO": "HT 75", "SABRE": 30, "SABRE COD": "3005-000-3905", "ESPESSURA E PASSO": "1.1 - 3/8", "CORRENTE COD": "3610-000-0044", "CORRENTE": "34240", "METRO": "0,82", "DENTES": 22, "LIMA": 4.0, "LIMA COD": 14767, "ELOS": 44},
    {"MODELO": "HT 131", "SABRE": 30, "SABRE COD": "3005-000-3905", "ESPESSURA E PASSO": "1.1 - 3/8", "CORRENTE COD": "3610-000-0044", "CORRENTE": "34240", "METRO": "0,82", "DENTES": 22, "LIMA": 4.0, "LIMA COD": 14767, "ELOS": 44},
    {"MODELO": "HT 135", "SABRE": 30, "SABRE COD": "3005-000-3905", "ESPESSURA E PASSO": "1.1 - 3/8", "CORRENTE COD": "3610-000-0044", "CORRENTE": "34240", "METRO": "0,82", "DENTES": 22, "LIMA": 4.0, "LIMA COD": 14767, "ELOS": 44},
    {"MODELO": "MSE 141", "SABRE": 30, "SABRE COD": "3005-000-3905", "ESPESSURA E PASSO": "1.1 - 3/8", "CORRENTE COD": "3610-000-0044", "CORRENTE": "34240", "METRO": "0,82", "DENTES": 22, "LIMA": 4.0, "LIMA COD": 14767, "ELOS": 44},
    {"MODELO": "MSE 170", "SABRE": 30, "SABRE COD": "3005-000-4805", "ESPESSURA E PASSO": "1.1 - 3/8", "CORRENTE COD": "3613-000-0044", "CORRENTE": "34240", "METRO": "0,82", "DENTES": 22, "LIMA": 4.0, "LIMA COD": 14767, "ELOS": 44},
    {"MODELO": "MSA 220", "SABRE": 35, "SABRE COD": "3005-000-4809", "ESPESSURA E PASSO": "1.1 - 3/8", "CORRENTE COD": "3616-000-0050", "CORRENTE": "34240", "METRO": "0,93", "DENTES": 25, "LIMA": 4.0, "LIMA COD": 14767, "ELOS": 50},
    {"MODELO": "MSA 162", "SABRE": 30, "SABRE COD": "3005-008-4905", "ESPESSURA E PASSO": "1.1 - 3/8", "CORRENTE COD": "3610-000-0044", "CORRENTE": "34240", "METRO": "0,82", "DENTES": 22, "LIMA": 4.0, "LIMA COD": 14767, "ELOS": 44},
    {"MODELO": "MS 170", "SABRE": 30, "SABRE COD": "3005-000-3905", "ESPESSURA E PASSO": "1.1 - 3/8", "CORRENTE COD": "3610-000-0044", "CORRENTE": "34240", "METRO": "0,82", "DENTES": 22, "LIMA": 4.0, "LIMA COD": 14767, "ELOS": 44},
    {"MODELO": "MS 170", "SABRE": 40, "SABRE COD": "3005-000-3905", "ESPESSURA E PASSO": "1.1 - 3/8", "CORRENTE COD": "3610-000-0044", "CORRENTE": "34240", "METRO": "1,02", "DENTES": "27 + 1 ELO", "LIMA": 4.0, "LIMA COD": 14767, "ELOS": 55},
    {"MODELO": "MS 172", "SABRE": 35, "SABRE COD": "3005-000-3905", "ESPESSURA E PASSO": "1.1 - 3/8", "CORRENTE COD": "3610-000-0050", "CORRENTE": "34240", "METRO": "0,93", "DENTES": 25, "LIMA": 4.0, "LIMA COD": 14767, "ELOS": 50},
    {"MODELO": "MS 172 C-BE", "SABRE": 35, "SABRE COD": "3005-000-3909", "ESPESSURA E PASSO": "1.1 - 3/8", "CORRENTE COD": "3610-000-0050", "CORRENTE": "34240", "METRO": "0,93", "DENTES": 25, "LIMA": 4.0, "LIMA COD": 14767, "ELOS": 50},
    {"MODELO": "MS 180", "SABRE": 30, "SABRE COD": "3005-000-3905", "ESPESSURA E PASSO": "1.1 - 3/8", "CORRENTE COD": "3610-000-0044", "CORRENTE": "34240", "METRO": "0,82", "DENTES": 22, "LIMA": 4.0, "LIMA COD": 14767, "ELOS": 44},
    {"MODELO": "MS 180", "SABRE": 35, "SABRE COD": "3005-000-3909", "ESPESSURA E PASSO": "1.1 - 3/8", "CORRENTE COD": "3610-000-0050", "CORRENTE": "34240", "METRO": "0,93", "DENTES": 25, "LIMA": 4.0, "LIMA COD": 14767, "ELOS": 50},
    {"MODELO": "MS 182", "SABRE": 40, "SABRE COD": "3005-000-4813", "ESPESSURA E PASSO": "1.1 - 3/8", "CORRENTE COD": "3636-000-0055", "CORRENTE": "34240", "METRO": "1,02", "DENTES": "27 + 1 ELO", "LIMA": 4.0, "LIMA COD": 14767, "ELOS": 55},
    {"MODELO": "MS 193 T", "SABRE": 30, "SABRE COD": "3005-000-3905", "ESPESSURA E PASSO": "1.1 - 3/8", "CORRENTE COD": "3610-000-0044", "CORRENTE": "34240", "METRO": "0,82", "DENTES": 22, "LIMA": 4.0, "LIMA COD": 14767, "ELOS": 44},
    {"MODELO": "MS 194 T", "SABRE": 30, "SABRE COD": "3005-000-3905", "ESPESSURA E PASSO": "1.1 - 3/8", "CORRENTE COD": "3610-000-0044", "CORRENTE": "34240", "METRO": "0,82", "DENTES": 22, "LIMA": 4.0, "LIMA COD": 14767, "ELOS": 44},
    {"MODELO": "MS 210", "SABRE": 30, "SABRE COD": "3005-000-4805", "ESPESSURA E PASSO": "1.3 - 3/8", "CORRENTE COD": "3613-000-0050", "CORRENTE": "18331", "METRO": "0,82", "DENTES": 22, "LIMA": 4.0, "LIMA COD": 14767, "ELOS": 44},
    {"MODELO": "MS 210", "SABRE": 35, "SABRE COD": "3005-000-4809", "ESPESSURA E PASSO": "1.3 - 3/8", "CORRENTE COD": "3613-000-0050", "CORRENTE": "18331", "METRO": "0,93", "DENTES": 25, "LIMA": 4.0, "LIMA COD": 14767, "ELOS": 50},
    {"MODELO": "MS 212", "SABRE": 40, "SABRE COD": "3005-000-4813", "ESPESSURA E PASSO": "1.3 - 3/8", "CORRENTE COD": "3636-000-0055", "CORRENTE": "18331", "METRO": "1,02", "DENTES": "27 + 1 ELO", "LIMA": 4.0, "LIMA COD": 14767, "ELOS": 55},
    {"MODELO": "MS 212", "SABRE": 45, "SABRE COD": "3005-000-4817", "ESPESSURA E PASSO": "1.3 - 3/8", "CORRENTE COD": "3636-000-0061", "CORRENTE": "18331", "METRO": "1,13", "DENTES": "30 + 1 ELO", "LIMA": 4.0, "LIMA COD": 14767, "ELOS": 61},
    {"MODELO": "MS 230", "SABRE": 35, "SABRE COD": "3005-000-4809", "ESPESSURA E PASSO": "1.3 - 3/8", "CORRENTE COD": "3613-000-0050", "CORRENTE": "18331", "METRO": "0,93", "DENTES": 25, "LIMA": 4.0, "LIMA COD": 14767, "ELOS": 50},
    {"MODELO": "MS 250", "SABRE": 35, "SABRE COD": "3005-000-4809", "ESPESSURA E PASSO": "1.3 - 3/8", "CORRENTE COD": "3613-000-0050", "CORRENTE": "18331", "METRO": "0,93", "DENTES": 25, "LIMA": 4.0, "LIMA COD": 14767, "ELOS": 50},
    {"MODELO": "MS 250", "SABRE": 40, "SABRE COD": "3005-000-4813", "ESPESSURA E PASSO": "1.3 - 3/8", "CORRENTE COD": "3613-000-0055", "CORRENTE": "18331", "METRO": "1,02", "DENTES": "27 + 1 ELO", "LIMA": 4.0, "LIMA COD": 14767, "ELOS": 55},
    {"MODELO": "MS 260", "SABRE": 32, "SABRE COD": "3003-000-5306", "ESPESSURA E PASSO": "1.6 - .325", "CORRENTE COD": "3639-000-0056", "CORRENTE": "Fechada: 29867 / Por metro: 37393", "METRO": "0,93", "DENTES": 28, "LIMA": 4.8, "LIMA COD": 46815, "ELOS": 56},
    {"MODELO": "MS 260", "SABRE": 40, "SABRE COD": "3003-008-6813", "ESPESSURA E PASSO": "1.6 - .325", "CORRENTE COD": "3639-000-0067", "CORRENTE": "37393", "METRO": "1,11", "DENTES": "33 + 1 ELO", "LIMA": 4.8, "LIMA COD": 46815, "ELOS": 67},
    {"MODELO": "MS 260", "SABRE": 33, "SABRE COD": "3003-001-9207", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3621-000-0052", "CORRENTE": "37393", "METRO": "0,97", "DENTES": 26, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 52},
    {"MODELO": "MS 260", "SABRE": 32, "SABRE COD": "3003-001-9406", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3621-000-0050", "CORRENTE": "18330", "METRO": "0,93", "DENTES": 25, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 50},
    {"MODELO": "MS 260", "SABRE": 40, "SABRE COD": "3003-001-9213", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3621-000-0060", "CORRENTE": "18330", "METRO": "1,12", "DENTES": 30, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 60},
    {"MODELO": "MS 260", "SABRE": 50, "SABRE COD": "3003-001-9221", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3621-000-0072", "CORRENTE": "18330", "METRO": "1,34", "DENTES": 36, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 72},
    {"MODELO": "MS 310", "SABRE": 33, "SABRE COD": "3003-001-9207", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3652-000-0052", "CORRENTE": "18330", "METRO": "0,97", "DENTES": 26, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 52},
    {"MODELO": "MS 310", "SABRE": 40, "SABRE COD": "3003-001-9413", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3652-000-0060", "CORRENTE": "18330", "METRO": "1,12", "DENTES": 30, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 60},
    {"MODELO": "MS 310", "SABRE": 50, "SABRE COD": "3003-001-9421", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3652-000-0072", "CORRENTE": "18330", "METRO": "1,34", "DENTES": 36, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 72},
    {"MODELO": "MS 361", "SABRE": 33, "SABRE COD": "3003-001-9207", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3621-000-0052", "CORRENTE": "18330", "METRO": "0,97", "DENTES": 26, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 52},
    {"MODELO": "MS 361", "SABRE": 40, "SABRE COD": "3003-001-9213", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3621-000-0060", "CORRENTE": "18330", "METRO": "1,12", "DENTES": 30, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 60},
    {"MODELO": "MS 361", "SABRE": 50, "SABRE COD": "3003-001-9421", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3621-000-0072", "CORRENTE": "18330", "METRO": "1,34", "DENTES": 36, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 72},
    {"MODELO": "MS 362 C-M", "SABRE": 33, "SABRE COD": "3003-001-9207", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3621-000-0052", "CORRENTE": "18330", "METRO": "0,97", "DENTES": 26, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 52},
    {"MODELO": "MS 362 C-M", "SABRE": 40, "SABRE COD": "3003-001-9213", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3621-000-0060", "CORRENTE": "18330", "METRO": "1,12", "DENTES": 30, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 60},
    {"MODELO": "MS 362 C-M", "SABRE": 50, "SABRE COD": "3003-001-9221", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3621-000-0072", "CORRENTE": "18330", "METRO": "1,34", "DENTES": 36, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 72},
    {"MODELO": "MS 382", "SABRE": 33, "SABRE COD": "3003-001-9207", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3621-000-0052", "CORRENTE": "18330", "METRO": "0,97", "DENTES": 26, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 52},
    {"MODELO": "MS 382", "SABRE": 32, "SABRE COD": "3003-001-9406", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3621-000-0050", "CORRENTE": "18330", "METRO": "0,93", "DENTES": 25, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 50},
    {"MODELO": "MS 382", "SABRE": 40, "SABRE COD": "3003-001-9213", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3621-000-0060", "CORRENTE": "18330", "METRO": "1,12", "DENTES": 30, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 60},
    {"MODELO": "MS 382", "SABRE": 40, "SABRE COD": "3003-001-9413", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3621-000-0060", "CORRENTE": "18330", "METRO": "1,12", "DENTES": 30, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 60},
    {"MODELO": "MS 382", "SABRE": 40, "SABRE COD": "3003-000-5213", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3621-000-0060", "CORRENTE": "18330", "METRO": "1,12", "DENTES": 30, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 60},
    {"MODELO": "MS 382", "SABRE": 50, "SABRE COD": "3003-001-9221", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3621-000-0072", "CORRENTE": "18330", "METRO": "1,34", "DENTES": 36, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 72},
    {"MODELO": "MS 460", "SABRE": 40, "SABRE COD": "3003-001-9213", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3652-000-0060", "CORRENTE": "18330", "METRO": "1,12", "DENTES": 30, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 60},
    {"MODELO": "MS 460", "SABRE": 50, "SABRE COD": "3003-001-9221", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3652-000-0072", "CORRENTE": "18330", "METRO": "1,34", "DENTES": 36, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 72},
    {"MODELO": "MS 460", "SABRE": 63, "SABRE COD": "3003-001-9431", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3652-000-0084", "CORRENTE": "18330", "METRO": "1,58", "DENTES": 42, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 84},
    {"MODELO": "MS 462", "SABRE": 40, "SABRE COD": "3003-001-9213", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3652-000-0060", "CORRENTE": "18330", "METRO": "1,12", "DENTES": 30, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 60},
    {"MODELO": "MS 462", "SABRE": 50, "SABRE COD": "3003-001-9221", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3652-000-0072", "CORRENTE": "18330", "METRO": "1,34", "DENTES": 36, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 72},
    {"MODELO": "MS 462", "SABRE": 63, "SABRE COD": "3003-001-9431", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3652-000-0084", "CORRENTE": "18330", "METRO": "1,58", "DENTES": 42, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 84},
    {"MODELO": "MS 660", "SABRE": 40, "SABRE COD": "3003-001-9213", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3621-000-0060", "CORRENTE": "18330", "METRO": "1,12", "DENTES": 30, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 60},
    {"MODELO": "MS 660", "SABRE": 50, "SABRE COD": "3003-001-9221", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3652-000-0072", "CORRENTE": "18330", "METRO": "1,34", "DENTES": 36, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 72},
    {"MODELO": "MS 660", "SABRE": 75, "SABRE COD": "3003-001-9241", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3652-000-0096", "CORRENTE": "18330", "METRO": "1,78", "DENTES": 48, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 96},
    {"MODELO": "MS 660", "SABRE": 63, "SABRE COD": "3003-001-5631", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3621-000-0084", "CORRENTE": "18330", "METRO": "1,58", "DENTES": 42, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 84},
    {"MODELO": "MS 651", "SABRE": 40, "SABRE COD": "3003-001-9213", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3621-000-0060", "CORRENTE": "18330", "METRO": "1,12", "DENTES": 30, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 60},
    {"MODELO": "MS 651", "SABRE": 50, "SABRE COD": "3003-001-9221", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3652-000-0072", "CORRENTE": "18330", "METRO": "1,34", "DENTES": 36, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 72},
    {"MODELO": "MS 651", "SABRE": 75, "SABRE COD": "3003-001-9241", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3652-000-0096", "CORRENTE": "18330", "METRO": "1,78", "DENTES": 48, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 96},
    {"MODELO": "MS 651", "SABRE": 63, "SABRE COD": "3003-001-5631", "ESPESSURA E PASSO": "1.6 - 3/8", "CORRENTE COD": "3621-000-0084", "CORRENTE": "18330", "METRO": "1,58", "DENTES": 42, "LIMA": 5.2, "LIMA COD": 14768, "ELOS": 84},
]

df = pd.DataFrame(dados)

# Opções completas, usadas quando nenhum filtro está selecionado.
TODOS_MODELOS = sorted(df["MODELO"].unique().tolist())
TODOS_SABRES = sorted(df["SABRE"].unique().tolist())
TODAS_ESPESSURAS = sorted(df["ESPESSURA E PASSO"].unique().tolist())


# Som da motosserra
tocando = False
som_motosserra = None

try:
    pygame.mixer.init()
    if ARQUIVO_SOM.exists():
        som_motosserra = pygame.mixer.Sound(str(ARQUIVO_SOM))
except pygame.error:
    som_motosserra = None


def tocar_motosserra():
    """Liga ou desliga o som em loop ao clicar no botão da motosserra."""
    global tocando

    if som_motosserra is None:
        return

    if tocando:
        som_motosserra.stop()
        tocando = False
    else:
        som_motosserra.play(-1)
        tocando = True


# Janela principal
root = tk.Tk()
root.title("Consulta de Corrente - Desenvolvido by Kayque A.")
root.geometry("480x600")
root.configure(bg="white")

cabecalho = tk.Label(
    root,
    text="Consulta de Corrente",
    font=("Segoe UI", 18, "bold"),
    bg="#FF7B00",
    fg="black",
    pady=10,
)
cabecalho.pack(fill="x")

frame = tk.Frame(root, bg="white")
frame.pack(fill="both", expand=True, padx=20, pady=20)
frame.grid_columnconfigure(1, weight=1)
frame.grid_rowconfigure(3, weight=1)

# Variáveis ligadas aos campos de seleção.
modelo_var = tk.StringVar()
sabre_var = tk.StringVar()
espessura_var = tk.StringVar()

# Modelo
tk.Label(frame, text="Modelo:", font=("Segoe UI", 11, "bold"), bg="white").grid(
    row=0, column=0, sticky="w", pady=5
)
modelo_cb = ttk.Combobox(
    frame, textvariable=modelo_var, values=TODOS_MODELOS, state="readonly", width=25
)
modelo_cb.grid(row=0, column=1, pady=5, sticky="ew")

# Sabre
tk.Label(frame, text="Sabre:", font=("Segoe UI", 11, "bold"), bg="white").grid(
    row=1, column=0, sticky="w", pady=5
)
sabre_cb = ttk.Combobox(
    frame, textvariable=sabre_var, values=TODOS_SABRES, state="readonly", width=25
)
sabre_cb.grid(row=1, column=1, pady=5, sticky="ew")

# Espessura e passo
tk.Label(frame, text="Espessura/Passo:", font=("Segoe UI", 11, "bold"), bg="white").grid(
    row=2, column=0, sticky="w", pady=5
)
espessura_cb = ttk.Combobox(
    frame,
    textvariable=espessura_var,
    values=TODAS_ESPESSURAS,
    state="readonly",
    width=25,
)
espessura_cb.grid(row=2, column=1, pady=5, sticky="ew")

# Text box branca 
resultado_txt = tk.Text(
    frame,
    height=12,
    wrap="word",
    font=("Segoe UI", 10),
    bg="#f9f9f9",
    relief="solid",
    bd=1,
)
resultado_txt.grid(row=3, column=0, columnspan=3, pady=15, sticky="nsew")
resultado_txt.config(state="disabled")


# Filtros e pesquisa 
def filtrar_dados(modelo="", sabre="", espessura=""):
    """Retorna somente os registros compatíveis com os filtros informados."""
    resultado = df

    if modelo:
        resultado = resultado[resultado["MODELO"] == modelo]
    if sabre:
        resultado = resultado[resultado["SABRE"] == int(sabre)]
    if espessura:
        resultado = resultado[resultado["ESPESSURA E PASSO"] == espessura]

    return resultado


def atualizar_filtros(event=None):
    """Atualiza cada lista usando as escolhas feitas nos outros campos."""
    modelo = modelo_var.get()
    sabre = sabre_var.get()
    espessura = espessura_var.get()

    # Cada lista considera os outros dois campos, mas não filtra por si mesma.
    # Assim, as opções continuam coerentes sem ficarem presas a uma seleção antiga.
    modelos_possiveis = filtrar_dados(sabre=sabre, espessura=espessura)
    sabres_possiveis = filtrar_dados(modelo=modelo, espessura=espessura)
    espessuras_possiveis = filtrar_dados(modelo=modelo, sabre=sabre)

    modelo_cb["values"] = sorted(modelos_possiveis["MODELO"].unique().tolist())
    sabre_cb["values"] = sorted(sabres_possiveis["SABRE"].unique().tolist())
    espessura_cb["values"] = sorted(espessuras_possiveis["ESPESSURA E PASSO"].unique().tolist())


def pesquisar():
    """Mostra os dados da corrente que corresponde às três seleções."""
    resultado_txt.config(state="normal")
    resultado_txt.delete("1.0", "end")

    modelo = modelo_var.get()
    sabre = sabre_var.get()
    espessura = espessura_var.get()

    if not modelo or not sabre or not espessura:
        resultado_txt.insert("end", "Selecione modelo, sabre e espessura/passo.")
        resultado_txt.config(state="disabled")
        return

    encontrados = filtrar_dados(modelo, sabre, espessura)

    if encontrados.empty:
        resultado_txt.insert("end", "Nenhum resultado encontrado.")
    else:
        linha = encontrados.iloc[0]
        texto = (
            f"Código sabre: {linha['SABRE COD']}\n"
            f"Código fábrica corrente: {linha['CORRENTE COD']}\n"
            f"Espessura e passo: {linha['ESPESSURA E PASSO']}\n\n"
            f"Elos: {linha['ELOS']}\n"
            f"Dentes: {linha['DENTES']}\n"
            f"Metragem de corte: {linha['METRO']}\n"
            f"Código corrente: {linha['CORRENTE']}\n\n"
            f"Lima: {linha['LIMA']}\n"
            f"Código da lima: {linha['LIMA COD']}\n"
        )
        resultado_txt.insert("end", texto)

    resultado_txt.config(state="disabled")


def limpar():
    """Limpa a tela e volta a mostrar todas as opções nos campos."""
    modelo_var.set("")
    sabre_var.set("")
    espessura_var.set("")

    # Recalcula as listas sem filtros; correção de bug.
    atualizar_filtros()

    resultado_txt.config(state="normal")
    resultado_txt.delete("1.0", "end")
    resultado_txt.config(state="disabled")


def rocadeiras():
    """Área reservada para a consulta de roçadeiras."""
    resultado_txt.config(state="normal")
    resultado_txt.delete("1.0", "end")
    resultado_txt.insert("end", "Consulta de Roçadeiras em desenvolvimento...")
    resultado_txt.config(state="disabled")


# Atualiza as opções sempre que uma seleção muda.
modelo_cb.bind("<<ComboboxSelected>>", atualizar_filtros)
sabre_cb.bind("<<ComboboxSelected>>", atualizar_filtros)
espessura_cb.bind("<<ComboboxSelected>>", atualizar_filtros)


# Calculadora
def abrir_calculadora():
    calc_win = tk.Toplevel(root)
    calc_win.title("Calculadora de Corrente")
    calc_win.configure(bg="white")
    calc_win.geometry("330x300")

    tk.Label(
        calc_win,
        text="Calculadora de Corrente",
        font=("Segoe UI", 16, "bold"),
        bg="#FF7B00",
        fg="black",
        pady=10,
    ).pack(fill="x")

    frame_calc = tk.Frame(calc_win, bg="white")
    frame_calc.pack(fill="both", expand=True, padx=20, pady=20)

    tk.Label(frame_calc, text="Número de elos:", font=("Segoe UI", 11, "bold"), bg="white").grid(
        row=0, column=0, sticky="w", pady=5
    )
    elos_var = tk.StringVar()
    tk.Entry(frame_calc, textvariable=elos_var, width=20).grid(row=0, column=1, pady=5)

    tk.Label(frame_calc, text="Espessura/Passo:", font=("Segoe UI", 11, "bold"), bg="white").grid(
        row=1, column=0, sticky="w", pady=5
    )
    passo_var = tk.StringVar()
    ttk.Combobox(
        frame_calc,
        textvariable=passo_var,
        values=["1.1 - 1/4", "1.1 - 3/8", "1.3 - 3/8", "1.6 - .325", "1.6 - 3/8"],
        state="readonly",
        width=20,
    ).grid(row=1, column=1, pady=5)

    resultado_lbl = tk.Label(frame_calc, text="", font=("Segoe UI", 11), bg="white", fg="black")
    resultado_lbl.grid(row=2, column=0, columnspan=2, pady=10)

    def calcular():
        # A regra de cálculo dessa tela precisa ser definida antes de calcular o comprimento.
        if not elos_var.get().strip() or not passo_var.get():
            resultado_lbl.config(text="Informe os elos e selecione o passo.")
            return
        resultado_lbl.config(text="Cálculo em desenvolvimento.")

    tk.Button(
        frame_calc,
        text="Calcular",
        command=calcular,
        bg="#FF7B00",
        fg="black",
        font=("Segoe UI", 11, "bold"),
        width=12,
    ).grid(row=3, column=0, columnspan=2, pady=15)


# Botões da tela principal
btn_frame = tk.Frame(frame, bg="white")
btn_frame.grid(row=4, column=0, columnspan=3, pady=20, sticky="ew")

estilo_botao = {
    "bg": "#FF7B00",
    "fg": "black",
    "font": ("Segoe UI", 11, "bold"),
    "width": 12,
}

tk.Button(btn_frame, text="Pesquisar", command=pesquisar, **estilo_botao).grid(
    row=0, column=0, padx=10, pady=10
)
tk.Button(btn_frame, text="Limpar", command=limpar, **estilo_botao).grid(
    row=1, column=0, padx=10, pady=10
)
tk.Button(btn_frame, text="Roçadeiras", command=rocadeiras, **estilo_botao).grid(
    row=0, column=1, padx=10, pady=10
)
tk.Button(btn_frame, text="Outros", command=abrir_calculadora, **estilo_botao).grid(
    row=1, column=1, padx=10, pady=10
)

# Icon som da motossera.
try:
    motosserra_img = tk.PhotoImage(file=str(ARQUIVO_ICONE))
    btn_motosserra = tk.Button(
        btn_frame,
        text="",
        image=motosserra_img,
        command=tocar_motosserra,
        bg="#FF7B00",
        relief="raised",
        bd=2,
        width=90,
        height=45,
    )
except tk.TclError:
    motosserra_img = None
    btn_motosserra = tk.Button(
        btn_frame,
        text="Som",
        command=tocar_motosserra,
        **estilo_botao,
    )

btn_motosserra.grid(row=0, column=2, rowspan=2, padx=10, pady=10, sticky="nsew")

# Deixa os botões alinhados quando a janela muda de tamanho.
for coluna in range(3):
    btn_frame.grid_columnconfigure(coluna, weight=1)

root.mainloop()
