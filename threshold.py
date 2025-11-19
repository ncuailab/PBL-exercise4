# === 異常値（しきい値超え）を NaN にするユーティリティ ===
def remove_abnormal_by_threshold(df_in):
    df = df_in.copy()

    # 磁場：|value| が 999 を超えたら NaN
    for c in ['B_mag[nT]', 'Bx_GSE[nT]', 'By_GSM[nT]', 'Bz_GSM[nT]']:
        if c in df.columns:
            if c == 'B_mag[nT]':
                df.loc[df[c] >= 999, c] = np.nan   # 大きさは負にならないので符号なしで判定
            else:
                df.loc[df[c].abs() >= 999, c] = np.nan  # 成分は負もあるので絶対値で判定

    # T_proton：9,999,999 を超えたら NaN
    if 'T_proton[K]' in df.columns:
        df.loc[df['T_proton[K]'] >= 9_999_999, 'T_proton[K]'] = np.nan

    # N_proton：999 を超えたら NaN
    if 'N_proton[cm^-3]' in df.columns:
        df.loc[df['N_proton[cm^-3]'] >= 999, 'N_proton[cm^-3]'] = np.nan

    # V_sw：9,999 を超えたら NaN
    if 'V_sw[km/s]' in df.columns:
        df.loc[df['V_sw[km/s]'] >= 9_999, 'V_sw[km/s]'] = np.nan

    # Flow_pressure（P）：99 を超えたら NaN
    if 'Flow_pressure[nPa]' in df.columns:
        df.loc[df['Flow_pressure[nPa]'] >= 99, 'Flow_pressure[nPa]'] = np.nan

    # E_field：999 を超えたら NaN
    if 'E_field[mV/m]' in df.columns:
        df.loc[df['E_field[mV/m]'] >= 999, 'E_field[mV/m]'] = np.nan

    # F10.7：999 を超えたら NaN
    if 'f10.7[sfu]' in df.columns:
        df.loc[df['f10.7[sfu]'] >= 999, 'f10.7[sfu]'] = np.nan

    # 他の物理量は異常値なし（そのまま）
    return df

# === ③：2000/01–2025/06（しきい値で異常値→NaN） ===
masked_df_all_clean = remove_abnormal_by_threshold(masked_df_all)
plot_period(masked_df_all_clean, start, end_all, '2000/01–2025/06 (cleaned)')

# === ④：2020–2024（しきい値で異常値→NaN） ===
masked_df_2024_clean = remove_abnormal_by_threshold(masked_df_2024)
plot_period(masked_df_2024_clean, start_2020, end_2024, '2020–2024 (cleaned)')


