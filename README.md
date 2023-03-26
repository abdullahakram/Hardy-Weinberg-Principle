# Implementation for Hardy–Weinberg principle

The Hardy-Weinberg principle is a fundamental concept in population genetics that describes the relationship between the frequencies of alleles (different forms of a gene) and genotypes (the genetic makeup of an individual) in a population that is not evolving. The principle states that if certain assumptions are met, the frequencies of alleles and genotypes in a population will remain constant from one generation to the next.

The assumptions of the Hardy-Weinberg principle are:

No mutation occurs.
No migration occurs.
The population is infinitely large.
Mating is random.
All individuals have equal reproductive success.
There is no selection for or against any particular genotype.
Under these assumptions, the frequency of alleles in a population can be calculated using the equation p + q = 1, where p is the frequency of the dominant allele and q is the frequency of the recessive allele. The frequency of genotypes can be calculated using the equation p^2 + 2pq + q^2 = 1, where p^2 is the frequency of the homozygous dominant genotype, 2pq is the frequency of the heterozygous genotype, and q^2 is the frequency of the homozygous recessive genotype.

The Hardy-Weinberg principle is useful in studying the genetic structure of populations, as it allows us to predict the frequencies of alleles and genotypes in a population based on the initial frequencies. Deviations from the Hardy-Weinberg equilibrium can indicate that one or more of the assumptions are not met, and may be the result of evolutionary processes such as mutation, migration, or natural selection.

In this implementation, we define the frequencies of the two alleles p and q, and use them to calculate the expected genotype frequencies using the Hardy-Weinberg equation. We then calculate the expected allele frequencies based on the genotype frequencies. Finally, we print the expected genotype and allele frequencies.

Note that this implementation assumes that the population is not evolving and that the other assumptions of the Hardy-Weinberg principle are met. If these assumptions are not met, the observed frequencies may deviate from the expected frequencies.
