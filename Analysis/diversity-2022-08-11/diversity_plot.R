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
df <- read.csv("C:/Users/katrina/Desktop/SymbulationProject/Analysis/munged_diversity.csv", h=T)




p<-ggplot(data=df, aes(x=factor(VT_rate), y = alpha_diversity, color = partner)) + geom_boxplot(alpha=0.5, outlier.size=0.25) + xlab("vertical_transmission_rate") 

q<-ggplot(data=df, aes(x=factor(VT_rate), y = shannon_diversity, color = partner)) + geom_boxplot(alpha=0.5, outlier.size=0.25) + xlab("vertical_transmission_rate") 


grid.arrange(p,q, nrow=2)
