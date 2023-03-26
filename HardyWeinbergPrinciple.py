import numpy as np

# Define the frequencies of the two alleles
p = 0.6    # frequency of dominant allele
q = 0.4    # frequency of recessive allele

# Calculate the expected genotype frequencies
p_squared = p ** 2                    # frequency of homozygous dominant genotype
q_squared = q ** 2                    # frequency of homozygous recessive genotype
two_pq = 2 * p * q                    # frequency of heterozygous genotype

# Calculate the expected allele frequencies
expected_p = p_squared + (0.5 * two_pq)  # the frequency of dominant allele in the next generation
expected_q = q_squared + (0.5 * two_pq)  # the frequency of recessive allele in the next generation

# Print the expected genotype and allele frequencies
print("Expected genotype frequencies:")
print("Homozygous dominant: ", p_squared)
print("Heterozygous: ", two_pq)
print("Homozygous recessive: ", q_squared)
print("Expected allele frequencies:")
print("Dominant allele frequency: ", expected_p)
print("Recessive allele frequency: ", expected_q)
