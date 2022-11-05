from src.data import DATA_DIR
from src.chat_statistics.chat_statistics import ChatStatistics



if __name__ == '__main__':
    chat_data = ChatStatistics(file_path=DATA_DIR / 'CS-Stack.json')
    chat_data.generate_word_cloud(output_file_path=DATA_DIR)
    print("Done!")