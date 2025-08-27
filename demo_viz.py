import uuid
from mne_lsl.datasets import sample
from mne_lsl.player import PlayerLSL as Player
from mne_lsl.stream_viewer import StreamViewer

def main():
    source_id = uuid.uuid4().hex
    fname = sample.data_path() / "sample-ant-raw.fif"
    player = Player(fname, chunk_size=200, source_id=source_id)
    player.start()
    viewer = StreamViewer(stream_name=player.name)
    viewer.start()

if __name__ == "__main__":
    main()