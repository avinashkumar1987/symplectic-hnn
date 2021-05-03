# Symplectic Hamiltonian Neural Networks | 2021
# Marco David

# Originally written for the project and by:
# Hamiltonian Neural Networks | 2019
# Sam Greydanus, Misko Dzamba, Jason Yosinski

import torch

from model.standard_nn import MLP
from model.data import symplectic_form
from utils import save_path


class HNN(torch.nn.Module):
    """ Learn arbitrary Hamiltonian vector fields that are the symplectic derivative of a scalar function H """

    @staticmethod
    def create(args):
        # Create the standard MLP with args.dim inputs and one single scalar output, the Hamiltonian
        nn_model = MLP(hidden_layers=args.hidden_layers, input_dim=args.dim, hidden_dim=args.hidden_dim, output_dim=1,
                       nonlinearity=args.nonlinearity)
        # Use this model to create a Hamiltonian Neural Network, which knows how to differentiate the Hamiltonian
        model = HNN(nn_model)

        return model

    @staticmethod
    def load(args):
        saved_dict = torch.load(save_path(args))
        args = saved_dict['args']  # Loads all other arguments as saved initially when the model was trained

        # Create a model using the same args and load its state_dict
        model = HNN.create(args)
        model.load_state_dict(saved_dict['model'])

        return model, args

    def __init__(self, differentiable_model):
        super().__init__()
        self.differentiable_model = differentiable_model

        # Symplectic form J in matrix form in canonical coords
        self.J = symplectic_form(differentiable_model.input_dim)

    def forward(self, x):
        return self.differentiable_model(x)

    def time_derivative(self, x):
        """ Calculates the Hamiltonian vector field from the predicted Hamiltonian (self.forward) """
        H = self.forward(x)  # traditional forward pass, predicts Hamiltonian

        gradH = torch.autograd.grad(H.sum(), x, create_graph=True)[0]  # gradient using autograd

        # Do batch matrix-vector multiplication, since gradH contains batch_size many 2n-vectors
        # (Recall that J is antisymmetric and orthogonal: J^T = -J = J^(-1).)
        vector_field = torch.einsum('ij,aj->ai', self.J.T, gradH)
        # An alternative string for this batch operation would be 'ij,...j->...i' to not specify the extra dims.

        return vector_field


class CorrectedHNN(HNN):
    """ Use an HNN but correct the learned modified Hamiltonian to actually
        and accurately predict the real Hamiltonian. """

    def __init__(self, differentiable_model, scheme, h):
        super().__init__(differentiable_model)
        self.scheme = scheme
        self.h = h

    @staticmethod
    def get(hnn, scheme, h):
        return CorrectedHNN(hnn.differentiable_model, scheme, h)

    def forward(self, x):
        hamiltonian = super().forward(x)
        hamiltonian_corrected = self.scheme.corrected(hamiltonian, x, self.h)
        return hamiltonian_corrected
