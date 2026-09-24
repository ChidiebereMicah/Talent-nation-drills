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
"""
    The iris dataset is obtained from the UCI Machine Learning Repository
    Its a dataset of flowers and their features
"""
# print(iris)
# print(type(iris))
# print(type(iris["data"]))
# print(iris["data"].shape)
# print(iris["data"][0])

# print(iris["feature_names"])
# print(iris["target"][0])
# print(iris["target_names"])

#to build a single flower
# features = [iris["feature_names"]
# specs = iris["data"][0]
# flower_0 = {features[i]: specs[i] for i in range(len(features))}
# flower_0["species"] = iris["target_names"][0]
# print(flower_0)

#helper fn to build any flower for any given index
def make_flower(iris, index):
    flower = {feature.replace(' (cm)', '').replace(' ', '_'):float(value) for feature, value in zip(iris['feature_names'], iris['data'][index])}
    flower['species'] = str(iris['target_names'][iris['target'][index]])
    return flower

print(flower_0 := make_flower(iris, 0))
print(flower_50 := make_flower(iris, 50))
print(flower_100 := make_flower(iris, 100))

#Building the full dataset from iris
samples = [make_flower(iris, index) for index in range(len(iris['data']))]
print(samples)
"""
Your Dataset class should support the following Python behaviors.

A. Length
This should work:
len(dataset)
"""
class Dataset:
    def __init__(self, samples):
        self.samples = samples

    def __len__(self, samples):

