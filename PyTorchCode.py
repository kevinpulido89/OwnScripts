import torch

## Tensor Basics https://www.youtube.com/watch?v=exaWOE8jvy8
# # x = torch.empty(2,5, 3, 4) # or .ones(1,1)
# x = torch.rand(3,4, dtype=torch.float32)
#
# print(x)
# print(x.dtype) # x.size()
# x.div_(2)
# print(x)
# print()
# print(x[1,1:2].item())
#
# y = x.view(-1,6)
# print(y)
#
# a = np.ones(5)
# b = torch.from_numpy(a)
# print(b)
#
# z = x.numpy()
# print(z)
#
#
# if torch.cuda.is_available():
#     device = torch.device("cuda")
#
#     q = torch.ones(5, device=device)
#     w = torch.ones(5)
#     w = w.to(device)
#     r = q+w
#     r = r.to("cpu")
#
# print(r)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Gradient Calculation With Autograd https://www.youtube.com/watch?v=DbeIqrwb_dE



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
