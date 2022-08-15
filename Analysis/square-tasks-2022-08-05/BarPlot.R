require(ggplot2)
install.packages("viridis")
library(viridis)


df <- read.table("./table.dat", h=T) # do python3 process.py first
#final_df <- subset(df, update == "1000")
final_df <- df


p<-ggplot(final_df, aes(x=squareNum,y=completions,fill = partner)) + geom_bar(stat = "identity",width=0.5,position = "dodge") + scale_x_log10() + scale_y_log10() + facet_wrap(vars(update, vertical_transmission), scales = "free") 


print(p)




