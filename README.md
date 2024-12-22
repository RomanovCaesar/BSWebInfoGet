# BSWebInfoGet

---

# BeautifulSoup 爬取网页内容并保存为文本文件

这个 Python 程序使用 `BeautifulSoup` 爬取网页上的所有文字内容和链接，并将其保存到一个 `.txt` 文件中。适用于需要爬取中小型网页文本信息和链接的场景。

## 功能
- 爬取指定网页的 **所有文字内容**（包含网页中所有文本信息）。
- 爬取并保存网页中的 **所有超链接**（包括链接的文字和 URL）。
- 将爬取到的信息保存为一个 `.txt` 文件。

## 环境要求
- Python 3.x
- `requests` 库
- `beautifulsoup4` 库

## 安装依赖

在运行程序前，请确保您已安装所需的 Python 库。可以使用以下命令安装：

```bash
pip install requests beautifulsoup4
```

## 使用方法

1. 下载该程序并解压（如果下载的是压缩包）。
2. 在终端/命令行中运行以下命令启动程序：
   
   ```bash
   python BSWebInfoGet.py
   ```

3. 程序启动后，输入您想要爬取的网页 URL（例如：`https://caesaugu.com/hosthatch%E7%91%9E%E5%A3%AB%E8%8B%8F%E9%BB%8E%E4%B8%96vps%E6%B5%8B%E8%AF%84`）。

4. 程序将会：
   - 获取该网页的内容。
   - 解析网页上的所有文字和链接。
   - 将解析的内容保存到 `webpage_full_info.txt` 文件中。
   - 输出网页标题、文本内容和链接（链接包括文字和 URL）到文件中。

## 输出示例

程序将输出一个 `.txt` 文件，其中包含网页的以下内容：
1. 网页标题
2. 网页的所有文字内容（按段落分隔）
3. 网页的所有超链接（包含链接文字及链接 URL）

文件内容示例（`webpage_full_info.txt`）：

```
网页标题: HostHatch瑞士苏黎世VPS测评 – Caesar小站

网页所有文字内容:
HostHatch瑞士苏黎世VPS测评 – Caesar小站
Caesar小站
HostHatch瑞士苏黎世VPS测评
4 月 1, 2024

网页所有链接:
1.  - https://caesaugu.com/
2. Caesar小站 - https://caesaugu.com
3. 4 月 1, 2024 - https://caesaugu.com/hosthatch%e7%91%9e%e5%a3%ab%e8%8b%8f%e9%bb%8e%e4%b8%96vps%e6%b5%8b%e8%af%84/
4. Caesar_311 - https://caesaugu.com/author/caesar_311/
...
```

## 代码解释

1. **fetch_webpage(url)**： 
   - 使用 `requests` 库发送 GET 请求获取网页 HTML 内容。
   
2. **parse_and_save_webpage(html_content, output_file)**： 
   - 使用 `BeautifulSoup` 解析网页内容。
   - 提取网页标题、所有文本内容和所有链接，并保存到 `.txt` 文件。

3. **程序输出**：
   - 网页标题、所有文本和链接信息被按顺序写入文本文件，便于后续处理和分析。

## 注意事项

- 确保目标网页没有反爬虫机制，或者您已采取适当的反反爬措施。
- 如果遇到 **验证码** 或 **动态加载** 内容，可能需要额外处理，例如使用 `Selenium` 等工具来模拟浏览器操作。
- 网页上的图片、视频等多媒体内容未被提取，程序只会提取文本和链接。

## 许可证

该项目使用 MIT 许可证。详情请参见 [LICENSE](LICENSE) 文件。

---

### 备注：
- 该程序默认将爬取到的网页内容保存到 `webpage_full_info.txt` 文件，您可以根据需要修改文件名。
