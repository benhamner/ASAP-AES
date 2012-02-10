#!/usr/bin/env python2.7

import re
from sklearn.ensemble import RandomForestRegressor

def add_essay_training(data, essay_set, essay, score):
    if essay_set not in data:
        data[essay_set] = {"essay":[],"score":[]}
    data[essay_set]["essay"].append(essay)
    data[essay_set]["score"].append(score)

def add_essay_test(data, essay_set, essay, prediction_id):
    if essay_set not in data:
        data[essay_set] = {"essay":[], "prediction_id":[]}
    data[essay_set]["essay"].append(essay)
    data[essay_set]["prediction_id"].append(prediction_id)

def read_training_data(training_file):
    f = open(training_file)
    f.readline()

    training_data = {}
    for row in f:
        row = row.strip().split("\t")
        essay_set = row[1]
        essay = row[2]
        domain1_score = int(row[6])
        if essay_set == "2":
            essay_set = "2_1"
        add_essay_training(training_data, essay_set, essay, domain1_score)
        
        if essay_set == "2_1":
            essay_set = "2_2"
            domain2_score = int(row[9])
            add_essay_training(training_data, essay_set, essay, domain2_score)
    
    return training_data

def read_test_data(test_file):
    f = open(test_file)
    f.readline()

    test_data = {}
    for row in f:
        row = row.strip().split("\t")
        essay_set = row[1]
        essay = row[2]
        domain1_predictionid = int(row[3])
        if essay_set == "2": 
            domain2_predictionid = int(row[4])
            add_essay_test(test_data, "2_1", essay, domain1_predictionid)
            add_essay_test(test_data, "2_2", essay, domain2_predictionid)
        else:
            add_essay_test(test_data, essay_set, essay, domain1_predictionid)
    return test_data

def get_character_count(essay):
    return len(essay)

def get_word_count(essay):
    return len(re.findall(r"\s", essay))+1

def extract_features(essays, feature_functions):
    return [[f(es) for f in feature_functions] for es in essays]

def main():
    print("Reading Training Data")
    training = read_training_data("../Data/training_set_rel3.tsv")
    print("Reading Validation Data")
    test = read_test_data("../Data/valid_set.tsv")
    
    feature_functions = [get_character_count, get_word_count]

    essay_sets = sorted(training.keys())
    predictions = {}

    for es_set in essay_sets:
        print("Making Predictions for Essay Set %s" % es_set)
        features = extract_features(training[es_set]["essay"],
                                    feature_functions)
        rf = RandomForestRegressor(n_estimators = 100)
        rf.fit(features,training[es_set]["score"])
        features = extract_features(test[es_set]["essay"], feature_functions)
        predicted_scores = rf.predict(features)
        for pred_id, pred_score in zip(test[es_set]["prediction_id"], 
                                       predicted_scores):
            predictions[pred_id] = round(pred_score)
    
    output_file = "../Submissions/length_benchmark.csv"
    print("Writing submission to %s" % output_file)
    f = open(output_file, "w")
    f.write("prediction_id,predicted_score\n")
    for key in sorted(predictions.keys()):
        f.write("%d,%d\n" % (key,predictions[key]))
    f.close()
    
if __name__=="__main__":
    main()
