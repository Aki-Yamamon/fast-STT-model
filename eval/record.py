import argparse
from pathlib import Path

import sounddevice as sd
import soundfile as sf

SAMPLE_RATE = 16000  # Whisperが想定するレート
CHANNELS = 1         # モノラル


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--device", type=int, default=None, help="デバイス番号")
    p.add_argument("--seconds", type=float, default=10)
    p.add_argument("--out", type=Path, default=Path("eval/recordings/test.wav"))
    args = p.parse_args()

    args.out.parent.mkdir(parents=True, exist_ok=True)

    print(f"録音開始({args.seconds}秒)...")
    audio = sd.rec(
        int(args.seconds * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="float32",
        device=args.device,
    )
    sd.wait()  # 録音終了まで待つ
    sf.write(args.out, audio, SAMPLE_RATE)
    print(f"保存しました: {args.out}")


if __name__ == "__main__":
    main()