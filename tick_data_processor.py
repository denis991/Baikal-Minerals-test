import pandas as pd

def generate_ohlc(tick_data, time_range):
    # Чтение тиковых данных
    df = pd.read_csv(tick_data)

    # Преобразование даты и времени в формат datetime
    df['DATETIME'] = pd.to_datetime(df['<DATE>'].astype(str) + ' ' + df['<TIME>'].astype(str), format='%Y%m%d %H%M%S')

    # Установка даты и времени в качестве индекса
    df.set_index('DATETIME', inplace=True)

    # Ресемплирование данных на основе выбранного диапазона времени
    ohlc_data = df['<LAST>'].resample(time_range).ohlc()
    volume_data = df['<VOL>'].resample(time_range).sum()

    # Объединение OHLC-данных и объемов в один DataFrame
    ohlc_with_volume = pd.concat([ohlc_data, volume_data], axis=1)

    # Заполнение пропущенных значений нулями
    ohlc_with_volume.fillna(0, inplace=True)

    return ohlc_with_volume

# Пример использования функции
tick_data = 'GAZP_230310_230410.txt'
time_range = '15Min'

ohlc_data = generate_ohlc(tick_data, time_range)
print(ohlc_data)
