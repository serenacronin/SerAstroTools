"""
Function that will create a two-Gaussian model from input parameters
Input: x-axis array and input parameters (i.e., the initial guesses of data you may be trying to fit) 
for both Gaussians (amplitudes, centroids, and sigmas)
Output: two-Gaussian model
"""
function two_gaussian(x_array, amp1,cen1,sigma1, amp2,cen2,sigma2)
    gaussian1 = amp1 .* (exp.((-1.0/2.0) .* (((x_array .- cen1) ./ sigma1).^2.0)));
    gaussian2 = amp2 .* (exp.((-1.0/2.0) .* (((x_array .- cen2) ./ sigma2).^2.0)));

    gaussian1 .+ gaussian2;
end

"""
Function that will create a Gaussian model from input parameters
Input: x-axis array and input parameters (i.e., the initial guesses of data you may be trying to fit) 
for both Gaussians (amplitude, centroid, and sigma)
Output: Gaussian model
"""
function one_gaussian(x_array, amp,cen,sigma)
    amp .* (exp.((-1.0/2.0) .* (((x_array .- cen) ./ sigma).^2.0)));
end

"""
Function that will calculate the reduced chi square between your data and model.
Input: observed (data), calculated (model), number of parameters, and any errors
Output: reduced chi square, ideally ~1
"""
function red_chisq(obs,calc,num_params,err)
    (sum(obs .- calc).^2 ./ err) ./ (length(obs) ./ num_params);
end