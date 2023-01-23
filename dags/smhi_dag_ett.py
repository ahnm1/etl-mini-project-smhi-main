# Import modules
from airflow import DAG
from airflow.operators.python import PythonOperator 

from datetime import datetime
from etl_mini_project_smhi_main.source_to_raw import source_to_raw 
from etl_mini_project_smhi_main.raw_to_harmonized import raw_to_harmonized
from etl_mini_project_smhi_main.conn import DBWorker
from etl_mini_project_smhi_main import sql_to_df_to_plot




def _source_raw_to():
	source_to_raw.SourceToRaw()
	return 'source_to_raw'

def _raw_to_harmonized():
	raw_to_harmonized.RawToHarmonized()
	return 'raw_to_harmonized'

def _clean_to_db():
	db_worker = DBWorker()
	conn = db_worker.create_conn()
	dataframe = db_worker.read_json_to_df('data_harmonized.json')
	db_worker.add_data_to_db(dataframe, conn)
	return 'clean_to_db'

def _save_plot():
	df_to_plot = sql_to_df_to_plot
	df_to_plot.get_df()
	df_to_plot.plot_df()
	return 'save_plot'

with DAG(
	'smhi_dag',
	start_date        = datetime(2023, 1, 1),
	schedule_interval = '@daily',
	catchup           = False
	) as dag:

	source_to_raw_task = PythonOperator(
		task_id = 'source_to_raw',
		python_callable = _source_raw_to
	)

	raw_to_harmonized_task = PythonOperator(
		task_id = 'raw_to_harmonized',
		python_callable = _raw_to_harmonized
	)

	clean_to_db_task = PythonOperator(
		task_id = 'clean_to_db',
		python_callable = _clean_to_db
	)
	
	save_plot_task = PythonOperator(
		task_id = 'save_plot',
		python_callable = _save_plot
	)


	# operations at the same level are gruped in a 'list'
	source_to_raw_task >> raw_to_harmonized_task >> clean_to_db_task >> save_plot_task