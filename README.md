# CT画像(線減弱係数マップ)を処理するプログラム  

## CT値を計算し、CSVファイルにまとめる  
Gammexファントムの各インサートの平均CT値を計算する  
Recon_{data_size}のディレクトリに再構成画像を保存しておく  
計算されたCT値はCSVファイルに保存される  
`$python CTvalues.py`  
なお、画像自体をCT画像に変更したい場合は、convert='True'に変えておけばCTimagesのディレクトリにCT画像が保存される  

