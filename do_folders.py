import os
from macpaint import MacPaintFile

root_folder = os.path.dirname(__file__)
in_folder = os.path.join(root_folder, 'input')
out_folder = os.path.join(root_folder, 'output')


def main(args):
    macpaint_file = MacPaintFile.from_file(args.infile)
    macpaint_file.to_png(args.outfile)

if __name__ == "__main__":
    in_filenames = [f for f in os.listdir(in_folder) if os.path.isfile(os.path.join(in_folder, f))]
    os.makedirs(out_folder, exist_ok=True)

    print(f"Found {len(in_filenames)} files")
    
    for i in range(len(in_filenames)):
        try:
            macpaint_file = MacPaintFile.from_file(os.path.join(in_folder, in_filenames[i]))
            macpaint_file.to_png(os.path.join(out_folder, f"{in_filenames[i]}.png"))
            print(f"SUCCESS - {in_filenames[i]}")
        except:
            print(f"FAILED  - {in_filenames[i]}")

    print("Done")
