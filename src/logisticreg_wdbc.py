import logisticreg
import csv
import numpy as np

if __name__ == "__main__":
    n_test = 100
    data = []
    """
    X = []
    y = []
    """
    with open("wdbc.data") as fp:
        for row in csv.reader(fp):
            data.append(row)
    """
            if row[1] == "B":
                y.append(0)
            else:
                y.append(1)
            X.append(row[2:])
    """
    X = []
    y = []    
    np.random.seed(3)
    np.random.shuffle(data)
    for row in data:
        # row = data[i]
        if row[1] == "B":
            y.append(0)
        else:
            y.append(1)
        X.append(row[2:])
    
    X = np.array(X, dtype=np.float64)
    y = np.array(y, dtype=np.float64)
    X_train = X[:-n_test]
    y_train = y[:-n_test]
    X_test = X[-n_test:]
    y_test = y[-n_test:]
    model = logisticreg.LogisticRegression(tol=0.01)
    model.fit(X_train, y_train)
    y_predict = model.predict(X_test)
    n_hits = (y_test == y_predict).sum()
    print("Accuracy: {}/{}={}".format(n_hits, n_test, n_hits / n_test))    
