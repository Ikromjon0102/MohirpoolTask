class Unversity():
    '''Unversity nomli class '''
    __all_student = []
    def __init__(self,university_name,adress):
        self.name = university_name
        self.adress = adress

    @classmethod
    def add_(cls,student):
        """ Unversitetga talaba qo'shish """
        cls.__all_student.append(student)
        # print("talaba ro'yxatga qo'shildi")

    @classmethod
    def display_all(cls):
        """ Unversitet barcha talabalari ro'yxatini ko'rish"""
        return [i.full_name for i in cls.__all_student]

    @classmethod
    def find_one(cls,id):
        """Talabalar orasidan id orqali qidiruv"""
        for i in cls.__all_student:
            if i.id == id:
                return i.student_info()
        else:
            return "Talaba topilmadi"

    @classmethod
    def remove_one(cls,id):
        """talabalar orasidan id orqali chopish"""
        for i in cls.__all_student:
            if i.id == id:
                cls.__all_student.remove(i)
                return f"Talaba {i.full_name} unversitetdan surdi"
        else:
            return "bu id raqamidagi talaba bazada mavjud emas "

class Student():
    def __init__(self,id,full_name,millati,jinsi,fakulteti,qabul_yili):
        self.id = id
        self.full_name = full_name
        self.nation = millati
        self.gender = jinsi
        self.faculty = fakulteti
        self.admission_year = qabul_yili

    def student_info(self):
        text = f"Talaba {self.full_name} {self.admission_year} yilda {self.faculty}ga qabul qilingan,\n"
        text += f"Uning ID raqami: {self.id}, {self.nation} millatiga mansub!\n"
        return text

class Undergraduate(Student):
    """Bakalavr bosqichidagi student classi"""
    def __init__(self,id,full_name,millati,jinsi,fakulteti,qabul_yili,yotoq_joyi):
        super().__init__(id,full_name,millati,jinsi,fakulteti,qabul_yili)
        self.id = id
        self.full_name = full_name
        self.nation = millati
        self.gender = jinsi
        self.faculty = fakulteti
        self.admission_year = qabul_yili
        self.residential_hall = yotoq_joyi
    def student_info(self):
        """Bakalavr bosqichidagi student haqida info beradi"""
        text = f"Talaba {self.full_name} {self.admission_year} yilda {self.faculty}ga qabul qilingan,\n"
        text += f"Uning ID raqami: {self.id}, {self.nation} millatiga mansub bo'lib,\n"
        text += f"u {self.residential_hall}dan o'qishga qatnaydi."
        return text

class Postgraduate(Student):
    """Magister bosqichidagi student classi"""
    def __init__(self,id,full_name,millati,jinsi,fakulteti,qabul_yili,supervisor_name, research_topic):
        super().__init__(id,full_name,millati,jinsi,fakulteti,qabul_yili)
        self.id = id
        self.full_name = full_name
        self.nation = millati
        self.gender = jinsi
        self.faculty = fakulteti
        self.admission_year = qabul_yili
        self.super_name = supervisor_name
        self.research_topic = research_topic
    def student_info(self):
        """Magister bosqichidagi student haqida info beradi"""
        text = f"Talaba {self.full_name} {self.admission_year} yilda {self.faculty}ga qabul qilingan,\n"
        text += f"Uning ID raqami: {self.id}, {self.nation} millatiga mansub bo'lib,\n"
        text += f"uning diplom raxbari Janob {self.super_name}\n"
        text += f"va '{self.research_topic}' mavzusida izlanish olib borayapti."
        return text
