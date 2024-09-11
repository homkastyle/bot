from fpdf import FPDF
import os

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Отчет по результатам оптимизации стратегии', 0, 1, 'C')

    def add_title(self, title):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, title, 0, 1, 'L')

    def add_text(self, text):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, text)

    def add_image(self, image_path, w=100):
        if os.path.exists(image_path):
            self.image(image_path, w=w)
        else:
            self.add_text(f"Изображение {image_path} не найдено.")

def create_pdf_report(metrics, charts, save_path="optimization_report.pdf"):
    pdf = PDFReport()
    pdf.add_page()

    # Добавление заголовка и метрик
    pdf.add_title('Ключевые метрики')
    metrics_text = (
        f"Общее количество сделок: {metrics['total_trades']}\n"
        f"Прибыльные сделки: {metrics['profitable_trades']}\n"
        f"Убыточные сделки: {metrics['losing_trades']}\n"
        f"Процент прибыльных сделок: {metrics['win_rate']:.2f}%\n"
        f"Средний размер сделки: {metrics['average_trade_size']:.2f} USDT\n"
        f"Максимальная прибыль: {metrics['max_profit']:.2f} USDT\n"
        f"Максимальный убыток: {metrics['max_loss']:.2f} USDT\n"
    )
    pdf.add_text(metrics_text)

    # Добавление графиков
    for chart in charts:
        pdf.add_page()
        pdf.add_image(chart)

    # Сохранение PDF
    pdf.output(save_path)
    print(f"PDF отчет сохранен в файл: {save_path}")
