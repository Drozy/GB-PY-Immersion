import os


def rename_files(*, name_range=None, desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc"):
    if name_range is None:
        name_range = [0, 0]
    index = 1
    for file in os.listdir(folder):
        if file.endswith(source_ext):
            serial_number = ''
            for i in range(num_digits):
                if index % pow(10, num_digits - i) > 0:
                    serial_number = '0' * i + f'{index}'
                old_filename = str(os.path.splitext(file)[0])[name_range[0]:name_range[1]]
                new_filename = f'{old_filename}{desired_name}{serial_number}.{target_ext}'
                os.rename(os.path.join(folder, file), os.path.join(folder, new_filename))
                index += 1
