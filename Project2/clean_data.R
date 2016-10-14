library(dplyr)
library(tidyr)

setwd("/home/bsnacks/Documents/CUNY/Web_Analytics_620/Project2")

df = tbl_df(read.csv("NDactors_edit.net",header = F,sep=' ',fill=TRUE))
df = df %>% gather("V2", "movie", 2:11) %>% select(-V2) %>% rename(actor=V1) %>% na.omit()

df$actor = sub("^","actor_", df$actor) # added to id for bipartite analytics
df$movie = sub("^","movie_", df$movie)

write.csv(df,"NDactors_edgelist_melt.csv",quote = T,row.names = F)






