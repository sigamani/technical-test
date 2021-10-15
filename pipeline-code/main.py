from argparse import ArgumentParser
import pandas as pd
from datetime import date

from modules.response_processing import load_data, clean_data, add_weights, save_to_output
from modules.clustering import kmodes_clustering, process, rules_segmentation
from modules.salient_questions import SalientQuestions


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:

    # Clean data
    response_data = clean_data.main(df=df)
    # Add weights
    response_data = add_weights.main(data=response_data,
                                     gender_col="DEM_WW_GENDER_RB_L_v3_14072020",
                                     age_col="DEM_WW_AGE_DM_L_v1_14072020",
                                     region_col="REGION")

    # Save data
    save_to_output.processed_responses(data=response_data,
                                       file_name=f'processed_responses_{date_str}.csv')
    return response_data


def segmentation(df: pd.DataFrame, segmentation_type='kmodes', **kwargs) -> pd.DataFrame:
    """If segmentation_type = 'rules' additional argument required,
    *segmentation_cols:  str type, column to segment on e.g. 'DEM_WW_GENDER_RB_L_v3_14072020'
    """
    segmented_data = pd.DataFrame()
    # Automatic segmentation
    if segmentation_type == 'kmodes':
        # Run analysis
        clustering_data, removed_cols = process.clean_up(df)
        cluster_sizes, clustered_df = kmodes_clustering.set_up_and_cluster(clustering_data, cluster_vars = 'all',
                                                                           override_n_clusters = None)
        segmented_data = kmodes_clustering.return_full_clustered_df(clustered_df, df, removed_cols)

    # Rules-based segmentation
    elif segmentation_type == 'rules':
        segmented_data = rules_segmentation.segmentation(df, segmentation_cols = kwargs['segmentation_cols'])

    # Save data
    save_to_output.processed_responses(data = segmented_data, file_name = f'clustered_responses_{date_str}.csv')

    return segmented_data


def make_report(df: pd.DataFrame) -> pd.DataFrame:
    print("Instantiate class..")
    # Create instance
    salient_feats = SalientQuestions(df)
    print("Class has been instantiated")
    # Calc discover & deliver stats: seg_col= 'cluster' for auto clustering or 'question_code' for rules based
    salient_feats.create_summary_stats_df(seg_col = 'cluster')
    print("Summary stats have been calculated.")
    # Save data
    save_to_output.processed_responses(data = salient_feats.summary_stats,
                                       file_name = f'cluster_summary_stats_{date_str}.csv')

    return salient_feats.summary_stats


if __name__ == "__main__":

    parser = ArgumentParser(description="Run the sentiment model")  # todo: update appropriately
    parser.add_argument('mode', choices=['process', 'segment', 'report'], default='process',
                        help='Choose the mode: process, segment, or report.')
    parser.add_argument('-s', '--segmentation_type', choices = ['kmodes', 'rules'], default = 'kmodes',
                        help = "Choose the type of segmentation you'd like to run: kmodes or rules.")
    parser.add_argument('-c', '--segmentation_cols', nargs='+')  # Takes 1 or more column names (str)

    args = parser.parse_args()

    today = date.today()
    date_str = today.strftime("%b-%d-%Y").replace('-', '_')
    print(f"\nToday's date is '{date_str}'\n")

    if args.mode == 'process':
        data = load_data.response_data(id_column='ID')
        preprocess_data(df=data)

    if args.mode == 'segment':
        data = pd.read_csv(f"data/processed_data/response_data/processed_responses_{date_str}.csv")
        print("\nData upload successful.\n")

        # e.g. python main.py segment 'rules' -c 'Go City:AIDA_WW_ABA_IMS_07062021' 'DEM_WW_GENDER_RB_L_v3_14072020'
        segmented_df = segmentation(data, args.segmentation_type, segmentation_cols = args.segmentation_cols)
        print("Segmentation complete. \n")

    if args.mode == 'report':
        data = pd.read_csv(f'data/processed_data/response_data/clustered_responses_{date_str}.csv')
        try:
            summary_stats = make_report(data)
            print("Reporting complete. \n", summary_stats.head())
        except:
            print('Data not found. You must run the clustering step first.')
