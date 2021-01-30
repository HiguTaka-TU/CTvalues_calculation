# CT画像(線減弱係数マップ)を処理するプログラム  

## CT値を計算し、CSVファイルにまとめる  
Gammexファントムの各インサートの平均CT値を計算する  
Recon_{data_size}のディレクトリに再構成画像を保存しておく  
計算されたCT値はCSVファイルに保存される  
`$python CTvalues.py`  
なお、画像自体をCT画像に変更したい場合は、convert='True'に変えておけばCTimagesのディレクトリにCT画像が保存される  

## CT画像(μマップ)からSNRを計算し、CSV、図に出力  
Gammexファントムの中心部のピクセルを取得し、SNRを計算する  
Recon_{data_size}のディレクトリに再構成画像を保存しておく
計算されたSNRはCSVファイルにまとめられ、プロットされた図とともに出力される  
`$python SNR.py`

## CT画像のCT値と電子密度の関係を図に出力  
デジタルGammexファントムと実際のGammexファントムの電子密度とCT値の関係(CT to Density curve)を図に保存する  
`$CTtoDensity.py`   

## RMSEなどの評価指標を図に出力  
RMSEやMAEなどのテキストファイルに保存された評価指標の数値を図に保存する  
`$evaluation.py`
