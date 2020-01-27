# Projekt PSI

Zadaniem w projekcie była eksploracja i analiza danych w zbiorze BIRAFFE: Bio-Reactions and Faces for Emotion-based Personalization.

W trakcie wykonywania ćwiczenia zbiór danych został poddany preprocessingowi w celu połączeniua wielu plików .csv w jeden.

### Opis pliku po preprocessingu


- sub_id - ID badanej osoby,
- iads_id - ID pliku dźwiękowego z bazy IADS,
- iaps_id - ID obrazu z bazy IAPS,

Emocje rozpoznane na twarzy badanej osoby: 
- anger - gniew [0-1],
- contempt - zadowolenie [0-1],
- disgust - obrzydzenie [0-1],
- fear - strach [0-1],
- happiness - radość [0-1],
- neutral - emocje neutralne [0-1],
- sadness - smutek [0-1],
- surprise - zaskoczenie [0-1],

Dane na temat obiektów z bazy IADS i IAPS:
- picture_valance,
- picture_arousal,
- sound_valance,
- sound_arousal,

Wyniki testu osobowości NEO-FFI
- openness,
- conscientiousness,
- extraversion,
- agreeableness,
- neurocism,

Dane uzyskane w badaniu Procedure:
- widget_type - typ udzielonej odpowiedzi,
- ans_time - czas potrzebny na udzielenie odpowiedzi [s] (100 gdy brak),
- emotion_ans - odpowiedź w przypadku *emoscale*,
- valence_ans - odpowiedź w przypadku *emospace*,
- arousal_ans - odpowiedź w przypadku *emospace*,

### Uzyskana korelacja

![correlation](https://raw.githubusercontent.com/Warzecha/BIRAFFE-Emotion-Analysis/master/img/correlation.png)
