{{ config(materialized='view') }}


with fact_je as (
                    SELECT
                    '1'								                                as 'EntityID'
                    ,f.{{ var("var_JE_id") }}						                as 'JE_id'
                    ,f.{{ var("var_line_ID") }}						                as 'line_ID'
                    ,f.{{ var("var_batch_num") }}					                as 'batch_num'
                    ,f.{{ var("var_account_number") }} 					            as 'account_number'
                    ,f.{{ var("var_account_name") }}						        as 'account_name'
                    ,f.{{ var("var_credit/debit") }} 					            as 'credit/debit'
                    ,f.{{ var("var_JE_type") }}					                    as 'JE_type'
                    ,f.{{ var("var_details") }}						                as 'details'
                    ,f.{{ var("var_value_date") }} 					                as 'value_date'
                    ,f.{{ var("var_refrence_date") }}						        as 'refrence_date'
                    ,f.{{ var("var_credit_in_local_currency") }}					as 'credit_in_local_currency'
                    ,f.{{ var("var_debit_in_local_currency") }}						as 'debit_in_local_currency'
                    ,f.{{ var("var_credit_in_foreign_currency") }}					as 'credit_in_foreign_currency'
                    ,f.{{ var("var_debit_in_foreign_currency") }}			        as 'debit_in_foreign_currency'
                    ,f.{{ var("var_balance_date") }}						        as 'balance_date'
                    ,f.{{ var("var_refrence") }}						            as 'refrence'
                    ,f.{{ var("var_refrence_2") }}						            as 'refrence_2'
                    ,f.{{ var("var_offset_account_number") }}						as 'offset_account_number'
                    ,f.{{ var("var_offset_account_name") }}						    as 'offset_account_name'
                    ,f.{{ var("var_username") }}					                as 'username'
                    ,f.{{ var("var_JE_insert_date") }}						        as 'JE_insert_date'
                    ,f.{{ var("var_record_insert_timestamp") }}					    as 'record_insert_timestamp'
                    ,f.{{ var("var_record_last_modified_timestamp") }}				as 'record_last_modified_timestamp'
                    ,f.{{ var("var_debit_in_local_currency") }}-f.{{ var("var_credit_in_local_currency") }}         as 'amount_in_local_currency'
                    ,f.{{ var("var_debit_in_foreign_currency") }}-f.{{ var("var_credit_in_foreign_currency") }}		as 'amount_in_foreign_currency'
                    

                    from {{ var("account_id") }}.FNCLOG f
                )

select *
from fact_je

