def load_accounts() -> list:
    try:
        accounts = []
        with open("data/accounts.txt", "r") as file:
            for line in file:
                api_id, api_hash, phone = line.strip().split(";")
                accounts.append({
                    "api_id": int(api_id),
                    "api_hash": api_hash,
                    "phone": phone
                })
        return accounts
    except FileNotFoundError:
        print("Файл accounts.txt не найден.")
    except Exception as ex:
        print(f"Не удалось прочитать файл с данными аккаунтов. Ошибка: {ex}")


def load_channels() -> list:
    try:
        with open("data/channels.txt", "r") as file:
            channels = [line.strip() for line in file]
        return channels
    except FileNotFoundError:
        print("Файл channels.txt не найден.")
    except Exception as ex:
        print(f"Не удалось прочитать файл с каналами. Ошибка: {ex}")