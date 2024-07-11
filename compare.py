import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def read_files(folder):
    files = {}
    for filename in os.listdir(folder):
        if filename.endswith('.py'):
            with open(os.path.join(folder, filename), 'r', encoding='utf-8') as file:
                files[filename] = file.read()
    return files


def compute_similarity_matrix(code_dict):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(code_dict.values())
    similarity_matrix = cosine_similarity(tfidf_matrix)
    return similarity_matrix


def normalize_matrix(matrix):
    min_val = np.min(matrix)
    max_val = np.max(matrix)
    if max_val - min_val != 0:
        return (matrix - min_val) / (max_val - min_val)
    return matrix


def find_outliers(similarity_matrix, threshold):
    median_value = np.median(similarity_matrix)
    outliers = []
    pre = 0
    k = similarity_matrix.shape[0]
    for i in range(k):
        count = 0
        for j in range(k):
            if similarity_matrix[i][j] < median_value:
                count += 1
        if count >= threshold:
            outliers.append(i)
            pre += 1
    print("pre is ", pre/30)
    return outliers


def main(test_folder, result_folder, threshold):
    test_files = read_files(test_folder)
    result_files = read_files(result_folder)

    if set(test_files.keys()) != set(result_files.keys()):
        raise ValueError("The files in test and result folders do not match.")

    code_dict = {filename: test_files[filename] + result_files[filename] for filename in test_files}
    similarity_matrix = compute_similarity_matrix(code_dict)
    normalized_matrix = normalize_matrix(similarity_matrix)
    outliers = find_outliers(normalized_matrix, threshold)

    print("Outliers indices:", outliers)
    # print(normalized_matrix)
    print("Outliers filenames:", [list(code_dict.keys())[i] for i in outliers])


if __name__ == "__main__":
    test_folder = 'test1'
    result_folder = 'result1'
    threshold = 10  # Adjust the threshold as needed
    main(test_folder, result_folder, threshold)