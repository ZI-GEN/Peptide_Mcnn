#Get attribute
python get_Feature.py (1 or 2 or 3) -in (fasta files path) -out (output files path)

1 is pssm
2 is binary
3 is prottrans

#Data pre-processing

Obtain biological information near all amino acids

python batch_get_series_feature.py -in (pssm folder or prottrans folder or binary folder path) -out(output folder path)  -script ./get_series_feature.py -num 10 -old_ext ".binary or .mmseq2 or .prottrans" -new_ext ".set" -w 5

#run model
python MCNN_Pep.py -D_tr (Train_Data folder path) -L_tr (Train_Label folder path ) -D_ts (Test_Data folder path) -L_ts (Test_Label folder path ) -n_feat (Dimensions)

-n_dep  #the number of dependent variables
-n_fil  #the number of filters in the convolutional layer
-n_hid  #the number of hidden units in the dense layer
-bs     #the batch size
-ws     #the window sizes for convolutional filters
-n_feat #the number of features
-e	#the number of epochs for training
-val    #the mod for validation 'cross' or 'independent'
-k_fold #the number of k for k_fold cross validation
