-- models/example_model.sql

{{ config(materialized='view') }}

with source_data as (
                        select 
                                
                                acc.{{ var("var_account_num") }} as account_num
                                ,acc.{{ var("var_account_name") }} as account_name
                                ,acc.{{ var("var_english_account_name") }} as english_account_name
                                ,acc.{{ var("var_account_currency") }} as account_currency
                                ,acc.{{ var("var_level_1_code") }} as level_1_code
                                ,acc.{{ var("var_level_1_desc") }} as level_1_desc
                                ,acc.{{ var("var_level_2_desc") }} as level_2_desc
                                ,acc.{{ var("var_level_3_desc") }} as level_3_desc
                                ,acc.{{ var("var_pnl_flag") }} as pnl_flag
                                ,acc.{{ var("var_BS_title") }} as BS_title
                                ,acct.{{ var("var_order") }} as 'order'
                                ,acct.{{ var("var_pnl_impact") }} as pnl_impact
                                ,acct.{{ var("var_english_pnl_impact") }} as english_pnl_impact
                                

                        from {{ var("account_id") }}.accounts acc
                        left join {{ var("account_id") }}.acctypes acct
                                on (acc.ACCTYPENAME = acct.ACCTYPENAME)
                        )

select *
from source_data
