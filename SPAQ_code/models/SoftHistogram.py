import torch
import torch.nn as nn
import torch.nn.functional as F
class SoftHistogram(nn.Module):

    def __init__(self, n_features, n_examples, num_bins, quantiles=False):
        super(SoftHistogram, self).__init__()
        self.in_channels = n_features
        self.n_examples = n_examples
        self.num_bins = num_bins
        self.quantiles = quantiles

        self.bin_centers_conv = nn.Conv1d(self.in_channels, self.num_bins * self.in_channels, kernel_size=1,
                                          groups=self.in_channels, bias=True)

        self.bin_centers_conv.weight.data.fill_(1)
        self.bin_centers_conv.weight.requires_grad = False

        self.bin_widths_conv = nn.Conv1d(self.num_bins * self.in_channels, self.num_bins * self.in_channels,
                                         kernel_size=1, groups=self.num_bins * self.in_channels, bias=True)

        self.bin_widths_conv.bias.data.fill_(1)
        self.bin_widths_conv.bias.requires_grad = False

        self.centers = self.bin_centers_conv.bias
        self.widths = self.bin_widths_conv.weight

        bin_centers = -1 / self.num_bins * (torch.arange(self.num_bins).float() + 0.5)
        self.bin_centers_conv.bias = torch.nn.Parameter(torch.cat(self.in_channels * [bin_centers]), requires_grad=True)
        bin_width = -self.num_bins * 2
        self.bin_widths_conv.weight.data.fill_(bin_width)

    def forward(self, input):
        input = self.bin_centers_conv(input.transpose(0, 1).unsqueeze(0))
        input = torch.abs(input)
        input = self.bin_widths_conv(input)

        input = F.relu(input)
        if self.quantiles:
            input = input.view(-1, self.num_bins).cumsum(dim=1)
        return input

    def constrain_bins(self, xx):
        n, c, l = xx.size()
        xx_sum = xx.reshape(n, c // self.numBins, self.numBins, l).sum(2) + torch.tensor(10e-6)
        xx_sum = torch.repeat_interleave(xx_sum, self.numBins, dim=1)
        xx = xx / xx_sum
        return xx
