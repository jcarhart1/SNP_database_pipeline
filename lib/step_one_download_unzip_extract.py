
import pandas as pd
from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO
# download and unzip (wrap in function after testing so that this file can be called with the exe)

# z = urlopen('https://api.pharmgkb.org/v1/download/file/data/clinicalAnnotations.zip')
# myzip = ZipFile(BytesIO(z.read())).extract('clinical_annotations.tsv')
# pd.read_csv(myzip)
from pandas._libs.reshape import explode

df = pd.read_csv("C:/Users/jcarhart/Desktop/clinical_annotations.tsv", sep='\t')
print(df)
# extract to local (db next iteration)


# Select the ones you want
df_abridged = df[['Gene', 'Variant/Haplotypes', 'Level of Evidence', 'Phenotype Category', 'Drug(s)']]
# print(df_abridged)

df_abridged = df_abridged.rename(columns={'Variant/Haplotypes': 'Variant'}, inplace=False)

df_filtered_on_gene = (df_abridged.loc[df_abridged['Gene'].isin(['CYP2D6', 'CYP2C19', 'HTR2A', 'SLC6A4'])])
# print(df_filtered_on_gene)
# note: htr2a and slc6a4 were not in the clinical annotations input file

df_filtered_on_loe = (df_filtered_on_gene.loc[df_filtered_on_gene['Level of Evidence'].isin(['1A', '1B', '2A', '2B'])])
# print(df_filtered_on_loe)

df_filtered_on_med = (df_filtered_on_loe.loc[df_filtered_on_loe['Drug(s)'].isin(['amitriptyline', 'amoxapine', 'brexanolone',
                                                                                 'bupropion', 'citalopram', 'desipramine',
                                                                                 'desvenlafaxine', 'doxepin', 'duloxetine',
                                                                                 'escitalopram', 'esketamine', 'fluoxetine',
                                                                                 'imipramine', 'isocarboxazid', 'levomilnacipran',
                                                                                 'maprotiline', 'mirtazapine', 'nefazodone',
                                                                                 'nortriptyline', 'paroxetine', 'phenelzine',
                                                                                 'protriptyline', 'quetiapine', 'selegiline',
                                                                                 'sertraline', 'tranylcypromine', 'trazodone',
                                                                                 'trimipramine', 'trimipramine', 'venlafaxine',
                                                                                 'vilazodone', 'vortioxetine'])])
# print(df_filtered_on_med)

# split Variant on ';' to create new row for each variant
test_df = df_filtered_on_med.assign(Variant=df_filtered_on_med.Variant.str.split(",")).explode('Variant')
# print(test_df)

# remove (i.e., concat the new string) to remove everything before the '*'
# df_filtered_on_med.Variants = df_filtered_on_med.Variant.split('.')[1].lstrip().split(' ')[0]
# print(df_filtered_on_med)

# pivot from long to wide on medication names

# df_filtered_on_med.to_csv('C:/Users/jcarhart/Desktop/pharm_gkb_filtered.csv', index=False)
# test_df.to_csv('C:/Users/jcarhart/Desktop/pharm_gkb_filtered_split.csv', index=False)
