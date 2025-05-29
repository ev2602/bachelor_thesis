# Detecting Gene Variants in a Population Using Machine Learning

Discovering and knowing alleles is key to understanding the hereditary traits of organism, also in the field of medical genetics, agriculture and cattle breeding. In our work we have implemented an algorithm that will find all the different allele variants in the sample of genetic material. We did discovering of gene variants by grouping, using hierarchical grouping algorithm and the goal of the research is to identify different variants of genes. The gene samples were obtained by sequencing, and the clustering algorithm was based on grouping similar sequences and analyzing a large number of samples. Detailed data preparation and sequence alignment was needed to ensure quality analysis. We adjusted different parameters, such as the cost to open and widen the gap, when creating multiple sequence alignment, in order to achieve the best possible result quality by grouping. Hierarchical grouping algorithm (Aglomerative clustering) was used for grouping gene variants. We successfully detected genes that are more represented and we presented the problem of detecting less represented genes and rejecting invalid data.

running_mafft.py - Multiple sequence alignemnet of all sequences

best_cluster.py - calculating distance matrix

zavrsni_rad.ipynb - jupyter notebook 

