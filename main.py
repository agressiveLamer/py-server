import socket


class SOCKET:
    def __init__(self):
        self.server_start_func()

    def server_start_func(self):
        try:
            """Запуск серввера"""
            self.server = socket.socket(socket.AF_INET,
                                        socket.SOCK_STREAM)
            self.server.bind(('127.0.0.1', 3334))
            self.server.listen(500)
            while True:
                print('Сервер запущен...')
                """Ожидание запроса"""
                self.client_socket, self.address = self.server.accept()
                """Обработка запроса"""
                self.data = self.client_socket.recv(1024).decode('utf-8')
                # print(self.data)
                """Отправка ответа"""
                self.answer_content = self.load_page_from_get(self.data)
                self.client_socket.send(self.answer_content)
                self.client_socket.shutdown(socket.SHUT_WR)
        except KeyboardInterrupt:
            self.server.close()
            print('Работа завершена')

        """Обработчик запросов"""

    def load_page_from_get(self, request_data):
        self.HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
        self.HDRS404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
        self.path = request_data.split(' ')[1]
        self.response = ''
        try:
            with open('views' + self.path, 'rb') as file:
                self.response = file.read()
            return self.HDRS.encode('utf-8') + self.response
        except FileNotFoundError:
            return (self.HDRS404 + '404 ERROR PAGE').encode('utf-8')


if __name__ == '__main__':
    start_point_server = SOCKET()
