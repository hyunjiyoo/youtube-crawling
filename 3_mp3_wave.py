import sys
from pydub import AudioSegment
from PIL import Image, ImageDraw


class Waveform(object):
   bar_count = 107 # 음원 파형을 그리는데 사용할 총 막대기 개수
   db_ceiling = 60 # 음원 파형들의 높이를 평준화(nomalize)시키는 값

   def __init__(self, filename):
      # 오디오파일의 위치를 받는다.
      self.filename = filename
      # AudioSegment 객체 생성(오디오파일 위치, 파일확장자)
      audio_file = AudioSegment.from_file(self.filename, self.filename.split('.')[-1])
      # 각 오디오 파형 막대의 높이를 계산할 때 사용될 볼륨 피크 값.(Array 데이터)
      self.peaks = self._calculate_peaks(audio_file)


    # -------------------------------------- #
    # 구간별 볼륨값 데이터를 계산하는 메서드 #
    # -------------------------------------- #
    # 각각의 파형 막대의 높이를 계산하는데 쓰이는 볼륨값 데이터를 리스트로 리턴.
    def _calculate_peaks(self, audio_file):
      # 음원 파일의 길이를 막대의 개수로 나누어서 막대하나가 나타내게 될 음원의 부분 길이 계산.
      chunk_length = len(audio_file) / self.bar_count
      # 각 부분의 소리 크기(rms)값을 리스트에 저장.
      loudness_of_chunks = [
      audio_file[i * chunk_length: (i + 1) * chunk_length].rms
      for i in range(self.bar_count)]
      # 구해진 리스트에서 가장 큰 값을 max_rms 값에 저장 후, 실수값으로 변경.
      max_rms = max(loudness_of_chunks) * 1.00
      # 각 막대의 소리크기를 최대값에 대한 비율로 맞춰주고, 평준화 시킨 후 정수로 변경.
      return [int((loudness / max_rms) * self.db_ceiling)
      for loudness in loudness_of_chunks]
    
    
    # 막대 이미지를 그리는 메서드
    def _get_bar_image(self, size, fill):
      # 전체 넓이와 전체 높이
      width, height = size
      bar = Image.new('RGBA', size, fill)
      end = Image.new('RGBA', (width, 2), fill)
      draw = ImageDraw.Draw(end)
      draw.point([(0, 0), (3, 0)], fill='#c1c1c1')
      draw.point([(0, 1), (3, 1), (1, 0), (2, 0)], fill='#555555')
      bar.paste(end, (0, 0))
      bar.paste(end.rotate(180), (0, height - 2))
      return bar
  
    # 막대 이미지들을 합치는 메서드
    def _generate_waveform_image(self):
      # 전체 넓이와 전체 높이를 가지는 비어있는 이미지 생성
      im = Image.new('RGB', (840, 128), '#f5f5f5')
      # 각 요소들을 하나씩 순회
      for index, value in enumerate(self.peaks, start=0):
      # 막대를 붙여넣기 할 X축과 Y축 위치 지정
      column = index * 8 + 2
      upper_endpoint = 64 - value
      # 막대 넓이 값과 볼륨 크기 데이터의 두배 값을 높이 값으로 전달해주어 막대 생성
      # 생성한 막대를 X, Y좌표에 붙여넣음
      im.paste(self._get_bar_image((4, value * 2), '#424242'), (column, upper_endpoint))
      return im
  

    def save(self):
      png_filename = self.filename.replace(
      self.filename.split('.')[-1], 'png')
      with open(png_filename, 'wb') as imfile:
      self._generate_waveform_image().save(imfile, 'PNG')


    for i in range(len(titles)):
      mp3_filename = str(new_filename[i])
      mp3_path = os.path.join(parent_dir, mp3_filename)
      if __name__ == '__main__':
      filename = sys.argv[1]
      waveform = Waveform(mp3_path)
      waveform.save()
