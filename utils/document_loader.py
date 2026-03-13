import os


def load_documents(folder_path):

    try:

        documents = []

        for filename in os.listdir(folder_path):

            if filename.endswith(".txt"):

                file_path = os.path.join(folder_path, filename)

                with open(file_path, "r", encoding="utf-8") as f:

                    text = f.read()

                documents.append({
                    "filename": filename,
                    "content": text
                })

        return documents

    except Exception as e:

        print("Document loading error:", e)

        return []