-- models/example_model.sql



with source_data as (
                        select 
                                
                                acc.ACCNAME as account_num
                                ,acc.ACCDES as account_name
                                ,acc.EACCDES as english_account_name
                                ,acc.CODE as account_currency
                                ,acc.TRIALBALCODE as level_1_code
                                ,acc.TRIALBALDES as level_1_desc
                                ,acc.SECNAME as level_2_desc
                                ,acc.ACCTYPENAME as level_3_desc
                                ,acc.BALFLAG as pnl_flag
                                ,acc.BALTYPEDES as BS_title
                                ,acct.ORD as 'order'
                                ,acct.ACCTOTAL as pnl_impact
                                ,acct.EACCTOTAL as english_pnl_impact
                                

                        from 03445d66.accounts acc
                        left join 03445d66.acctypes acct
                                on (acc.ACCTYPENAME = acct.ACCTYPENAME)
                        )

select *
from source_data