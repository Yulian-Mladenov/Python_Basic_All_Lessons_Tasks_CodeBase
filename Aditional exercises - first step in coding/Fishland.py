skumriq_cena = float(input())
caca_cena = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = float(input())

cena_na_midi = 7.50

total_cena_midi = midi_kg * cena_na_midi
total_cena_safrid = safrid_kg * (caca_cena + (caca_cena * 0.80))
total_cena_palamud = palamud_kg *(skumriq_cena + (skumriq_cena * 0.60))

suma_za_plastane = total_cena_palamud + total_cena_midi + total_cena_safrid

print("{:.2f}".format(suma_za_plastane))