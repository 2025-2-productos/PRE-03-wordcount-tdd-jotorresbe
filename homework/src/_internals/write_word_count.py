import os


def write_word_count(output_folder, word_counts):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # save the results using tsv format
    output_path = os.path.join(output_folder, "wordcount.tsv")
    with open(output_path, "w", encoding="utf-8") as f:
        for key, value in word_counts.items():
            # write the key and value to the file
            f.write(f"{key}\t{value}\n")
