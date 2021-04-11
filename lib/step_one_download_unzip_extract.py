
import pandas as pd
from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO
# download and unzip (wrap in function after testing so that this file can be called with the exe)

# z = urlopen('https://api.pharmgkb.org/v1/download/file/data/clinicalAnnotations.zip')
# myzip = ZipFile(BytesIO(z.read())).extract('clinical_annotations.tsv')
# pd.read_csv(myzip)

df = pd.read_csv("C:/Users/jcarhart/Desktop/clinical_annotations.tsv", sep='\t')
print(df)
# extract to local (db next iteration)


# Select the ones you want
df_abridged = df[['Gene', 'Variant/Haplotypes', 'Level of Evidence', 'Phenotype Category', 'Drug(s)']]
# print(df_abridged)

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
print(df_filtered_on_med)

# split Variant/Haplotypes on ';' to create new row for each variant
# remove (i.e., concat the new string) to remove everything before the '*'

df_filtered_on_med.to_csv('C:/Users/jcarhart/Desktop/pharm_gkb_filtered.csv', index=False)
