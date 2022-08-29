library(ggplot2)
library(viridis)
library(reshape2)
library(gridExtra)


df <- read.table("./table.dat", h=T) # do python3 process.py first
final_df <- subset(df, update =="50000")
#final_df$bin <- cut(final_df$squareNum, c(0, 5, 5^2, 5^3, 5^4, 5^5, 5^6, 5^7, 5^8, 5^9, 5^10, 5^11, 5^12, 5^13))
p<-ggplot(final_df, aes(x = as.factor(squareNum), y=completions, fill = partner, col = partner)) + 
geom_boxplot(alpha=0.5, outlier.size=0.25) + scale_y_log10()  + facet_wrap(vars(update, vertical_transmission), scales = "free") +
scale_color_manual(name="", values=viridis(3), guide=guide_legend(direction='horizontal')) + theme(axis.text.x = element_text(size =4, angle = 90, vjust = 0.5, hjust=1))


print(p)




