from glob import glob
import os

def get_image_list(data_root, split):
    filelist = []
    with open('filelists/{}.txt'.format(split)) as f:
        for line in f:
            line = line.strip()
            if ' ' in line: line = line.split()[0]
            filelist.append(os.path.join(data_root, line))
    return filelist

class HParams:
    # Audio processing
    sample_rate = 16000
    preemphasis = 0.97
    n_fft = 800
    hop_length = 200
    hop_size = 200  # Alias for hop_length
    win_length = 800
    win_size = 800  # Alias for win_length
    num_mels = 80
    mel_fmin = 0.0
    mel_fmax = 8000.0
    fmin = 55
    fmax = 7600
    ref_level_db = 20
    min_level_db = -100
    frame_shift_ms = None
    griffin_lim_iters = 60
    power = 1.5
    signal_normalization = True
    allow_clipping_in_normalization = True
    symmetric_mels = True
    max_abs_value = 4.0
    preemphasize = True
    use_lws = False

    # Spectrogram scaling
    rescale = True
    rescaling_max = 0.9

    # Model and training
    img_size = 96
    fps = 25
    batch_size = 16
    initial_learning_rate = 1e-4
    nepochs = 200000000000000000
    num_workers = 16
    checkpoint_interval = 3000
    eval_interval = 3000
    save_optimizer_state = True
    syncnet_wt = 0.0  # Will be set to 0.03 later
    syncnet_batch_size = 64
    syncnet_lr = 1e-4
    syncnet_eval_interval = 10000
    syncnet_checkpoint_interval = 10000
    disc_wt = 0.07
    disc_initial_learning_rate = 1e-4

    def __getattr__(self, key):
        raise AttributeError(f"'HParams' object has no attribute {key}")

hp = HParams()

def hparams_debug_string():
    values = vars(hp)
    hp_list = ["  %s: %s" % (name, values[name]) for name in sorted(values)]
    return "Hyperparameters:\n" + "\n".join(hp_list)