import argparse
import time
from pathlib import Path

from faster_whisper import WhisperModel


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("wav", type=Path)
    p.add_argument("--model", default="small", help="tiny / base / small / medium")
    p.add_argument("--language", default="ja")
    args = p.parse_args()

    t0 = time.perf_counter()
    model = WhisperModel(args.model, device="cpu", compute_type="int8")
    t_load = time.perf_counter() - t0

    t1 = time.perf_counter()
    segments, info = model.transcribe(str(args.wav), language=args.language)
    text = "".join(seg.text for seg in segments)  # ここで実際に処理が走る
    t_infer = time.perf_counter() - t1

    print(f"認識結果: {text}")
    print(f"モデル読込: {t_load:.2f}s / 推論: {t_infer:.2f}s")


if __name__ == "__main__":
    main()