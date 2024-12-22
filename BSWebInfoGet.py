import requests
from bs4 import BeautifulSoup

def fetch_webpage(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return None

def parse_and_save_webpage(html_content, output_file):
    soup = BeautifulSoup(html_content, 'html.parser')

    with open(output_file, "w", encoding="utf-8") as file:
        title = soup.title.string if soup.title else "无标题"
        file.write(f"网页标题: {title}\n\n")
        print(f"\n网页标题: {title}")

        file.write("网页所有文字内容:\n")
        print("\n网页所有文字内容:")
        text_content = soup.get_text(separator="\n", strip=True)
        file.write(text_content + "\n\n")
        print(text_content[:1000])

        file.write("网页所有链接:\n")
        print("\n网页所有链接:")
        links = soup.find_all('a', href=True)
        for i, link in enumerate(links, 1):
            url = link['href']
            text = link.get_text(strip=True)
            file.write(f"{i}. {text} - {url}\n")
            print(f"{i}. {text} - {url}")
    
    print(f"\n解析结果已保存到文件: {output_file}")

def main():
    url = input("请输入要爬取的网页URL: ").strip()
    output_file = "webpage_full_info.txt"

    html_content = fetch_webpage(url)
    if html_content:
        print("\n网页内容已成功获取，开始解析并保存到文件...")
        parse_and_save_webpage(html_content, output_file)
    else:
        print("无法获取网页内容，请检查URL或网络连接。")

if __name__ == "__main__":
    main()
