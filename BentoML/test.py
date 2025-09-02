import bentoml

# Create a runner from your BentoML model
iris_clf_runner = bentoml.sklearn.get("iris_clf:latest").to_runner()

# Initialize locally
iris_clf_runner.init_local()

# Predict
print(iris_clf_runner.predict.run([[5.9, 3, 5.1, 1.8]]))
