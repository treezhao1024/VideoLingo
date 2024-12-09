import whisperx
import torch
print(torch.cuda.is_available())
# 加载模型和声学模型（用于字幕时间对齐）
device="cuda"
model = whisperx.load_model("base", "cuda")
audio_file_path = "sub.wav"

# 转录音频
with open(audio_file_path, "rb") as audio_file:
    audio_data = audio_file.read()
result = model.transcribe(audio_file_path)

# 对齐文本与音频时序（如果需要）
#aligner = whisperx.align.AlignmentModel(device=device, model=model.alignment_model)
#result = aligner.align(result["segments"], audio_file_path, result["language"])

#print(result["text"])  # 打印转录的文本
print(result)  # 打印转录的文本
