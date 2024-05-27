
############################ Create final sample ############################
# Extract sub-samples from each continent sample and merge into final sub-sample

# %%
# Import libraries
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit

# %%
# Load data
africa = pd.read_csv('Africa_Clean.csv')
asia = pd.read_csv('Asia_Clean.csv')
europe = pd.read_csv('Europe_Clean.csv')
north_america = pd.read_csv('NorthAmerica_Clean.csv')
south_america = pd.read_csv('SouthAmerica_Clean.csv')
oceania = pd.read_csv('Oceania_Clean.csv')


# %%
# Define create_sub_sample function
def create_sub_sample(dataframe, proportion):
    """
    Create a sub-sample (50% of the original sample) from the given DataFrame using stratified sampling.

    Arguments:
    dataframe: The input DataFrame (a sample for each of the 6 continents)

    Returns:
    pd.DataFrame: A sub-sample of the input DataFrame, maintaining the class distribution based on 'UserCountry3'
    and ensuring both sides of each scenario (ResponseID) are included
    """

    # Print original sample info - verify number of rows
    print(dataframe.info())

    # Group the data by 'ResponseID'
    grouped = dataframe.groupby('ResponseID')

    # Create a list of indices and their corresponding 'UserCountry3' values
    indices_list = []
    country_labels = []

    for response_id, group in grouped:
        # response_id: current ResponseID
        # group: group DataFrame containing rows with the current ResponseID
        indices = group.index.tolist()
        # indices: indices of those two rows as a list
        user_country = group['UserCountry3'].iloc[0]
        # user_country: takes country of first row of the group (the same for both rows)
        indices_list.append(indices)
        # append the current list of indices to indices_list
        # indices_list is a list of lists
        country_labels.append(user_country)
        # append the country of the current group to the list country_labels

    # Create an instance of StratifiedShuffleSplit
    stratified_sampler = StratifiedShuffleSplit(n_splits=1, test_size=proportion, random_state=42)

    # Perform stratified sampling to extract a sub-sample
    sub_sample_indices = []

    # Iterate over train and test indices produced by stratified_sampler, based on indices_list and country_labels
    for train_indices, test_indices in stratified_sampler.split(indices_list, country_labels):
        # Iterate over test indices
        for idx in test_indices:
            # idx: index of specific inner list in indices_list
            sub_sample_indices.extend([index for index in indices_list[idx] if index in dataframe.index])
            # index for index in indices_list[idx]: iterate over each index (a row in the DataFrame) in the inner lists 'indices_list' at position idx
            # idx: integer index of specific inner list within indices_list
            # if index in dataframe.index: filter indices that are present in dataframe.index
            # .extend: append the list of indices to sub_sample_indices

    # Create the sub-sample by indexing the original DataFrame
    sub_sample = dataframe.loc[sub_sample_indices]

    return sub_sample


proportion = 0.5

# %%
# Define verify_proportions function
def verify_proportions(df, columns):
    """
    Verify the proportions and counts of specific columns in the provided dataframe

    Arguments:
    df: The input DataFrame containing the columns to be verified
    columns: A list of column names to be verified

    Returns:
    None: The function prints the counts and proportions of each specified column in the DataFrame.
    """

    for column in columns:
        # Calculate the counts and proportions for each value in the column
        counts = df[column].value_counts()
        proportions = df[column].value_counts(normalize=True)

        # Combine counts and proportions
        combined = pd.DataFrame({
            'Count': counts,
            'Proportion': proportions})

        # Display the results
        print(f"Column: '{column}'")
        print(combined)
        print()


# Columns to verify
columns_to_verify = ['Saved', 'UserCountry3', 'Cultures']

# %%
######################## Africa ########################
# Apply create_sub_sample function
africa_sub = create_sub_sample(africa, proportion)
# From 311.892 entries to 155.946 entries

# Display the sub-sample
print(africa_sub.info())
print()
print(africa_sub.head())

# %%
# Verify proportions in the entire continent sample
print("Proportions and counts in the entire continent sample:")
verify_proportions(africa, columns_to_verify)

# Verify proportions in the sub-sample
print("Proportions and counts in the sub-sample:")
verify_proportions(africa_sub, columns_to_verify)

"""
Proportions and counts in the entire continent sample:
Column: 'Saved'
    Count  Proportion
1  155946         0.5
0  155946         0.5

Column: 'UserCountry3'
      Count  Proportion
ZAF  129424    0.414964
MAR   49870    0.159895
EGY   45754    0.146698
DZA   30718    0.098489
TUN   23650    0.075828
REU   15746    0.050485
KEN    8428    0.027022
MUS    8302    0.026618

Column: 'Cultures'
            Count  Proportion
Islamic    287844    0.922896
Catholic    15746    0.050485
SouthAsia    8302    0.026618

Proportions and counts in the sub-sample:
Column: 'Saved'
   Count  Proportion
0  77973         0.5
1  77973         0.5

Column: 'UserCountry3'
     Count  Proportion
ZAF  64712    0.414964
MAR  24934    0.159889
EGY  22878    0.146705
DZA  15358    0.098483
TUN  11824    0.075821
REU   7874    0.050492
KEN   4214    0.027022
MUS   4152    0.026625

Column: 'Cultures'
            Count  Proportion
Islamic    143920    0.922884
Catholic     7874    0.050492
SouthAsia    4152    0.026625
"""

# %%
######################## Asia ########################
# Apply create_sub_sample function
asia_sub = create_sub_sample(asia, proportion)
# From 6.447.088 entries to 3.223.544 entries

# Display the sub-sample
print(asia_sub.info())
print()
print(asia_sub.head())

# %%
# Verify proportions in the entire continent sample
print("Proportions and counts in the entire continent sample:")
verify_proportions(asia, columns_to_verify)

# Verify proportions in the sub-sample
print("Proportions and counts in the sub-sample:")
verify_proportions(asia_sub, columns_to_verify)

"""
Proportions and counts in the entire continent sample:
Column: 'Saved'
     Count  Proportion
0  3223544         0.5
1  3223544         0.5

Column: 'UserCountry3'
       Count  Proportion
TUR  1747060    0.270984
JPN  1480808    0.229686
SGP   503692    0.078127
TWN   321624    0.049887
KOR   293780    0.045568
IND   284362    0.044107
HKG   248426    0.038533
PHL   227956    0.035358
THA   186246    0.028888
IDN   181952    0.028222
CHN   154316    0.023936
MYS   148466    0.023028
VNM   106064    0.016451
SAU   100328    0.015562
ARE    91482    0.014190
KAZ    49874    0.007736
AZE    38266    0.005935
PAK    33624    0.005215
JOR    33324    0.005169
IRN    25274    0.003920
GEO    23594    0.003660
CYP    22302    0.003459
LBN    20332    0.003154
QAT    19944    0.003093
KWT    17342    0.002690
BGD    15458    0.002398
PSE    11396    0.001768
ARM    11362    0.001762
IRQ    11008    0.001707
LKA    10804    0.001676
KHM     8374    0.001299
MNG     6814    0.001057
MAC     5864    0.000910
NPL     5570    0.000864

Column: 'Cultures'
                Count  Proportion
Islamic       2545130    0.394772
Confucian     2511632    0.389576
SouthAsia     1105112    0.171413
LatinAmerica   227956    0.035358
Orthodox        57258    0.008881

Proportions and counts in the sub-sample:
Column: 'Saved'
     Count  Proportion
0  1611772         0.5
1  1611772         0.5

Column: 'UserCountry3'
      Count  Proportion
TUR  873530    0.270984
JPN  740404    0.229686
SGP  251846    0.078127
TWN  160812    0.049887
KOR  146890    0.045568
IND  142182    0.044107
HKG  124214    0.038533
PHL  113978    0.035358
THA   93124    0.028889
IDN   90976    0.028222
CHN   77158    0.023936
MYS   74232    0.023028
VNM   53032    0.016451
SAU   50164    0.015562
ARE   45740    0.014189
KAZ   24936    0.007736
AZE   19132    0.005935
PAK   16812    0.005215
JOR   16662    0.005169
IRN   12638    0.003921
GEO   11796    0.003659
CYP   11152    0.003460
LBN   10166    0.003154
QAT    9972    0.003093
KWT    8672    0.002690
BGD    7730    0.002398
PSE    5698    0.001768
ARM    5680    0.001762
IRQ    5504    0.001707
LKA    5402    0.001676
KHM    4186    0.001299
MNG    3408    0.001057
MAC    2932    0.000910
NPL    2784    0.000864

Column: 'Cultures'
                Count  Proportion
Islamic       1272564    0.394772
Confucian     1255818    0.389577
SouthAsia      552556    0.171413
LatinAmerica   113978    0.035358
Orthodox        28628    0.008881
"""

# %%
######################## Europe ########################
# Apply create_sub_sample function
europe_sub = create_sub_sample(europe, proportion)
# From 31.794.814 entries to 15.897.408 entries

# Display the sub-sample
print(europe_sub.info())
print()
print(europe_sub.head())

# %%
# Verify proportions in the entire continent sample
print("Proportions and counts in the entire continent sample:")
verify_proportions(europe, columns_to_verify)

# Verify proportions in the sub-sample
print("Proportions and counts in the sub-sample:")
verify_proportions(europe_sub, columns_to_verify)

"""
Proportions and counts in the entire continent sample:
Column: 'Saved'
      Count  Proportion
1  15897407         0.5
0  15897407         0.5

Column: 'UserCountry3'
       Count  Proportion
DEU  4440290    0.139655
FRA  3822946    0.120238
GBR  3588516    0.112865
RUS  2400228    0.075491
ESP  1680388    0.052851
POL  1654370    0.052033
ITA  1646878    0.051797
CZE  1422984    0.044755
BEL  1347572    0.042383
HUN  1236058    0.038876
NLD  1018216    0.032025
SWE   975528    0.030682
FIN   811468    0.025522
AUT   602588    0.018952
CHE   578686    0.018201
UKR   556240    0.017495
DNK   511616    0.016091
PRT   473966    0.014907
ROU   413722    0.013012
SVK   396024    0.012456
NOR   394098    0.012395
LTU   337660    0.010620
IRL   259504    0.008162
GRC   234168    0.007365
BGR   151890    0.004777
HRV   125380    0.003943
BLR   118134    0.003716
EST   106740    0.003357
SRB    96272    0.003028
LVA    87570    0.002754
SVN    67224    0.002114
MKD    58534    0.001841
LUX    49404    0.001554
BIH    37104    0.001167
ISL    31716    0.000998
MDA    20936    0.000658
MLT    19254    0.000606
ALB    13448    0.000423
MNE     7494    0.000236

Column: 'Cultures'
               Count  Proportion
Catholic    14545036    0.457466
Protestant   8761618    0.275568
Orthodox     4108170    0.129209
English      3848020    0.121027
Baltic        531970    0.016731

Proportions and counts in the sub-sample:
Column: 'Saved'
     Count  Proportion
1  7948704         0.5
0  7948704         0.5

Column: 'UserCountry3'
       Count  Proportion
DEU  2220146    0.139655
FRA  1911474    0.120238
GBR  1794258    0.112865
RUS  1200114    0.075491
ESP   840194    0.052851
POL   827186    0.052033
ITA   823440    0.051797
CZE   711492    0.044755
BEL   673786    0.042383
HUN   618030    0.038876
NLD   509108    0.032025
SWE   487764    0.030682
FIN   405734    0.025522
AUT   301294    0.018952
CHE   289344    0.018201
UKR   278120    0.017495
DNK   255808    0.016091
PRT   236984    0.014907
ROU   206862    0.013012
SVK   198012    0.012456
NOR   197048    0.012395
LTU   168830    0.010620
IRL   129752    0.008162
GRC   117084    0.007365
BGR    75944    0.004777
HRV    62690    0.003943
BLR    59066    0.003715
EST    53370    0.003357
SRB    48136    0.003028
LVA    43784    0.002754
SVN    33612    0.002114
MKD    29266    0.001841
LUX    24702    0.001554
BIH    18552    0.001167
ISL    15858    0.000998
MDA    10468    0.000658
MLT     9626    0.000606
ALB     6724    0.000423
MNE     3746    0.000236

Column: 'Cultures'
              Count  Proportion
Catholic    7272522    0.457466
Protestant  4380810    0.275568
Orthodox    2054082    0.129209
English     1924010    0.121027
Baltic       265984    0.016731
"""

# %%
######################## North America ########################
# Apply create_sub_sample function
north_america_sub = create_sub_sample(north_america, proportion)
# From 20.730.470 entries to 10.365.236 entries

# Display the sub-sample
print(north_america_sub.info())
print()
print(north_america_sub.head())

# %%
# Verify proportions in the entire continent sample
print("Proportions and counts in the entire continent sample:")
verify_proportions(north_america, columns_to_verify)

# Verify proportions in the sub-sample
print("Proportions and counts in the sub-sample:")
verify_proportions(north_america_sub, columns_to_verify)

"""
Proportions and counts in the entire continent sample:
Column: 'Saved'
      Count  Proportion
1  10365235         0.5
0  10365235         0.5

Column: 'UserCountry3'
        Count  Proportion
USA  17230746    0.831180
CAN   2679992    0.129278
MEX    629000    0.030342
CRI     62000    0.002991
GTM     24536    0.001184
DOM     24056    0.001160
PRI     23560    0.001136
PAN     16098    0.000777
SLV     12734    0.000614
TTO     10728    0.000517
HND     10360    0.000500
JAM      6660    0.000321

Column: 'Cultures'
                 Count  Proportion
English       19910738    0.960458
LatinAmerica    819732    0.039542

Proportions and counts in the sub-sample:
Column: 'Saved'
     Count  Proportion
0  5182618         0.5
1  5182618         0.5

Column: 'UserCountry3'
       Count  Proportion
USA  8615374    0.831180
CAN  1339996    0.129278
MEX   314500    0.030342
CRI    31000    0.002991
GTM    12268    0.001184
DOM    12028    0.001160
PRI    11780    0.001136
PAN     8050    0.000777
SLV     6366    0.000614
TTO     5364    0.000517
HND     5180    0.000500
JAM     3330    0.000321

Column: 'Cultures'
                Count  Proportion
English       9955370    0.960458
LatinAmerica   409866    0.039542
"""

# %%
######################## South America ########################
# Apply create_sub_sample function
south_america_sub = create_sub_sample(south_america, proportion)
# From 5.144.964 entries to 2.572.482 entries

# Display the sub-sample
print(south_america_sub.info())
print()
print(south_america_sub.head())

# %%
# Verify proportions in the entire continent sample
print("Proportions and counts in the entire continent sample:")
verify_proportions(south_america, columns_to_verify)

# Verify proportions in the sub-sample
print("Proportions and counts in the sub-sample:")
verify_proportions(south_america_sub, columns_to_verify)

"""
Proportions and counts in the entire continent sample:
Column: 'Saved'
     Count  Proportion
0  2572482         0.5
1  2572482         0.5

Column: 'UserCountry3'
       Count  Proportion
BRA  3861234    0.750488
ARG   458238    0.089065
COL   253482    0.049268
CHL   253440    0.049260
PER    88108    0.017125
VEN    87694    0.017045
URY    67962    0.013209
ECU    45808    0.008903
PRY    15830    0.003077
BOL    13168    0.002559

Column: 'Cultures'
                Count  Proportion
LatinAmerica  5144964         1.0

Proportions and counts in the sub-sample:
Column: 'Saved'
     Count  Proportion
0  1286241         0.5
1  1286241         0.5

Column: 'UserCountry3'
       Count  Proportion
BRA  1930618    0.750488
ARG   229120    0.089066
COL   126740    0.049268
CHL   126720    0.049260
PER    44054    0.017125
VEN    43846    0.017044
URY    33982    0.013210
ECU    22904    0.008903
PRY     7914    0.003076
BOL     6584    0.002559

Column: 'Cultures'
                Count  Proportion
LatinAmerica  2572482         1.0
"""

# %%
######################## Oceania ########################
# Apply create_sub_sample function
oceania_sub = create_sub_sample(oceania, proportion)
# From 2.190.686 entries to 1.095.344 entries

# Display the sub-sample
print(oceania_sub.info())
print()
print(oceania_sub.head())

# %%
# Verify proportions in the entire continent sample
print("Proportions and counts in the entire continent sample:")
verify_proportions(oceania, columns_to_verify)

# Verify proportions in the sub-sample
print("Proportions and counts in the sub-sample:")
verify_proportions(oceania_sub, columns_to_verify)

"""
Proportions and counts in the entire continent sample:
Column: 'Saved'
     Count  Proportion
1  1095343         0.5
0  1095343         0.5

Column: 'UserCountry3'
       Count  Proportion
AUS  1800224    0.821763
NZL   385078    0.175780
NCL     5384    0.002458

Column: 'Cultures'
            Count  Proportion
English   2185302    0.997542
Catholic     5384    0.002458

Proportions and counts in the sub-sample:
Column: 'Saved'
    Count  Proportion
1  547672         0.5
0  547672         0.5

Column: 'UserCountry3'
      Count  Proportion
AUS  900112    0.821762
NZL  192540    0.175780
NCL    2692    0.002458

Column: 'Cultures'
            Count  Proportion
English   1092652    0.997542
Catholic     2692    0.002458
"""

# %%
# Merge six continent sub-samples into a final sub-sample
merged_df = pd.concat([africa_sub, asia_sub, europe_sub, north_america_sub, south_america_sub, oceania_sub], axis=0)

# Reset index
merged_df = merged_df.reset_index(drop=True)

# %%
# Visualize info
print(merged_df.info())
# RangeIndex: 33.309.960 entries <-- Number of rows in the final sample
# [that is: 16.654980 scenarios]
print()
print(merged_df.head())

# %%
# Verify proportions on final sub-sample
print("Proportions and counts in the final merged sub-sample:")
verify_proportions(merged_df, columns_to_verify)

"""
Proportions and counts in the final merged sub-sample:
Column: 'Saved'
      Count  Proportion
0  16654980         0.5
1  16654980         0.5

Column: 'UserCountry3'
       Count  Proportion
USA  8615374    0.258643
DEU  2220146    0.066651
BRA  1930618    0.057959
FRA  1911474    0.057384
GBR  1794258    0.053866
..       ...         ...
MNG     3408    0.000102
JAM     3330    0.000100
MAC     2932    0.000088
NPL     2784    0.000084
NCL     2692    0.000081

[106 rows x 2 columns]

Column: 'Cultures'
                 Count  Proportion
English       12972032    0.389434
Catholic       7283088    0.218646
Protestant     4380810    0.131517
LatinAmerica   3096326    0.092955
Orthodox       2082710    0.062525
Islamic        1416484    0.042524
Confucian      1255818    0.037701
SouthAsia       556708    0.016713
Baltic          265984    0.007985
"""

# %%
# Export the merged_df
merged_df.to_csv('Merged_Samples.csv', index=False)
