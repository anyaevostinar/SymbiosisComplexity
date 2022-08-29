require(ggplot2)
library(viridis)


df <- read.table("./table.dat", h=T) # do python3 process.py first
final_df <- df




p<-ggplot(subset(subset(final_df, update=="200000"), vertical_transmission=="0.8"), aes(x=as.factor(squareNum), y=completions,fill = partner)) + geom_bar(stat = "identity",position=position_dodge())  + scale_y_log10() + theme(axis.text.x = element_text(size =4, angle = 90, vjust = 0.5, hjust=1), panel.background = element_rect(fill = "white")) + labs(x = "Square Numbers", y = "Completions")



print(p)