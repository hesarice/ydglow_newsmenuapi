from flask import Flask, jsonify, request, abort
import os

app = Flask(__name__)

# 文件存储目录
FILE_DIRECTORY = r"C:\PycharmProjects\pachong\.venv"

# 确保目录存在
if not os.path.exists(FILE_DIRECTORY):
    os.makedirs(FILE_DIRECTORY)


# 读取文件内容的函数
def get_file_content(filename):
    try:
        file_path = os.path.join(FILE_DIRECTORY, filename)
        if not os.path.exists(file_path):
            return None
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return None


# API 路由：通过 GET 请求获取文件内容
@app.route('/api/get_file_content', methods=['GET'])
def get_file():
    filename = request.args.get('filename')

    if not filename:
        return jsonify({'error': 'Missing filename parameter'}), 400

    content = get_file_content(filename)

    if content is None:
        return jsonify({'error': 'File not found or could not be read'}), 404

    return jsonify({'filename': filename, 'content': content}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
