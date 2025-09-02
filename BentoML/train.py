import bentoml

from sklearn import datasets, svm

# Load training data set
iris = datasets.load_iris()
X, y = iris.data, iris.target

# Train the model
clf = svm.SVC(gamma = "scale")
clf.fit(X, y)

# Save the model to the BentoML local model store
saved_model = bentoml.sklearn.save_model("iris_clf:latest", clf)
print(f"Model Saved: {saved_model}")


## iris_clf:ifhkak3xbwbqebhn