# Water Meter YOLO Labeler

A simple tool for labeling water meter images in YOLO format.

## What this tool does

This tool helps you:

- open a folder of images
- draw bounding boxes
- assign the correct class to each box
- move and resize boxes
- rotate images before labeling
- save labels in YOLO `.txt` format

---

## Supported classes

The tool uses the following classes:

- `meter`
- `window`
- `0`
- `1`
- `2`
- `3`
- `4`
- `5`
- `6`
- `7`
- `8`
- `9`
- `unknown`

---

## How to run the tool

Make sure Python and the required packages are installed.

### Install dependencies

```bash
pip install opencv-python PySide6
```

### Prepare dataset

Use the included script to build a clean YOLO dataset from labeled folders:

```bash
python3 -m scripts.02_prepare_dataset raw_dataset dataset
```

### Train (quick test)

Use the virtualenv Python to ensure installed packages (like `ultralytics`) are used.

Git Bash / MSYS:

```bash
./venv/Scripts/python scripts/03_train.py --data dataset/data.yaml --model yolov8n.pt --epochs 1 --imgsz 640 --batch 2 --name test_run
```

PowerShell (when `venv` activated):

```powershell
venv\Scripts\python.exe scripts/03_train.py --data dataset/data.yaml --model yolov8n.pt --epochs 1 --imgsz 640 --batch 2 --name test_run
```

If you prefer to run multiple epochs, increase `--epochs` and adjust `--batch` for your machine.

### Quick launcher helper

You can use the included helper to ensure scripts run with the project's virtualenv Python even if your `python3` points to the system interpreter:

```bash
# run by script name (looks for scripts/03_train.py)
python3 scripts/run.py 03_train --epochs 1 --data dataset/data.yaml --model yolov8n.pt --batch 2 --name quick_test

# or provide a full script path
python3 scripts/run.py scripts/05_retrain.py
```

The helper will detect `venv` and re-exec the appropriate Python interpreter automatically.

### Predict/Inference

Run predictions on test images using the trained model:

Git Bash / MSYS:

```bash
./venv/Scripts/python scripts/04_predict.py
```

PowerShell (when `venv` activated):

```powershell
venv\Scripts\python.exe scripts/04_predict.py
```

Or using the helper script:

```bash
python3 scripts/run.py 04_predict
```

The prediction script will:
- Automatically find the latest trained model (`best.pt`) from `training_runs/`
- Use images from `dataset/images/test/`
- Save annotated images with bounding boxes
- Save prediction `.txt` files in YOLO format
- Save confidence scores
- Output results to `prediction_outputs/test_predictions/`

**Custom prediction parameters:**

You can modify the prediction script to adjust:
- `CONFIDENCE`: Minimum confidence threshold (default: 0.25)
- `IMAGE_SIZE`: Input image size (default: 640)
- `SAVE_TXT`: Save prediction text files (default: True)
- `SAVE_CONF`: Save confidence scores (default: True)
