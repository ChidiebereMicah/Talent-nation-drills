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
# print(flower_0 := make_flower(iris, 0))
# print(flower_50 := make_flower(iris, 50))
# print(flower_100 := make_flower(iris, 100))

#Building the full dataset from iris
samples = [make_flower(iris, index) for index in range(len(iris['data']))]
#print(samples)
"""
Your Dataset class should support the following Python behaviors.

A. Length
This should work:
len(dataset)
"""
class Dataset:
    def __init__(self, samples):
        self._samples = list(samples)

    def __len__(self):
        return len(self._samples)

    """
    B. Indexing
    This should work:

    dataset[0]
    dataset[1]
    dataset[-1]
    """
    def __getitem__(self, key):
        return self._samples[key]

    """
    C. Iteration

    This should work:

    for sample in dataset:
        print(sample)
    """
    def __iter__(self):
        for sample in self._samples:
            yield sample

    """
    D. Membership

    Make this work:

    sample in dataset
    """
    def __contains__(self, item):
        return item in self._samples

    """
    Make:

    print(dataset)

    produce something useful, such as:
    Dataset(samples=3)
    """
    def __str__(self):
        return f"Dataset(samples={len(self._samples)})"

    """And make repr(dataset) developer-friendly with:
    __repr__
    """
    def __repr__(self):
        return f"Dataset(n_samples={len(self._samples)})"

    """
    Two Dataset objects should be considered equal when their samples are equal and in the same order:

    dataset1 == dataset2

    Implement:
    __eq__
    """
    def __eq__(self, value):
        if not isinstance(value, Dataset):
                return NotImplemented
        return value._samples == self._samples

"""
Write a function:

def summarize_dataset(dataset):

It should accept anything that satisfies the relevant protocols, not specifically a Dataset.

It should return information such as:

Number of samples: 3
First sample: {...}
"""
def summarize_dataset(dataset):
    return (f"Number of samples: {len(dataset)}\n"
            f"First sample: {dataset[0]}\n"
            f"{dataset!r}"
    )
            
dataset = Dataset(samples)
dataset1 = Dataset(samples)
dataset2 = Dataset(samples)

print(len(dataset))
print(dataset[0])
print(dataset[-1])
print(dataset == Dataset(samples))
print(dataset1 == dataset2)
print(samples[0] in dataset)
print(dataset)

print("--------------------------------------\n--------------------------------------")
print(summarize_dataset(dataset))

print(dataset[0:10])

print(dataset[::-1][0])
print(type(iter(dataset)))

iterator = iter(dataset)
print(next(iterator)) #prints 1st dict in samples
print(next(iterator)) #prints 2nd dict in samples

print(dataset == 42)