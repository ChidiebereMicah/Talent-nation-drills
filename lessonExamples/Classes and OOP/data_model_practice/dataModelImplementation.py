from sklearn.datasets import load_iris

"""
Build a class called:
Dataset

It represents a small collection of training samples.
Each sample is a dictionary:
For example:
samples = [
    {"text": "Python is great", "label": "positive"},
    {"text": "I dislike bugs", "label": "negative"},
    {"text": "Learning is fun", "label": "positive"},
]
"""

iris = load_iris()
# print(iris)
# print(type(iris))
# print(type(iris["data"]))
# print(iris["data"].shape)
# print(iris["data"][0])

# print(iris["feature_names"])
# print(iris["target"][0])
# print(iris["target_names"])
training_samples = [
    
]

features = [feature for feature in iris["feature_names"]]
specs = [spec for spec in iris["data"][0]]
flower_0 = {features[i]: specs[i] for i in range(len(features))}
flower_0["species"] = iris["target_names"][0]
print(flower_0)

"""
Your Dataset class should support the following Python behaviors.

A. Length
This should work:
len(dataset)
"""