from mongoengine import connect
import configparser

#read config file for DB key safety
config = configparser.ConfigParser()
config.read("configs/config.ini")

mongo_user = config.get("DB", "user")
mongodb_pass = config.get("DB", "pass")
domain = config.get("DB", "domain")


if __name__ == "__main__":
    #check connection to DB
    try:
        connect(
            host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/?retryWrites=true&w=majority""",
            ssl=True,
        )
        print("Connected to DB")
    except Exception as e:
        print("Error: ", e)
