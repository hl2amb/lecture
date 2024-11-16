class Score:
    def __init__(self, name, mid, final, avr, grade):
        self.name = name
        self.mid = mid
        self.final = final
        self.avr = avr
        self.grade = grade

        print('{0}의 중간고사 성적은 {1}, 기말고사 성적은 {2}, 평균은 {3}이고 최종 학점은 {4}입니다.'.format(self.name, self.mid, self.final, self.avr, self.grade))


st01 = Score('영희', 100, 90, 90, "A0" )
St02 = Score('철수', 80, 70, 75, "C+")
