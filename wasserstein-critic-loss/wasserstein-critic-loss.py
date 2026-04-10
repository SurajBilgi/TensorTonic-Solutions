import numpy as np

def wasserstein_critic_loss(real_scores, fake_scores):
    """
    Compute Wasserstein Critic Loss for WGAN.
    """
    # Write code here
    fake_scores = np.mean(fake_scores)
    real_scores = np.mean(real_scores)

    return fake_scores - real_scores