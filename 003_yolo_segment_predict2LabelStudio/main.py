import json
from utils.main_class import read_yaml, YoloSeg2LabelStudio


read_data=read_yaml()


if __name__ == '__main__':
    cls_yoloseg2LabStud = YoloSeg2LabelStudio( read_data["weight_model"], read_data["labelst_part_path"], )
    dict_labelme = cls_yoloseg2LabStud.get_labels(read_data["pth_imgs"])
    with open(read_data["file_label_studio"], 'w') as f:
        json.dump(dict_labelme, f)
    
    print(f"File {read_data['file_label_studio']} have saved, script finish!")