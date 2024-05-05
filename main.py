import csv
import json
import time


def process_csv(input_file, output_file):
    qa_pairs = []

    with open(input_file, 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter='\t')

        for row in reader:
            group_id = row[0]
            headline = row[1].strip('"')
            question = row[2]
            answer = "Yes" if row[3] == "1" else "No"
            qes_class = row[4]

            unique_id = f"QA_{len(qa_pairs) + 1}"

            qa_pair = {
                "id": unique_id,
                "GroupId": group_id,
                "Headline": headline,
                "Question": question,
                "Answer": answer,
                "QuestionClass": qes_class
            }

            qa_pairs.append(qa_pair)

    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(qa_pairs, json_file, ensure_ascii=False, indent=2)

    return len(qa_pairs)


start_time = time.time()
train_len = process_csv('train.csv', 'train.json')
test_len = process_csv('test.csv', 'test.json')
end_time = time.time()

processing_time = end_time - start_time
print("数据集清理和转换所需的时间:", processing_time, "秒")
print("从数据集中提取的问题-答案对的总数:", train_len + test_len, "对")
