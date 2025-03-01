from huggingface_hub import HfApi, snapshot_download


api = HfApi()
# api.upload_large_folder(
#     folder_path="/mnt/dongxu-fs1/data-hdd/geyuan/datasets/huggingface/v1",
#     repo_id="ygtxr1997/oxe_octo",
#     repo_type="dataset"
# )

api.upload_folder(
    folder_path="/mnt/dongxu-fs1/data-hdd/geyuan/datasets/huggingface/v1/bridge_dataset",
    repo_id="ygtxr1997/oxe_octo",
    path_in_repo="bridge_dataset",
    # allow_patterns="*.txt", # Upload all local text files
    # delete_patterns="*.txt", # Delete all remote text files before
)

snapshot_download(
    repo_id="ygtxr1997/oxe_octo",
    etag_timeout=100,
    local_dir=".",
    repo_type="dataset",
)