class Score:
    def __init__(self, name, mid, final):
        self.name = name
        self.mid = mid
        self.final = final
        avr = int((mid + final)*0.5)

        print('{0}의 중간 고사 점수는 {1} 기말고사 점수는 {2}, 평균은 {3}입니다'.format(self.name, self.mid, self.final, avr))


        if avr >= 90:
            print("당신의 최종 학점은 A0입니다")
        elif avr <= 89:
            print ("당신의 최종 학점은 B 입니다")
        else:
            print("당신읜 재시험 대상자입니다")



st01 = Score('김아리', 80, 70)
st02 = Score('박아름', 90, 95)