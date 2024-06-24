from telethon import TelegramClient, errors
from loaders import load_accounts, load_channels


def auth_accounts(accounts_data):
    for account in accounts_data:
        print(f"Авторизация аккаунта с номеров: {account['phone']}...")
        client = TelegramClient(f"sessions/{account['phone']}", account["api_id"], account["api_hash"])
        try:
            client.start(phone=account['phone'])
            print("Авторизация пройдена.")
        except Exception as ex:
            print(f"Ошибка при авторизации: {ex}")
        finally:
            client.disconnect()


async def send_msg_to_channel():
    pass


if __name__ == "__main__":
    data_accounts = load_accounts()
    auth_accounts(data_accounts)
