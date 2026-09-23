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

print(iris["feature_names"])
print(iris["target"][0])
print(iris["target_names"])
training_samples = [
    
]


"""
Your Dataset class should support the following Python behaviors.

A. Length
This should work:
len(dataset)
"""