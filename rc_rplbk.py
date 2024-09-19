class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def get_mahasiswa_details(self):
        return f"Nama: {self.nama}, NIM: {self.nim}, Jurusan: {self.jurusan}"

class NilaiCalculator:
    def __init__(self, grades):
        self.grades = grades

    def calculate_average_grade(self):
        total = sum(self.grades)
        return total / len(self.grades)

    def determine_grade_status(self):
        average = self.calculate_average_grade()
        if average >= 85:
            return "A"
        elif 70 <= average < 85:
            return "B"
        elif 55 <= average < 70:
            return "C"
        else:
            return "D"

if __name__ == "__main__":

    mahasiswa = Mahasiswa("Raihan Maulana", "21120122140136", "Teknik Komputer")
    print(mahasiswa.get_mahasiswa_details())

    grades = [90, 92, 76, 85]
    nilai_calculator = NilaiCalculator(grades)

    print(f"Rata-rata Nilai: {nilai_calculator.calculate_average_grade()}")
    print(f"Status Nilai: {nilai_calculator.determine_grade_status()}")
