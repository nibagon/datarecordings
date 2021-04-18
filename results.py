freqX = np.linspace(0, fs / 2, int(dataLength / 2))
fft_outer_closed = np.abs(np.fft.fft(outer_closed)[0:np.int(dataLength / 2)])
fft_inner_closed = np.abs(np.fft.fft(inner_closed)[0:np.int(dataLength / 2)])
fft_closed_nn = np.abs(np.fft.fft(closed_nn)[0:np.int(dataLength / 2)])

fft_outer_opened = np.abs(np.fft.fft(outer_opened)[0:np.int(dataLength / 2)])
fft_inner_opened = np.abs(np.fft.fft(inner_opened)[0:np.int(dataLength / 2)])
fft_opened_nn = np.abs(np.fft.fft(opened_nn)[0:np.int(dataLength / 2)])
            
            # moving average:
df_inner_opened = pd.DataFrame({"x": freqX, "y": fft_inner_opened})
df_inner_closed = pd.DataFrame({"x": freqX, "y": fft_inner_closed})
df_opened_nn = pd.DataFrame({"x": freqX, "y": fft_opened_nn})
df_closed_nn = pd.DataFrame({"x": freqX, "y": fft_closed_nn})
fft_inner_opened_smooth_alpha = df_inner_opened.y.rolling(window=int(moving_average_alpha[subject])).mean()
fft_inner_closed_smooth_alpha = df_inner_closed.y.rolling(window=int(moving_average_alpha[subject])).mean()
fft_opened_nn_smooth_alpha = df_opened_nn.y.rolling(window=int(moving_average_alpha[subject])).mean()
fft_closed_nn_smooth_alpha = df_closed_nn.y.rolling(window=int(moving_average_alpha[subject])).mean()
fft_inner_opened_smooth_delta = df_inner_opened.y.rolling(window=int(moving_average_delta[subject])).mean()
fft_inner_closed_smooth_delta = df_inner_closed.y.rolling(window=int(moving_average_delta[subject])).mean()
fft_opened_nn_smooth_delta = df_opened_nn.y.rolling(window=int(moving_average_delta[subject])).mean()
fft_closed_nn_smooth_delta = df_closed_nn.y.rolling(window=int(moving_average_delta[subject])).mean()
    
            # ALPHA SNR
aS = 8
aE = 12
alphaStart = int((aS / fs) * dataLength)
alphaEnd = int((aE / fs) * dataLength)
diff_noise_alpha = alphaEnd - alphaStart
     # RAW
left_alpha_noise = fft_inner_opened_smooth_alpha[alphaStart]
right_alpha_noise = fft_inner_opened_smooth_alpha[alphaEnd]
left_alpha_total = fft_inner_closed_smooth_alpha[alphaStart]
right_alpha_total = fft_inner_closed_smooth_alpha[alphaEnd]
correct_alpha_left = left_alpha_noise / left_alpha_total
correct_alpha_right = right_alpha_noise / right_alpha_total
    
correct_alpha = 0
if correction_a[subject] == 0:
    correct_alpha = 1
else:
    if correction_a[subject] == 1:
        correct_alpha = correct_alpha_left
    else:
        if correction_a[subject] == 2:
            correct_alpha = correct_alpha_right
    
fft_inner_closed_scaled_alpha = correct_alpha * fft_inner_closed
fft_inner_closed_smooth_scaled_alpha = correct_alpha * fft_inner_closed_smooth_alpha
    
noise_alpha = np.sum(fft_inner_opened[alphaStart:alphaEnd]) / diff_noise_alpha
integral_alpha = np.sum(fft_inner_closed_scaled_alpha[alphaStart:alphaEnd]) / diff_noise_alpha
signal_alpha = integral_alpha - noise_alpha
snr_alpha = signal_alpha / noise_alpha
            #
            # NN
left_alpha_noise_nn = fft_opened_nn_smooth_alpha[alphaStart]
right_alpha_noise_nn = fft_opened_nn_smooth_alpha[alphaEnd]
left_alpha_total_nn = fft_closed_nn_smooth_alpha[alphaStart]
right_alpha_total_nn = fft_closed_nn_smooth_alpha[alphaEnd]
correct_alpha_left_nn = left_alpha_noise_nn / left_alpha_total_nn
correct_alpha_right_nn = right_alpha_noise_nn / right_alpha_total_nn
    
correct_alpha_nn = 0
if correction_a[subject] == 0:
    correct_alpha_nn = 1
else:
    if correction_a[subject] == 1:
        correct_alpha_nn = correct_alpha_left_nn
    else:
        if correction_a[subject] == 2:
            correct_alpha_nn = correct_alpha_right_nn
    
fft_closed_nn_scaled_alpha = correct_alpha_nn * fft_closed_nn
fft_closed_nn_smooth_scaled_alpha = correct_alpha_nn * fft_closed_nn_smooth_alpha
    
noise_alpha_nn = np.sum(fft_opened_nn[alphaStart:alphaEnd]) / diff_noise_alpha
integral_alpha_nn = np.sum(fft_closed_nn_scaled_alpha[alphaStart: alphaEnd]) / diff_noise_alpha
signal_alpha_nn = integral_alpha_nn - noise_alpha_nn
snr_alpha_nn = signal_alpha_nn / noise_alpha_nn
snr_alpha_ratio = snr_alpha_nn / snr_alpha