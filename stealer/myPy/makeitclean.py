import shutil

def delete_all():
    try:   
        shutil.rmtree("C:\\Min")
    except Exception as e:
        print(f"An error occurred: {e}")