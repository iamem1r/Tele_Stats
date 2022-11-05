from src.data import DATA_DIR
from src.chat_statistics.chat_statistics import ChatStatistics



if __name__ == '__main__':
    chat_data = ChatStatistics(file_path=DATA_DIR / 'CS-Stack.json')
    print("Done!")