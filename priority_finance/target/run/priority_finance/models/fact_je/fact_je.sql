
  create view `03445d66`.`fact_je__dbt_tmp` as (
    






with fact_je as (
                    SELECT
                    '1'								                                as 'EntityID'
                    ,f.FNCNUM						                as 'JE_id'
                    ,f.KLINE						                as 'line_ID'
                    ,f.FNCLOTNUM					                as 'batch_num'
                    ,f.ACCNAME 					            as 'account_number'
                    ,f.ACCDES						        as 'account_name'
                    ,f.DC 					            as 'credit/debit'
                    ,f.FNCPATNAME					                    as 'JE_type'
                    ,f.DETAILS						                as 'details'
                    ,f.FNCDATE 					                as 'value_date'
                    ,f.CURDATE						        as 'refrence_date'
                    ,f.credit1					as 'credit_in_local_currency'
                    ,f.DEBIT1						as 'debit_in_local_currency'
                    ,f.credit3					as 'credit_in_foreign_currency'
                    ,f.DEBIT3			        as 'debit_in_foreign_currency'
                    ,f.BALDATE						        as 'balance_date'
                    ,f.IVNUM						            as 'refrence'
                    ,f.BOOKNUM						            as 'refrence_2'
                    ,f.IACCNAME						as 'offset_account_number'
                    ,f.IACCDES						    as 'offset_account_name'
                    ,f.USERLOGIN					                as 'username'
                    ,f.UDATE						        as 'JE_insert_date'
                    ,f.INSERTDATE					    as 'record_insert_timestamp'
                    ,f.LastModifiedDate				as 'record_last_modified_timestamp'
                    ,f.DEBIT1-f.credit1         as 'amount_in_local_currency'
                    ,f.DEBIT3-f.credit3		as 'amount_in_foreign_currency'
                    

                    from 03445d66.FNCLOG f
                )

select *
from fact_je
  );