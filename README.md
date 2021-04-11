# genetika+ pharmGKB db updates sop

--prerequisties     
1: install python
2: install pycharm                                  
3: download github desktop      
4: configure pycharm with github desktop

--SOP for pipeline dev and replication  
1: create python file that queries PharmGKB API to obtain download  
2: download .zip, unzip and extract to local disk   
3: convert to df and wrangle/clean to create abridged data set with attributes of interest  
4: write local df to postgres   
5: drop local df    
6: import postgres table into a different python file used to create reporting website  
