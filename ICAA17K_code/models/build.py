from .dat import DAT
import torch

def parse_option():
    import argparse
    from config import get_config
    parser = argparse.ArgumentParser()
    parser.add_argument('--cfg', type=str, metavar="FILE", help='path to config file', default='configs/dat_tiny.yaml')
    parser.add_argument(
        "--opts",
        help="Modify config options by adding 'KEY VALUE' pairs. ",
        default=None,
        nargs='+',
    )
    # easy config modification
    parser.add_argument('--data-path', type=str, help='path to dataset')
    parser.add_argument('--resume', help='resume from checkpoint', default='/home/supershuai/dat_tiny_in1k_224.pth')
    parser.add_argument('--amp', action='store_true', default=False)
    parser.add_argument('--output', default='output', type=str, metavar='PATH',
                        help='root of output folder, the full path is <output>/<model_name>/<tag> (default: output)')
    parser.add_argument('--tag', help='tag of experiment')
    parser.add_argument('--eval', action='store_true', help='Perform evaluation only')
    parser.add_argument('--pretrained', type=str, help='Finetune 384 initial checkpoint.', default='')

    args, unparsed = parser.parse_known_args()

    config = get_config(args)

    return args, config

def build_model(config):

    model_type = config.MODEL.TYPE
    if model_type == 'dat':
        model = DAT(**config.MODEL.DAT)
    else:
        raise NotImplementedError(f"Unkown model: {model_type}")

    return model

def load_and_build_model():
    args, config = parse_option()
    print(f"Creating model:{config.MODEL.TYPE}/{config.MODEL.NAME}")
    model = build_model(config)
    # print(model)

    # model_weights = model.state_dict()

    checkpoint = torch.load(config.MODEL.RESUME)
    pre_weights = checkpoint['model']
    pre_dict = {k: v for k, v in pre_weights.items() if "cls_head" not in k}
    model.load_state_dict(pre_dict, strict=False)

    # model.load_state_dict('/home/supershuai/dat_tiny_in1k_224.pth', strict=False)
    # model.cuda()
    # model = model.to(opt.device)
    return model