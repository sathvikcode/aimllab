# MCA 3rd Semester Python Lab Programs

Programs are arranged in the same order as the 3rd Semester Lab Manual.

## Folder guide
- `Program-1/` — 1(a) to 1(h)
- `Program-2/` — Supervised and Unsupervised Learning
- `Program-3/` — ID3 Decision Tree
- `Program-4/` — ANN with Backpropagation
- `Program-5/` — Naive Bayes Email Spam Classification
- `Program-6/` — Naive Bayes News Classification
- `Program-7/` — Heart Disease Classification (Gaussian Naive Bayes, as in the manual)
- `Program-8/` — K-Means Employee Clustering
- `Program-9/` — KNN Iris Classification
- `Program-10/` — Locally Weighted Regression

## Setup in VS Code

1. Install Python and the VS Code Python extension.
2. Open this folder in VS Code.
3. Open Terminal → New Terminal.
4. Install common packages:

```bash
python -m pip install pandas numpy scikit-learn matplotlib statsmodels
```

5. For Program 4 only, install TensorFlow separately if your Python version/platform supports it:

```bash
python -m pip install tensorflow
```

6. Run a program from its own folder:

```bash
python filename.py
```

## Dataset note

The lab manual refers to CSV files, but does not include the actual CSV datasets.
Place each required CSV in the same folder as its Python program. The required file names
and columns are mentioned in the README inside each program folder.

## Calculator note

Program 1(d) has two Python files. Keep `calculator.py` and `main.py` in the same folder,
then run `python main.py`.

## GitHub: get only one program folder

After you create a GitHub repository and push this project once, you can download only
the folder you need with sparse checkout:

```bash
git clone --filter=blob:none --sparse https://github.com/YOUR-USERNAME/MCA-3rd-Sem-Lab.git
cd MCA-3rd-Sem-Lab
git sparse-checkout set Program-5
```

Replace `Program-5` with `Program-1`, `Program-2`, etc.

To switch to another program later:

```bash
git sparse-checkout set Program-8
```

To update the selected folder with the latest GitHub changes:

```bash
git pull
```

If you want multiple folders:

```bash
git sparse-checkout set Program-1 Program-4 Program-5
```
