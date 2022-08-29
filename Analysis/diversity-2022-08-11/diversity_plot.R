require(ggplot2)
install.packages("viridis")
library(viridis)
library(gridExtra)

#library(ggplot2)
#library(viridis)
#library(reshape2)
#library(gridExtra)

#Set your working directory to the Analysis folder for your project

#Read in the data
df <- read.csv("./munged_diversity.csv", h=T)




p<-ggplot(data=df, aes(x=factor(VT_rate), y = alpha_diversity, color = partner)) + geom_boxplot(alpha=0.5, outlier.size=0.25) + xlab("vertical_transmission_rate") 

q<-ggplot(data=df, aes(x=factor(VT_rate), y = shannon_diversity, color = partner)) + geom_boxplot(alpha=0.5, outlier.size=0.25) + xlab("vertical_transmission_rate") 

grid.arrange(p,q, nrow=2)

df2 <- read.csv("./munged_diversity_phenotype_sums.csv", h=T)


r <- ggplot(data = df2, aes(x = "", y = sum_count, fill = factor(phenotype))) +
  geom_bar(width = 1, stat = 'identity') +
  coord_polar("y", start=0) +
  facet_wrap(~VT_rate) + theme_void()

print(r)


