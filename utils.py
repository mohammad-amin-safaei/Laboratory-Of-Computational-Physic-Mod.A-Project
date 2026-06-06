import os
import glob
import numpy as np
import wfdb

def load_rr_intervals(data_dir):
    """
    Load all NSR records and return a dict:
        { 'nsr001': rr_array_in_seconds, ... }

    Uses wfdb to read the .hea/.ecg files properly,
    then extracts RR intervals from the annotations.
    """
    records = sorted(glob.glob(os.path.join(data_dir, "nsr*.hea")))
    records = [os.path.splitext(r)[0] for r in records]  # strip .hea

    rr_data = {}

    for record_path in records:
        record_name = os.path.basename(record_path)
        try:
            # Read annotation (R-peak locations in samples)
            ann = wfdb.rdann(record_path, extension="ecg")
            r_peaks = ann.sample                        # sample indices
            fs = wfdb.rdheader(record_path).fs          # sampling frequency

            rr = np.diff(r_peaks) / fs                  # convert to seconds
            rr = rr[(rr > 0.3) & (rr < 2.0)]           

            rr_data[record_name] = rr
            print(f"  {record_name}: {len(rr)} beats, "
                  f"mean HR = {60 / np.mean(rr):.1f} bpm")

        except Exception as e:
            print(f"  {record_name}: FAILED — {e}")

    print(f"\nLoaded {len(rr_data)} records, "
          f"{sum(len(v) for v in rr_data.values()):,} total beats")
    return rr_data


if __name__ == "__main__":
    data_dir = "physionet.org/files/nsr2db/1.0.0"
    rr_data = load_rr_intervals(data_dir)