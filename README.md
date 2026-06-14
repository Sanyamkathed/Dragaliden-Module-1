# Wind Farm Forecasting Pipeline



## Structure

```text
Final_code/
  main.py
  scripts/
    train.py
  src/
    wind_farm_forecast/
      config.py
      constants.py
      pipeline.py
      data/
      features/
      analysis/
      evaluation/
      models/
        ml/
        dl/
      visualization/
      persistence/
      reporting/
```

## Run

Synthetic quick run without deep learning or autoregression:

```powershell
python main.py --synthetic --skip_dl --skip_ar
```

Real CSV data:

```powershell
python main.py --data_dir C:\path\to\csv_files --output_dir .\results
```

Install dependencies if needed:

```powershell
pip install -r requirements.txt
```
