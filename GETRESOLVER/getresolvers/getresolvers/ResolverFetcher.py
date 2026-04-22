# -*- coding: utf-8 -*-

import logging
import requests

def main():
    logging.basicConfig(format="%(message)s", level=logging.INFO)
    logging.info(r"""
            __                   __
  ___ ____ / /________ ___ ___  / /  _____ _______
 / _ `/ -_) __/ __/ -_|_-</ _ \/ / |/ / -_) __(_-<
 \_, /\__/\__/_/  \__/___/\___/_/|___/\__/_/ /___/
/___/
    """)
 
    logging.info("🔍 Fetching resolvers\n")

    resolvers_source = "https://raw.githubusercontent.com/devanshbatham/getresolvers/main/resolvers.txt"

    try:
        response = requests.get(resolvers_source, timeout=10)
        response.raise_for_status()  # Handle bad responses
    except requests.exceptions.RequestException as e:
        logging.error(f"❌ Error fetching resolvers: {e}")
        return

    with open("resolvers.txt", "w") as f:
        f.write(response.text)

    with open("resolvers.txt", "r") as f:
        resolvers_list = f.read().splitlines()

    for resolver in resolvers_list:
        print(resolver)

    logging.info(f"\n✅ Resolvers found : {len(resolvers_list)}")
    logging.info("✅ Output saved in resolvers.txt")

if __name__ == "__main__":
    main()