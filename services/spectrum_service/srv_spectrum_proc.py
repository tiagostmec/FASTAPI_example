import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


def classify(f, Pxx):
    X = np.array([f, Pxx]).T
    y = np.random.randint(0, 2, size=len(X))  # Dummy target for demonstration
 
    '''
    Know bugs, sometimes, rand generate only 1 class. Need to investigate.
    '''
     # Ensure we have more than one class
    while len(np.unique(y)) < 2:
        y = np.random.randint(0, 2, size=len(X))

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Feature scaling
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # Train the SVM classifier
    classifier = SVC(kernel='linear', random_state=42)
    classifier.fit(X_train, y_train)

    # Predict the test set results
    y_pred = classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    return {"result": accuracy}  # Convertendo para float

