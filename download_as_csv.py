import pandas as pd

    df = pd.DataFrame(main_list)

    MEDIA_ROOT = settings.MEDIA_ROOT
    dir_path = MEDIA_ROOT + '/cp_usages/'
    if not os.path.isdir(dir_path):
        oldmask = os.umask(000)
        os.makedirs(dir_path, exist_ok=True, mode=0o777)
        os.umask(oldmask)
    file_path = dir_path + 'cp_usage.csv'
    df.to_csv(file_path, index=False)
    with open(file_path, 'rb') as fh:
        response = HttpResponse(fh.read())
        response['Content-Type'] = 'application/csv'
        response['Content-Disposition'] = 'attachment; filename=cp_usage.csv'
    return response
